from os import mkdir
# local project modules
from core.singleton.smsg import SMsg as Msg
from pornpics.model.pornpics import Pornpics
from tools.tools import isdirectory, checkurl
from core.pornload.pornload import Pornload


class ServicePornpics:
    """Service Pornpics to download
    photos from pornpics page.

    Author:
        xhottestxp
    """

    def __init__(self):
        """New Service Pornpics.
        """
        self._pornland = Pornload()

    # getter

    @property
    def pornland(self):
        return self._pornland

    # try make download

    def download_pornpics(self, pornpics: Pornpics) -> bool:
        """This method checks and try to make download from files
        and returns boolean types.

        Args:
            pornpics (Pornpics): model Pornpics.

        Returns:
            bool: True if success.
        """
        if not isdirectory(pathdir=pornpics.path):
            # invalid directory - return False
            Msg.msg().warning = True
            Msg.msg().title = 'Warning - Path'
            Msg.msg().message = 'Warning! This path is invalid'
            return False
        for data in pornpics.photos[1:]:
            # checks if there's a invalid imagem url link
            if not checkurl(urlink=data):
                Msg.msg().warning = True
                Msg.msg().title = 'Warning - URL problem'
                Msg.msg().message = 'Warning! This URL is invalid'
                return False
        if pornpics.photos[0].__len__() > 0:
            # creating a new folder with name got from pornpics.com
            pornpics.path += f'/{pornpics.photos[0]}'
            mkdir(pornpics.path)
        # taking the first element - name folder new
        pornpics.photos = pornpics.photos[1:]
        # trying to make download
        if self.pornland.download_pornpics(pornpics=pornpics):
            Msg.msg().info = True
            Msg.msg().title = 'Success - Download'
            Msg.msg().message = 'Success! All photos were downloaded'
            return True
        else:
            Msg.msg().error = True
            Msg.msg().title = 'Error - Download'
            Msg.msg().message = 'Error! Invalid download'
            return False
