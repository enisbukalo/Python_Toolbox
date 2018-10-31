"""
This Module is in charge of accepting a user input file location,
taking that file location, determining if it is the correct extension,
if so then converting the UI file created by QT Designer into usable
Python Code.
"""
from subprocess import Popen
from os import remove
from os.path import join
from os.path import expanduser as exp
from shutil import copy
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
        self.pyuic_location = join(
                exp("~"),
                "AppData",
                "Local",
                "Programs",
                "Python",
                "Python37-32",
                "Scripts")
        self.file_to_convert = self.ui_location.split('/')[-1]

        self.CallCommandLine()

    def CallCommandLine(self):
        """
        This function pull open a command line on windows.
        It then executes the desired commands.
        """
        if self.new_name is not None or self.new_name == "":
            if self.new_name.split(".")[-1] == "py":
                file_name = self.new_name
            else:
                file_name = "{0}.py".format(self.new_name)
        else:
            file_name = self.file_to_convert.replace('.ui', '.py')

        """Copies UI file into pyuic5.bat location"""
        copy(self.ui_location, join(
                self.pyuic_location,
                self.file_to_convert))

        """Sends Command to CMD"""
        command_to_send = ('pyuic5 -o {1} {0}').format(
                self.file_to_convert,
                file_name)
        p = Popen(command_to_send, cwd=self.pyuic_location)
        p.wait()

        """Moves newely created python script to the destination"""
        move(join(self.pyuic_location,
                  file_name),
             join(self.py_destination,
                  file_name))

        """Removes copied ui file from pyuic5.bat location"""
        remove(join(self.pyuic_location, self.file_to_convert))

        if (
                self.resource_location is not None
                or self.resource_location == ""):

            res_file_to_convert = self.resource_location.split('/')[-1]
            res_file_py_version = res_file_to_convert.replace(".qrc", ".py")
            resource_dest = "/".join(self.resource_location.split("/")[:-1])

#            """Copies Resource file into pyrcc5.bat location"""
#            copy(self.resource_location, join(
#                    self.pyuic_location,
#                    res_file_to_convert))

            """Generates the resource.py file"""
            command_to_send = ('pyrcc5 {0} -o {1}').format(
                    res_file_to_convert,
                    res_file_py_version)
            p = Popen(command_to_send, cwd=resource_dest)
            p.wait()

#            move(join(self.pyuic_location,
#                      res_file_py_version),
#                 join(self.py_destination,
#                      res_file_py_version))
#
#            remove(join(self.pyuic_location, res_file_py_version))
