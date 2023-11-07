#!/usr/bin/python3
""" console """
import cmd

class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(hbnb) '    
    def do_EOF(self, gs):
        """exit the program"""
        return True
    def emptyline(self):
        """an empty line + ENTER shouldnt execute anything"""
        return False
    def do_quit(self, gs):
        """Quit command to exit the programe"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
