from classObj.Data_burn import Data
from classObj.Cup import Cup
from classObj.Team import Team
from classObj.Pot import Pot
import random

if __name__ == "__main__":
    """Creation UEFA champions"""
    uefa_champions = Cup("UEFA Champions League")

    cups = []
    count_teams = 0
    name_cups = []
    """Import list of objects"""
    list_objects = Data.teams_list

    """Creation Leagues and Teams"""
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

    for league in cups:
        print("\n---- LEAGUE: {} ----".format(league.get_name()))
        print(league.show_teams())
        # print(type(new_league.get_teams()))
        print("------- END League ---------")
        uefa_champions.set_teams(league.get_teams())
    print("\n---- TEAMS EUFA Champions league ----")
    print(uefa_champions.show_teams())  # Add league in Uefa
    print("--- END ---")

    """Order teams in UEFA with the best IQ"""
    print("\n---- TEAMS EUFA Champions league (ORDERED)----")
    sorted_teams = uefa_champions.get_teams()
    sorted_teams = sorted(sorted_teams, key=lambda x: x.iq)[::-1]
    uefa_champions.clean_teams()
    uefa_champions.set_teams(sorted_teams)
    uefa_champions.show_teams()
    print("--- END ---\n")
    """Order teams in UEFA with the best IQ (SUCCESS)"""

    """Create pots"""
    pots_uefa_collection = []
    pot_obj = Pot()
    pots_uefa_betters = pot_obj.create_pot(uefa_champions.get_teams())
    pots_uefa_collection.append(pots_uefa_betters)
    pot_obj.clean()
    pots_uefa_goods = pot_obj.create_pot(uefa_champions.get_teams())
    pots_uefa_collection.append(pots_uefa_goods)
    pot_obj.clean()
    pots_uefa_bads = pot_obj.create_pot(uefa_champions.get_teams())
    pots_uefa_collection.append(pots_uefa_bads)
    pot_obj.clean()
    pots_uefa_very_bads = pot_obj.create_pot(uefa_champions.get_teams())
    pots_uefa_collection.append(pots_uefa_very_bads)
    pot_obj.clean()
    for pot in pots_uefa_collection:
        print("---- Pot ----")
        for teams in pot:
            print(teams)
        print("---- END pot ----\n")
    """Create pots (SUCCESS)"""

    """Create groups in UEFA champions league"""
    groups = uefa_champions.create_groups(pots_uefa_collection)
    for obj in groups:
        print("---- Group {} ----".format(obj.name))
        for teams in obj.teams:
            print(teams)
        print("---- END Group ----\n")
    """Create groups in UEFA champions league (SUCCESS)"""
