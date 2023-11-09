#!/usr/bin/python3
""" console """
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""

    prompt = '(hbnb) '

    classes = {
    "BaseModel": BaseModel,
    }

    def do_EOF(self, line):
        """exit the program"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldnt execute anything"""
        pass

    def do_quit(self, line):
        """Quit command to exit the programe"""
        return True
    def do_create(self, line):
        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            storage.save()
            print(new.id)
if __name__ == '__main__':
    HBNBCommand().cmdloop()
