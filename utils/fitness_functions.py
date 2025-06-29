from collections import Counter

def compute_project_satisfaction(team, project_name):
    scores = {'Choice 1': 1.0, 'Choice 2': 0.8, 'Choice 3': 0.6, 'Choice 4': 0.4, 'Choice 5': 0.2}
    
    satisfaction_scores = []
    for member in team:
        score = 0.0
        matched = False
        for choice, value in scores.items():
            if member[choice] == project_name:
                score = value
                print(f"{member['ID']} got project satisfaction score {score}, since {project_name} was their {choice}")
                matched = True
                break
        if not matched:
            print(f"{member['ID']} got project satisfaction score 0.0 (No matching choice)")
        satisfaction_scores.append(score)
    
    return sum(satisfaction_scores) / len(satisfaction_scores)

def compute_belbin_diversity(team):
    roles = [member['Belbin'] for member in team]
    role_counts = Counter(roles)
    n = len(team)

    print(f"Belbin Roles: {roles}")

    # Compute Blau index
    proportions = [count / n for count in role_counts.values()]
    raw_blau = 1 - sum(p ** 2 for p in proportions)
    adjusted_blau = (n / (n - 1)) * raw_blau

    return adjusted_blau

def evaluate_team(team, project_name, lambda_1=0.5, lambda_2=0.5):

    print("="*40)
    print(f"Evaluating team for project: {project_name}")
    print(f"Members: {[member['ID'] for member in team]}")

    satisfaction = compute_project_satisfaction(team, project_name)
    print(f"-> Average satisfaction for project '{project_name}': {satisfaction:.2f}")

    diversity = compute_belbin_diversity(team)
    print(f"-> Diversity score: {diversity:.2f}\n")

    score = lambda_1 * satisfaction + lambda_2 * diversity
    print(f"-> Overall score: {score:.2f}\n")
    return score

def evaluate_all_teams(team_assignments, lambda_1=0.5, lambda_2=0.5):
    
    team_fitness_scores = []

    for team in team_assignments:

        print(f"Team ID: {team.team_id}")
        fitness = evaluate_team(team.members, team.project, lambda_1, lambda_2)
        team.fitness = fitness
        team_fitness_scores.append(fitness)

    # Return average fitness for the entire population
    return sum(team_fitness_scores) / len(team_fitness_scores)

def evaluate_objectives_separately(team_assignments):
    
    total_diversity = 0.0
    total_satisfaction = 0.0

    for team in team_assignments:

        print("="*40)
        print(f"Evaluating team for project: {team.project}")
        print(f"Members: {[member['ID'] for member in team.members]}")
        
        satisfaction = compute_project_satisfaction(team.members, team.project)
        total_satisfaction += satisfaction
        print(f"-> Average satisfaction for project '{team.project}': {satisfaction:.2f}")

        diversity = compute_belbin_diversity(team.members)
        total_diversity += diversity
        print(f"-> Diversity score: {diversity:.2f}\n")

    avg_div = total_diversity / len(team_assignments)
    avg_sat = total_satisfaction / len(team_assignments)

    return avg_div, avg_sat