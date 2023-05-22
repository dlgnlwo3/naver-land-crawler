if 1 == 1:
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


class GUIDto:
    def __init__(self):
        self.__account_file = ""

        self.__user_id = ""
        self.__user_pw = ""
        self.__keyword = ""

        self.__delete_count = ""
        self.__delete_all = bool

    @property
    def account_file(self):  # getter
        return self.__account_file

    @account_file.setter
    def account_file(self, value):  # setter
        self.__account_file = value

    @property
    def user_id(self):  # getter
        return self.__user_id

    @user_id.setter
    def user_id(self, value):  # setter
        self.__user_id = value

    @property
    def user_pw(self):  # getter
        return self.__user_pw

    @user_pw.setter
    def user_pw(self, value):  # setter
        self.__user_pw = value

    @property
    def keyword(self):  # getter
        return self.__keyword

    @keyword.setter
    def keyword(self, value):  # setter
        self.__keyword = value

    @property
    def delete_count(self):  # getter
        return self.__delete_count

    @delete_count.setter
    def delete_count(self, value):  # setter
        self.__delete_count = value

    @property
    def delete_all(self):  # getter
        return self.__delete_all

    @delete_all.setter
    def delete_all(self, value: bool):  # setter
        self.__delete_all = value

    def to_print(self):
        print("account_file: ", self.account_file)
        print("keyword: ", self.keyword)
        print("delete_count: ", self.delete_count)
        print("delete_all: ", self.delete_all)
