"""
This Module is in charge of executing CMD commands to create executable files
from the various inputs sent in by the Python_Toolbox GUI
"""
from subprocess import Popen


class PyInstaller():
    """
    This class will handl all aspects of this operation in order.
    """
    def __init__(self, pysrc, onefile=False, noconsole=False):
        self.py_location = pysrc
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
        if self.file is True and self.console is True:
            command_line = "pyinstaller {0} {1} --clean {2}".format(
                    "--onefile",
                    "--noconsole",
                    self.file_name)
        elif self.file is False and self.console is True:
            command_line = "pyinstaller {0} --clean {1}".format(
                    "--noconsole",
                    self.file_name)
        elif self.file is True and self.console is False:
            command_line = "pyinstaller {0} --clean {1}".format(
                    "--onefile",
                    self.file_name)
        elif self.file is False and self.console is False:
            command_line = "pyinstaller --clean {0}".format(
                    self.file_name)

        currwd = "/".join(self.py_location.split("/")[:-1])
        command_to_send = command_line
        p = Popen(command_to_send, cwd=currwd)
        p.wait()
