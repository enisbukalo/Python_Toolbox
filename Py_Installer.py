"""
This Module is in charge of executing CMD commands to create executable files
from the various inputs sent in by the Python_Toolbox GUI
"""
from subprocess import Popen, PIPE, STDOUT
from os.path import join
from os.path import expanduser as exp


class PyInstaller():
    """
    This class will handl all aspects of this operation in order.
    """
    def __init__(self, pysrc, exedst, onefile=False, noconsole=False):
        self.py_location = pysrc
        self.exe_destination = exedst
        self.file = onefile
        self.console = noconsole
        self.file_name = self.py_location.split("/")[-1]

        self.CallCommandLine()

    def CallCommandLine(self):
        """
        This function will pull open a command line in windows.
        Then it will execute the pyinstaller function.
        """
        command_line = "pyinstaller "
        if self.file is True and self.noconsole is True:
            command_line = "pyinstaller {0} {1} --cleanup {2}".format(
                    "--onefile",
                    "--noconsole",
                    self.file_name)
        elif self.file is False and self.noconsole is True:
            command_line = "pyinstaller {0} --cleanup {1}".format(
                    "--noconsole",
                    self.file_name)
        elif self.file is True and self.noconsole is False:
            command_line = "pyinstaller {0} --cleanup {1}".format(
                    "--onefile",
                    self.file_name)
        elif self.file is False and self.noconsole is False:
            command_line = "pyinstaller --cleanup {1}".format(
                    self.file_name)
        print(command_line)
