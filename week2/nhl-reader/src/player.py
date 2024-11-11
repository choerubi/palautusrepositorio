class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.points = self.goals + self.assists
        self.nationality = dict['nationality']
    
    def __str__(self):
        return f"{self.name:20} {self.team:5} {self.goals} + {self.assists} = {self.points}"

    def __lt__(self, other):
        return self.points < other.points
