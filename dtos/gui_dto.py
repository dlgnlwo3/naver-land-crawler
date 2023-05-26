if 1 == 1:
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


class GUIDto:
    def __init__(self):
        self.__city = ""
        self.__dvsn = ""
        self.__tradTpCd = ""
        self.__rletTpCd = ""

        self.__search_keyword = ""

    @property
    def city(self):  # getter
        return self.__city

    @city.setter
    def city(self, value):  # setter
        self.__city = value

    @property
    def dvsn(self):  # getter
        return self.__dvsn

    @dvsn.setter
    def dvsn(self, value):  # setter
        self.__dvsn = value

    @property
    def tradTpCd(self):  # getter
        return self.__tradTpCd

    @tradTpCd.setter
    def tradTpCd(self, value):  # setter
        delimiter = ","
        value = delimiter.join(value)
        self.__tradTpCd = value

    @property
    def rletTpCd(self):  # getter
        return self.__rletTpCd

    @rletTpCd.setter
    def rletTpCd(self, value):  # setter
        delimiter = ","
        value = delimiter.join(value)
        self.__rletTpCd = value

    @property
    def search_keyword(self):  # getter
        return self.__search_keyword

    @search_keyword.setter
    def search_keyword(self, value):  # setter
        self.__search_keyword = value

    def to_print(self):
        print("city: ", self.city)
        print("tradTpCd: ", self.tradTpCd)
        print("rletTpCd: ", self.rletTpCd)
