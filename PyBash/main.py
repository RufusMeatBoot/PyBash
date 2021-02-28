from cmd import Cmd
import os
import socket
import time
import shutil
import sys


class Prompt(Cmd):

    user = socket.gethostname()

    def do_echo(self, args):
        """Print a string."""

        print(args)

    def do_exit(self, args):
        """Exit the shell."""

        try:
            raise SystemExit
        except:
            pass

    def do_clear(self, args):
        """Clear the shell."""

        if sys.platform == "win32" or sys.platform == "win64":
            try:
                os.system('cls')
            except:
                pass
        if sys.platform == "linux" or sys.platform == "linux2":
            try:
                os.system('clear')
            except:
                pass

    def do_cd(self, args):
        """Change current working directory."""

        try:
            if len(args) > 0:
                try:
                    os.chdir(args)
                except:
                    print("*** Unknown directory: " + args)
            else:
                try:
                    print(os.getcwd())
                except:
                    pass
        except:
            pass

    def do_pwd(self, args):
        """Print current working directory."""

        try:
            print(os.getcwd())
        except:
            pass

    def do_ls(self, args):
        """List files in a directory."""

        try:
            if len(args) == 0:
                for files in os.listdir(os.getcwd()):
                    print(files)
            else:
                for files in os.listdir(args):
                    print(files)
        except:
            print("*** Unknown directory: " + args)

    def do_mkdir(self, args):
        """Create a new folder."""

        try:
            os.mkdir(args)
        except:
            print("*** Unknown directory: " + args)

    def do_rmdir(self, args):
        """Remove a folder from device."""

        try:
            os.rmdir(args)
        except:
            print("*** Unknown file or folder: " + args)

    def do_eval(self, args):
        """Evaluate an expression."""

        try:
            output = eval(args)
            print(output)
        except:
            print("*** Invalid expression: " + args)

    def do_date(self, args):
        """Print the date."""

        try:
            now = time.localtime()
            print(time.strftime("%a %b %d %H:%M:%S %Y", now))
        except:
            pass

    def do_mv(self, args):
        """Move a file to a specified location."""

        try:
            directory = args[0]
            destination = args[1]
            shutil.move(directory, destination)
        except:
            pass


if __name__ == '__main__':
    name = "~/" + Prompt.user + "$ "
    prompt = Prompt()
    prompt.prompt = name
    prompt.cmdloop('PyBash v1.2.3. Type ? for a list of commands.\n')
