
class Group:
    def __init__(self, name="", list_teams={}):
        self.__name = name
        self.__list_teams = list_teams

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_list_teams(self):
        return self.__list_teams

    def set_list_teams(self, key, value):
        self.__list_teams[key] = value

    name = property(get_name, set_name)
    list_teams = property(get_list_teams, set_list_teams)
