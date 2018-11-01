"""
This Module is in charge of installing a passed in list packaged via
the pip method.
"""
from pip._internal import main
from os.path import join, expanduser


class PipInstaller():

    def __init__(self, enteredlist=None, remove=False, requirementlist=None):
        self.ent_list = enteredlist
        self.req_list = requirementlist
        self.remove = remove
        self.dir_ = join(expanduser("~"))

        self.InitInstall()

    def InitInstall(self):
        if self.remove is False:
            value = "install"
        else:
            value = "uninstall"

        if self.ent_list is not None:
            for item in self.ent_list:
                if value == "uninstall":
                    main([value, '--yes', item.strip()])
                else:
                    main([
                            value,
                            item.strip()])

        if self.req_list is not None and self.remove is False:
            with open(self.req_list, "r", encoding='utf-16') as file_:
                for line in file_.readlines():
                    main([value, line.strip().split("=")[0]])
