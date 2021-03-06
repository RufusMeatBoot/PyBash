from cmd import Cmd
import os, sys, socket, shutil


class Prompt(Cmd):

    user = socket.gethostname()

    def do_echo(self, args):
        """Print a string."""

        print(args)

    def do_exit(self, args):
        """Exit the shell."""

        try:
            sys.exit()
        except:
            pass

    def do_clear(self, args):
        """Clear the shell."""

        try:
            os.system('cls')
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
            
    def do_rmtree(self, args):
        """Remove a folder and all of its contents."""
        
        try:
            shutil.rmtree(args)
        except:
            print("*** Unknown file or folder: " + args)


if __name__ == '__main__':
    name = "~/" + Prompt.user + "$ "
    prompt = Prompt()
    prompt.prompt = name
    prompt.cmdloop('PyBash v1.3.1. Type ? for a list of commands.\n')
