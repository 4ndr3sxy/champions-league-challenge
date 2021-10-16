from classObj.Data_burn import Data
from classObj.Cup import Cup
from classObj.Team import Team
import random

if __name__ == "__main__":
    cups = [[]]
    count_teams = 0
    name_cups = []
    name_teams = []
    """Import list of objects"""
    list_objects = Data.teams_list
    """Create team and Cups"""
    validate_name_Cup = False
    for team, league in list_objects:
        if league not in name_cups:
            name_cups.append(league)
            new_league = Cup(league)
            cups.append(new_league)
        else:
            for cup in cups:
                if type(cup) is Cup and cup.name == league:
                    new_league = cup
                    break
        iq_random = random.randint(1, 100)
        new_team = Team(team, new_league, iq_random)
        new_league.teams = new_team

    """Creation Leagues and Teams CORRECT"""

