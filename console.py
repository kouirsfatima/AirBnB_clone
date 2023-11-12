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
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""

    prompt = '(hbnb) '

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "City": City,
        "State": State,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
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

    def handle_error(self, line, name):
        """Handler for method's error (helper function)
        return 0 if no error found otherwise 1
        """
        args = line.split()

        if len(args) < 1:
            print("** class name missing **")
            return 1

        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return 1

        if name in ["update", "show", "destroy"]:
            if len(args) < 2:
                print("** instance id missing **")
                return 1

            key = args[0] + "." + args[1]
            if key not in storage.all().keys():
                print("** no instance found **")
                return 1

        if name == "update":
            if len(args) < 3:
                print("** attribute name missing **")
                return 1
            if len(args) < 4:
                print("** value missing **")
                return 1
        return 0

    def do_create(self, line):
        """Creates a new instance and print it's id:
Usage: create <class name>
        """
        if self.handle_error(line, "create") == 0:
            args = line.split()
            # args[0] ==> class_name (type str)
            class_name = HBNBCommand.classes[args[0]]
            new = class_name()
            storage.save()
            print(new.id)

    def do_show(self, line):
        """Prints the string representation of an instance:
Usage: show <class name> <instance id>
        """
        if self.handle_error(line, "show") == 0:
            args = line.split()
            key = args[0] + '.' + args[1]
            obj = storage.all()[key]
            print(obj)

    def do_destroy(self, line):
        """Deletes an instance
Usage: destroy <instance id>
        """
        if self.handle_error(line, "destroy") == 0:
            args = line.split()
            key = args[0] + '.' + args[1]
            if key not in storage.all().keys():
                print("** no instance found **")
                return False

            del storage.all()[key]
            storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
Usage 1: all
Usage 2: all <class name>
        """
        args = line.split()
        new_list = []
        if len(args) == 0:
            for obj in storage.all().values():
                new_list.append(str(obj))

        elif args[0] in HBNBCommand.classes:
            for key, value in storage.all().items():
                if args[0] in key:
                    new_list.append(str(value))
        else:
            print("** class doesn't exist **")
            return False

        print(new_list)

    def do_update(self, line):
        """Updates an instance by adding or updating attribute:
Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        if self.handle_error(line, "update") == 0:
            args = line.split()
            class_name = args[0]
            obj_id = args[1]
            att_name = args[2]
            att_value = args[3]
            key = class_name + "." + obj_id
            obj = storage.all()[key]

            if (
                att_value[0] == "'" and att_value[-1] == "'" or
                att_value[0] == "\"" and att_value[-1] == "\""
            ):
                att_value = att_value[1:-1]
            if hasattr(obj, att_name):
                val = getattr(obj, att_name)
                att_type = type(val)
                try:
                    setattr(obj, att_name, att_type(att_value))
                except ValueError:
                    print(f"can't update {att_name} to {att_value}")
            else:
                setattr(obj, att_name, att_value)
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
