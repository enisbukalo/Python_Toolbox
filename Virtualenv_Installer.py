"""
This Module will handle the creation of a virtual environment at
the given location with the given name.
"""
from subprocess import Popen


class VirtualenvInstaller():
    def __init__(self, dest, pysrc=None, name=None):
        self.destination = dest
        self.python = pysrc
        self.name = name

        self.InitCreation()

    def InitCreation(self):
        currwd = self.destination
        if self.python is None or self.python == "":
            command_to_send = ('virtualenv {0}').format(self.name)
        else:
            command_to_send = ('virtualenv --python={0} {1}').format(
                    self.python,
                    self.name)
        p = Popen(command_to_send, cwd=currwd)
        p.wait()
