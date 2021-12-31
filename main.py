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

    """Init games in team of the each group"""
    print("--- Empiezan los encuentros ---")
    for i in range(0,2):
        if i == 0:
            print("--- Ida ---")
        else:
            print("--- Vuelta ---")
        for obj in groups:
            print("---- Group {} ----".format(obj.name))
            obj.play_games()
            print("\t---- Results Group {} ----".format(obj.name))
            obj.results()
            print("\t---- END results ----\n".format(obj.name))
            print("---- END Group ----\n")
    """Init games in team of the each group (SUCCESS)"""
    
    """Order teams in each group by wins"""
    print("\n---- TEAMS in each group (ORDERED by wins)----\n")
    for group in groups:
        sorted_teams_group = group.teams
        sorted_teams_group = sorted(sorted_teams_group, key=lambda x: x.win)[::-1]
        group.clean()
        for team in sorted_teams_group:
            group.teams = team
        print("---- Group {} ----".format(group.name))
        for teams in group.teams:
            print("{} -> P={} V={}, L={}".format(teams.name, teams.points, teams.win, teams.lose))
        print("---- END Group ----\n")
    print("--- END ---\n")
    """Order teams in each group by wins (SUCCESS)"""

    """"OCTAVOS"""
    print("--- Octavos ---")
    heads = Pot()
    n_heads = Pot()
    for group in groups:
        heads.teams = group.teams[0]
        n_heads.teams = group.teams[1]
        # print(group.teams[0])
        # for team in group.teams:
    # print(heads.teams)
    # print(n_heads)
    # print(heads.teams[1])
    print("\n--- Teams heads ---")
    for team in heads.teams:
        print(team)
    print("--- END ---")
    print("\n--- Teams NO heads ---")
    for team in n_heads.teams:
        print(team)
    print("--- END ---\n")

    """Sorteo OCTAVOS"""
    print("""---- Sorteo OCTAVOS ----""")
    # uefa_champions_octavos = Cup()
    octavos = uefa_champions.shuffle(heads, n_heads)
    for teams in octavos:
        print("{} - {}".format(teams[0].name, teams[1].name)) 
    print("""---- END ----\n""")
    groups_octavos = uefa_champions.create_groups(octavos, 2)
    # print(groups_octavos[0].teams[0])
    uefa_champions.clean_result()
    print("--- Empiezan los encuentros ---")
    for k in range(0, 2):
        if k == 0:
            print("--- Ida ---")
        else:
            print("--- Vuelta ---")
        for i in range(0, 8):
            team1 = groups_octavos[0].teams[i]
            team2 = groups_octavos[1].teams[i]
            groups_octavos[0].logic_play_game(team1, team2)

    # for group in octavos:
    #     print("---- Group {} ----".format(" "))
    #     print(group)
    #     for teams in group:
    #         print("{} -> P={} V={}, L={}".format(teams.name, teams.points, teams.win, teams.lose))
    #     #     print(teams)
    #     print("---- END Group ----\n")

    for group in groups_octavos:
        print("---- Group ----")
        for teams in group.teams:
            print("{} -> P={} V={}, L={}".format(teams.name, teams.points, teams.win, teams.lose))
        #     print(teams)
        print("---- END Group ----\n")
    
    print("---- Clasificados Cuartos ----")
    pot_uefa_champions_cuartos = Pot()
    for i in range(0, 8):
        team1 = groups_octavos[0].teams[i]
        team2 = groups_octavos[1].teams[i]
        # print(team1.points)
        # print(team2.points)
        if team1.points == team2.points:
            random_win = random.randint(0, 1)
            if random_win == 0:
                pot_uefa_champions_cuartos.teams = team1
            else:
                pot_uefa_champions_cuartos.teams = team2
        elif team1.points > team2.points:
            pot_uefa_champions_cuartos.teams = team1
        else:
            pot_uefa_champions_cuartos.teams = team2




        # groups_octavos[0].logic_play_game(team1, team2)
    for team in pot_uefa_champions_cuartos.teams:
        print(team)
    print("---- END Clasificados Cuartos ----")

    """OCTAVOS SUCCESS"""
