import math

def is_valid_team(members):

    student_count = len(members)
    if student_count not in [5, 6]:
        return False

    tcs_count = sum(1 for member in members if member.get('Program') == 'B-TCS')
    if tcs_count > 4:
        return False

    nationality_counts = {}
    for member in members:
        nationality = member.get('Nationality')
        nationality_counts[nationality] = nationality_counts.get(nationality, 0) + 1

    for nat, count in nationality_counts.items():
        if nat != 'Dutch' and count > 3:
            return False

    return True

def is_valid_arrangement(team_arrangement, total_students, projects):

    # Rules 1-3:
    if not all(is_valid_team(team) for team in team_arrangement):
        return False

    # Rule 4: Each student must be in exactly one team.
    all_ids = [member['ID'] for team in team_arrangement for member in team.members]

    unique_ids = set(all_ids)
    if len(all_ids) != total_students:
        return False  # Some students are missing or duplicated
    if len(unique_ids) != total_students:
        return False  # Some students appear more than once

    # Rule 5: Maximum number of teams per project = [Ideal number of teams/Number of projects]
    num_teams = len(team_arrangement)
    max_per_project = math.ceil(num_teams / len(projects))

    project_counts = {}
    for team in team_arrangement:
        project = team.project
        project_counts[project] = project_counts.get(project, 0) + 1

    for project, count in project_counts.items():
        if count > max_per_project:
            return False
        
    return True