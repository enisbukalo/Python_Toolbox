"""
This Module is in charge of accepting a user input file location,
taking that file location, determining if it is the correct extension,
if so then converting the UI file created by QT Designer into usable
Python Code.
"""
from subprocess import Popen
from os.path import join
from shutil import move


class QtConverter():
    """
    This class will handle all aspects of this operation in order.
    """
    def __init__(self, uisrc, pydst, resourcesrc=None, newname=None):
        self.ui_location = uisrc
        self.py_destination = pydst
        self.resource_location = resourcesrc
        self.new_name = newname
        self.file_to_convert = self.ui_location.split('/')[-1]

        self.CallCommandLine()

    def CallCommandLine(self):
        """
        This function will pull open a command line on windows.
        It then executes the desired commands.
        """
        if self.new_name is not None or self.new_name == "":
            if self.new_name.split(".")[-1] == "py":
                file_name = self.new_name
            else:
                file_name = "{0}.py".format(self.new_name)
        else:
            file_name = self.file_to_convert.replace('.ui', '.py')

        """Sends Command to CMD"""
        curr_cwd = "/".join(self.ui_location.split("/")[:-1])
        command_to_send = ('pyuic5 -o {1} {0}').format(
                self.file_to_convert,
                file_name)
        p = Popen(command_to_send, cwd=curr_cwd)
        p.wait()

        """Moves newely created python script to the destination"""
        if self.py_destination is not None:
            move(join(curr_cwd,
                      file_name),
                 join(self.py_destination,
                      file_name))

        if (
                self.resource_location is not None
                or self.resource_location == ""):

            res_file_to_convert = self.resource_location.split('/')[-1]
            res_file_py_version = res_file_to_convert.replace(".qrc", ".py")
            curr_cwd = "/".join(self.resource_location.split("/")[:-1])

            """Generates the resource.py file"""
            command_to_send = ('pyrcc5 {0} -o {1}').format(
                    res_file_to_convert,
                    res_file_py_version)
            p = Popen(command_to_send, cwd=curr_cwd)
            p.wait()
