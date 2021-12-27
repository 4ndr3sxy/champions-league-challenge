"""Class/ object Team"""


class Team:
    """Constructor"""
    def __init__(self, name=0, league="", iq=0):
        self.__name = name
        self.__league = league
        self.__iq = iq
        self.__win = 0
        self.__lose = 0
        self.__tie = 0

    """Get name"""
    def get_name(self):
        return self.__name

    """Set name"""
    def set_name(self, value):
        self.__name = value

    """Get league of the team"""
    def get_league(self):
        return self.__league

    """Set leagie to team"""
    def set_league(self, value):
        self.__league == value

    """Get league of the team"""
    def get_iq(self):
        return self.__iq

    """Set leagie to team"""
    def set_iq(self, value):
        self.__iq = value

    """Get name"""
    def get_win(self):
        return self.__win

    """Get name"""
    def get_lose(self):
        return self.__lose

    """Get name"""
    def get_tie(self):
        return self.__tie

    def set_result_match(self, val):
        if val == 1:
            self.__win += 1
        elif val == 0:
            self.__tie += 1
        elif val == -1:
            self.__lose += 1
        else:
            None

    name = property(get_name, set_name)
    league = property(get_league, set_league)
    iq = property(get_iq, set_iq)
    win = property(get_win, set_result_match)
    lose = property(get_lose, set_result_match)
    tie = property(get_tie, set_result_match)

    def __str__(self):
        information = ""
        information += self.name + " - "
        information += self.league.name + " - "
        information += str(self.iq)
        return information
