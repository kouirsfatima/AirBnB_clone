#!/usr/bin/python3
""" console """
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""

    prompt = '(hbnb) '

    classes = ["BaseModel", "Place", "User"]

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

    def do_show(self, line):

        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        if len(args) < 2:
            print("** instance id missing **")
            return False

        key = args[0] + "." + args[1]
        if key not in storage.all().keys():
            print("** no instance found **")
            return False

        obj = storage.all()[key]
        print(obj)

    def do_destroy(self, line):
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        if len(args) < 2:
            print("** instance id missing **")
            return False

        key = args[0] + '.' + args[1]
        if key not in storage.all().keys():
            print("** no instance found **")
            return False

        del storage.all()[key]
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
