
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
