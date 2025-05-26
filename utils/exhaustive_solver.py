import itertools
from itertools import combinations
from functools import lru_cache
from copy import deepcopy
from models.team_assignment import TeamAssignment
import utils.restriction_checker as rc
import utils.fitness_functions as ff
import io
import os
from contextlib import redirect_stdout
import math
import time

PROJECTS = ['Shotmaniacs', 'actFact', 'Honours Programme', 'Voice', 'Topicus', 'Earnit', 'Inter-actief']

def generate_valid_partitions(students, team_sizes=(5, 6)):
    n = len(students)

    # Step 1: Precompute all valid team size combinations
    @lru_cache(maxsize=None)
    def team_size_combinations(total, sizes):
        if total == 0:
            return [[]]
        combos = []
        for size in sizes:
            if total >= size:
                for rest in team_size_combinations(total - size, sizes):
                    combos.append([size] + rest)
        return combos

    valid_team_size_combos = team_size_combinations(n, team_sizes)

    # Step 2: For each team size combo, yield all valid partitions
    def partition_by_sizes(remaining_students, sizes):
        if not sizes:
            yield []
            return
        size = sizes[0]
        for team in combinations(remaining_students, size):
            rest = [s for s in remaining_students if s not in team]
            for subpartition in partition_by_sizes(rest, sizes[1:]):
                yield [list(team)] + subpartition

    all_partitions = []
    seen = set()

    for size_combo in valid_team_size_combos:
        for partition in partition_by_sizes(students, size_combo):
            # Canonicalize partition to avoid duplicates
            key = tuple(sorted(tuple(sorted(member['ID'] for member in team)) for team in partition))
            if key not in seen:
                seen.add(key)
                all_partitions.append(partition)

    return all_partitions

def is_valid_project_assignment(assignment, projects):
    from collections import Counter
    max_per_project = math.ceil(len(assignment) / len(projects))
    counts = Counter(assignment)
    return all(count <= max_per_project for count in counts.values())

def generate_project_assignments(num_teams, projects):
    return itertools.product(projects, repeat=num_teams)

def build_team_assignments(team_partition, project_assignment):
    team_assignments = []
    project_counts = {}  # Track number of teams per project.

    for (team, project) in zip(team_partition, project_assignment):

        count = project_counts.get(project, 0) + 1
        project_counts[project] = count

        team_id = f"{project} {count}"
        team_assignments.append(TeamAssignment(team_id, team, project, fitness=0.0))
    return team_assignments

def save_best_arrangement(arrangement, df, dataset_name):

    # Create output directory
    base_dir = "output"
    os.makedirs(base_dir, exist_ok=True)

    # Output optimal arrangement
    filename = os.path.join(base_dir, f"optimal_arrangement_{dataset_name}.txt")
    with open(filename, "w") as f:
        with redirect_stdout(f):
            score = ff.evaluate_all_teams(arrangement, df)
            print(f"\nFinal score for arrangement: {score:.4f}")

def find_best_arrangement(df, dataset_path):

    # Extract dataset filename for caching (not unnecessarily recomputing).
    dataset_name = os.path.splitext(os.path.basename(dataset_path))[0]
    output_path = os.path.join("output", f"optimal_arrangement_{dataset_name}.txt")

    # Skip if best arrangement for this dataset has already been computed, and returns value from file.
    if os.path.exists(output_path):
        with open(output_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                if "Final score for arrangement" in line:
                    try:
                        score_str = line.strip().split(":")[-1]
                        score = float(score_str)
                    except ValueError:
                        pass
                if "Evaluated combinations" in line:
                    try:
                        count_str = line.strip().split(":")[-1]
                        arrangements_computed = float(count_str)
                    except ValueError:
                        pass
            return None, score, arrangements_computed
        
    start_time = time.time()

    students = df.to_dict(orient='records')
    best_score = -1
    best_arrangement = None
    total_students = len(df)
    evaluated_count = 0

    partitions = generate_valid_partitions(students)

    for team_partition in partitions:
        if len(team_partition) > len(PROJECTS):
            continue

        for project_assignment in generate_project_assignments(len(team_partition), PROJECTS):
            evaluated_count += 1
            if not is_valid_project_assignment(project_assignment, PROJECTS):
                continue

            team_assignments = build_team_assignments(team_partition, project_assignment)

            if not rc.is_valid_arrangement(team_assignments, total_students, PROJECTS):
                continue

            f = io.StringIO()
            with redirect_stdout(f): # Supresses internal prints from evaluate_all_teams() function
                score = ff.evaluate_all_teams(team_assignments, df)

            if score > best_score:
                best_score = score
                best_arrangement = deepcopy(team_assignments)

    end_time = time.time()
    execution_time = end_time - start_time
    save_best_arrangement(best_arrangement, df, dataset_name) # Outputs best arrangement
    with open(os.path.join("output", f"optimal_arrangement_{dataset_name}.txt"), "a") as f: # Log evaluated combinations
        f.write(f"\nEvaluated combinations: {evaluated_count}\n")
        f.write(f"\nExecution Time: {execution_time:.4f} seconds\n")
    return best_arrangement, best_score, evaluated_count