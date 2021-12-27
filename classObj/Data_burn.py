from classObj.Team import Team
from classObj.Cup import Cup
import random

class Data:
    list_object_teams = []
    teams_list = [
    ["Atalanta","Italian Serie A"],
    ["Aston Villa","English Premier League"],
    ["Ajax","Dutch First Division"],
    ["Alkmaar", "Dutch First Division"],
    ["Atlético","The Spanish league"],
    ["Angers","Turn 1 French"],
    ["Athletic Club","The Spanish league"],
    ["Barcelona","The Spanish league"],
    ["Bayern", "German Bundesliga"],
    ["Benfica","Portuguese First Division"],
    ["Betis","The Spanish league"],
    ["Braga","Portuguese First Division"],
    ["Brighton","English Premier League"],
    ["Brentford","English Premier League"],
    ["Boavista","Portuguese First Division"],
    ["Bologna","Italian Serie A"],
    ["Chelsea","English Premier League"],
    ["CSKA Moskva","Russian league"],
    ["Dortmund","German Bundesliga"],
    ["Dynamo Kyiv","Russian league"],
    ["Empoli","Italian Serie A"],
    ["Estoril","Portuguese First Division"],
    ["Everton","English Premier League"],
    ["Feyenoord", "Dutch First Division"],
    ["Fiorentina","Italian Serie A"],
    ["Freiburg","German Bundesliga"],
    ["Gil Vicente","Portuguese First Division"],
    ["Groningen", "Dutch First Division"],
    ["Internazionale","Italian Serie A"],
    ["Juventus","Italian Serie A"],
    ["Köln", "German Bundesliga"],
    ["Krasnodar","Russian league"],
    ["Krylya Sovetov","Russian league"],
    ["Heerenveen", "Dutch First Division"],
    ["Lazio","Italian Serie A"],
    ["Leverkusen", "German Bundesliga"],
    ["Leipzig","German Bundesliga"],
    ["Lens","Turn 1 French"],
    ["Liverpool","English Premier League"],
    ["Lorient","Turn 1 French"],
    ["Lokomotiv Moskva","Russian league"],
    ["Lyon","Turn 1 French"],
    ["LOSC","Turn 1 French"],
    ["Marseille","Turn 1 French"],
    ["Mönchengladbach","German Bundesliga"],
    ["Monaco","Turn 1 French"],
    ["Mainz","German Bundesliga"],
    ["Man. City","English Premier League"],
    ["Man. United","English Premier League"],
    ["Milan","Italian Serie A"],
    ["Nantes","Turn 1 French"],
    ["Nice","Turn 1 French"],
    ["Nizhny Novgorod","Russian league"],
    ["Napoli","Italian Serie A"],
    ["Osasuna","The Spanish league"],
    ["Paris","Turn 1 French"],
    ["PSV","Dutch First Division"],
    ["Porto","Portuguese First Division"],
    ["Portimonense","Portuguese First Division"],
    ["Rayo Vallecano","The Spanish league"],
    ["Real Madrid","The Spanish league"],
    ["Real Sociedad","The Spanish league"],
    ["Roma","Italian Serie A"],
    ["Rubin","Russian league"],
    ["Sevilla","The Spanish league"],
    ["Spartak Moskva","Russian league"],
    ["Sochi","Russian league"],
    ["Sporting CP","Portuguese First Division"],
    ["Twente", "Dutch First Division"],
    ["Tottenham","English Premier League"],
    ["Tondela","Portuguese First Division"],
    ["Union Berlin","German Bundesliga"],
    ["Utrecht", "Dutch First Division"],
    ["Valencia","The Spanish league"],
    ["Vitesse","Dutch First Division"],
    ["Vitória SC","Portuguese First Division"],
    ["Wolfsburg","German Bundesliga"],
    ["West Ham","English Premier League"],
    ["Zenit","Russian league"],
    ["Zwolle", "Dutch First Division"],
    ]

    @classmethod
    def create_list_object_team(cls):
        print("Test Data Burn 1")
        print("-----------------------")
        list_teams = []
        list_league = []
        for team, league in cls.teams_list:
            new_league = Cup(league)
            if new_league not in list_league:
                list_league.append(new_league)
            for league2 in list_league:
                if league2.name == league:
                    rnd = random.randint(1, 100)
                    new_team = Team(team, league2, rnd)
                    list_teams.append(new_team)
                    print("New team:")
                    print("\t{} - {} - {}".format(new_team.name, new_team.league.name, new_team.iq))
                    break

        for league in list_league:
            print(league)
        print("-----------------------\n")
