class TeamAssignment:
    def __init__(self, team_id, members, project, fitness):
        self.team_id = team_id
        self.members = members
        self.project = project
        self.fitness = fitness

    def __repr__(self):
        return f"Team {self.team_id}: {self.members} | Project: {self.project} | Fitness: {self.fitness:.4f}"
