import random

class Group:
    count_instances = 0

    def __init__(self):
        Group.count_instances += 1
        self.__name = Group.count_instances
        self.__teams = []

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_teams(self):
        return self.__teams

    def set_teams(self, obj):
        self.__teams.append(obj)

    name = property(get_name, set_name)
    teams = property(get_teams, set_teams)

    def play_games(self):
        for i in range(len(self.teams) - 1):
            for j in range(i, len(self.teams) - 1):
                # print(type(self.teams[i]))
                print("{} VS {}:".format(self.teams[i].name, self.teams[j + 1].name))
                self.logic_play_game(self.teams[i], self.teams[j + 1])


            # print("empiezan los juegos {}".format(i))

    def logic_play_game(self, team1, team2):
        # print("{} VS {}".format(team1.name, team2.name))
        total_iq = team1.iq + team2.iq
        print("\tiq={} VS iq={} -> total iq={}".format(team1.iq, team2.iq, total_iq))
        rnd = random.randint(0, total_iq)
        print("\trandom {}".format(rnd))
        print("\t", end='')
        if rnd <= team1.iq:
            print("Victoria: {}".format(team1.name))
            team1.set_result_match(1)
            team2.set_result_match(-1)
        else:
            print("Victoria: {}".format(team2.name))
            team1.set_result_match(-1)
            team2.set_result_match(1)
        print("")

    def results(self):
        for teams in self.teams:
            print("\t{} - V={} | L={}".format(teams.name, teams.win, teams.lose))
