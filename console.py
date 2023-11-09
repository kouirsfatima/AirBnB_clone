#!/usr/bin/python3
""" console """
import cmd
from models.base_model import BaseModel
from models import storage
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.user import Amenity 

class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""

    prompt = '(hbnb) '

    classes = {
        "BaseMode" : BaseModel,
        "User" : User,
        "City" : City,
        "State" : State,
        "Place" : Place,
        "Amenity": Amenity,
        "review" : Review
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

    def do_all(self, line):
        args = line.split()
        new_list = []
        if len(args) == 0:
            for obj, in storage.all(). values():
                new_list.append(str(obj))
     
        elif args[0] in HBNBCommand.classes:
            for key,value in storage.all().item():
                if args[0] in key:
                    new_list.append(str(value))
        else:
            print ("** class doesn't exist **")
            return False

        print (new_list)     

if __name__ == '__main__':
    HBNBCommand().cmdloop()
