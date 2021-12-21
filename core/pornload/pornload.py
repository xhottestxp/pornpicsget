from requests import get as getpage, codes
# getting model for download
from pornpics.model.pornpics import Pornpics
from tools.tools import getnameurl


class Pornload:
    """This class is responsible to download all 
    photos from a pornpics page.

    Author:
        xhottestxp
    """

    def __init__(self):
        """New pornpics image download.
        """
        pass

    def download_pornpics(self, pornpics: Pornpics) -> bool:
        """This method checks and try to make download from files
        and returns boolean types.

        Args:
            pornpics (Pornpics): model Pornpics.

        Returns:
            bool: True if success.
        """
        for porn in pornpics.photos:
            if not self._downloaderfile(urlink=porn, pathfile=pornpics.path):
                return False
        else:
            return True

    def _downloaderfile(self, urlink: str, pathfile: str) -> bool:
        """This method is the downloader from pornpics photos
        sent up to here.

        Args:
            urlink (str): photo url.
            pathfile (str): path and file name.

        Returns:
            bool: True if success.
        """
        filepath = f'{pathfile}/{getnameurl(urlink=urlink)}'
        # download part
        answer = getpage(url=urlink, stream=True)
        if answer.status_code == codes.OK:
            with open(file=filepath, mode='wb') as varg:
                for bits in answer.iter_content(chunk_size=256):
                    varg.write(bits)
                else:
                    return True
        else:
            return False
