import math

def is_valid_team(members):

    student_count = len(members)
    if student_count not in [5, 6]:
        return False, f"Invalid number of students ({student_count})."

    tcs_count = sum(1 for member in members if 'TCS' in member.get('Program'))
    if tcs_count > 4:
        return False, f"Too many TCS students ({tcs_count})."

    nationality_counts = {}
    for member in members:
        nationality = member.get('Nationality')
        nationality_counts[nationality] = nationality_counts.get(nationality, 0) + 1

    for nat, count in nationality_counts.items():
        if nat != 'Dutch' and count > 3:
            return False, f"Too many {nat} students ({count})."

    return True, None

def is_valid_arrangement(team_arrangement, total_students, projects):

    invalid_reasons = []

    # Rules 1-3:
    for team in team_arrangement:
            valid, reason = is_valid_team(team.members)
            if not valid:
                invalid_reasons.append((team.team_id, reason))

    # Rule 4: Each student must be in exactly one team.
    all_ids = [member['ID'] for team in team_arrangement for member in team.members]

    unique_ids = set(all_ids)
    if len(all_ids) != total_students:
        invalid_reasons.append((None, "Some students are missing or duplicated."))
    if len(unique_ids) != total_students:
        invalid_reasons.append((None, "Some students appear more than once."))

    # Rule 5: Maximum number of teams per project = [Ideal number of teams/Number of projects]
    num_teams = len(team_arrangement)
    max_per_project = math.ceil(num_teams / len(projects))

    project_counts = {}
    for team in team_arrangement:
        project = team.project
        project_counts[project] = project_counts.get(project, 0) + 1

    for project, count in project_counts.items():
        if count > max_per_project:
            invalid_reasons.append((None, f"{count} teams are doing the {project} project, out of a maximum of {max_per_project} teams."))

    if len(invalid_reasons) == 0:
        return True, None
    else:
        return False, invalid_reasons