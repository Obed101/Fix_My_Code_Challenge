#!/usr/bin/python3
""" User class """


class User():
    """ Documentation Of the Class"""

    def __init__(self, email):
        """ Init is handling all instanced"""
        self.__email = email

    @property
    def email(self, value):
        """ this is the email """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value

    @email.getter
    def email(self):
        """ this is getter for email """
        return self.__email


if __name__ == "__main__":

    u = User("john@snow.com")
    print(u.email)
