"""
This Module is in charge of executing CMD commands to create executable files
from the various inputs sent in by the Python_Toolbox GUI
"""
from subprocess import Popen
from os.path import join, isdir, isfile
from os.path import expanduser as exp
from os import remove

from shutil import copy, rmtree, move, copytree
#"""Sends Command to CMD"""
#command_to_send = ('pyuic5 -o {1} {0}').format(
#        self.file_to_convert,
#        file_name)
#p = Popen(command_to_send, cwd=self.pyuic_location)
#p.wait()