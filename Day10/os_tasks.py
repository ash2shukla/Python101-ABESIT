import os
import shutil
import glob


def python_basic_os():
    # get current working directory
    print(os.getcwd())
    # Change current working directory
    os.chdir('/usr')
    # Print changed working directory
    print(os.getcwd())
    # Invoke a command on system
    # Command to start firefox from terminal
    # os.system('firefox')


def python_ls():
    # Get a list of all the names (sub-dirs and files) in a directory
    # * stands for a wildcard means everything
    # Instead of * we can give the regex we want to match
    contents = glob.glob('*')
    print(contents)


def python_ls_with_grep(pattern):
    print(glob.glob(pattern))
    # iglob returns a generator than returning a simple list.
    # Extremely useful if we do not have an estimate of how long
    # matched content can be
    for i in glob.iglob(pattern):
        print(i)


def paths():
    # Get absolute path of the file __main__ ie. current file
    print(os.path.abspath(__name__))
    # Get relative path of Day1 directory from Day10
    print(os.path.relpath('/home/troll/Python101-ABESIT/Day10',
                          '/home/troll/Python101-ABESIT/Day1'))
    # Get directory name from absolute path of the current file
    print(os.path.dirname(os.path.abspath(__name__)))
    # Join two parts of path
    print(os.path.join(os.path.dirname(os.path.abspath(__name__)), 'os_tasks.py'))


def copy_or_move():
    # Lets create a file
    file = open('some_file', 'w')
    file.close()
    # Lets copy this file into our parent directory
    shutil.copyfile('some_file', os.path.join(os.getcwd(),'..','new_filename'))
    # and Lets move this file into our Day1 directory
    shutil.move('some_file', os.path.join(os.path.join(os.getcwd(),'..'), 'Day1','new_filename'))


if __name__ == "__main__":
    # python_basic_os()
    # python_ls()
    # python_ls_with_grep('*.py')
    # paths()
    copy_or_move()