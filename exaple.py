#!/usr/bin/python3
class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

usr1 = User("mouad")
usr2 = User("fatima ez-zahra")

a = [str(usr1), str(usr2)]
print(a)

