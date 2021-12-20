from xhtml.model.xhtml import XHtml
from xhtml.getporn.getporn import GetPorn
from tools.tools import checkurl, isafile
from core.singleton.smsg import SMsg as Msg


class ServiceXHtml:
    """Service XHtml to checks data from make
    download from a Pornpics page.

    Author:
        xhottestxp
    """

    def __init__(self):
        """New ServiceXHtml.
        """
        self._getporn = GetPorn()

    # getter method

    @property
    def getporn(self):
        return self._getporn

    # make download, return data correct

    def download_xhmtl(self, xhmtl: XHtml) -> bool:
        """This method makes download from a pornpics
        page html.

        Args:
            xhmtl (XHtml): model class for pornpics.

        Returns:
            bool: True if success.
        """
        # basic check - url check, pornpics url and path is file
        if not checkurl(urlink=xhmtl.urlink):
            Msg.msg().warning = True
            Msg.msg().title = 'Warning - URL problem'
            Msg.msg().message = 'Warning! Invalid URL'
            return False
        elif 'https://www.pornpics.com' not in xhmtl.path:
            Msg.msg().warning = True
            Msg.msg().title = 'Warning - Pornpics URL'
            Msg.msg().message = 'Warning! It\'s not Pornpics URL'
            return False
        elif not isafile(pathfile=xhtml.path):
            Msg.msg().warning = True
            Msg.msg().title = 'Warning - pornpics.html'
            Msg.msg().message = 'Warning! There\'s not file pornpics.html'
            return False
        return self.getporn.download_xhmtl(pornhtml=xhmtl)

    def select_xhtml(self, xhtml: XHtml) -> tuple:
        """This method get from XHtml page downloaded.

        Args:
            xhtml (XHtml): model to get html page.

        Returns:
            tuple: html page tuple data.
        """
        # photos
        photos = ()
        # basic check - path is file and not empty ext
        if not isafile(pathfile=xhtml.path):
            Msg.msg().warning = True
            Msg.msg().title = 'Warning - pornpics.html'
            Msg.msg().message = 'Warning! There\'s not file pornpics.html'
            return photos
        elif xhtml.ext.__len__() == 0:
            Msg.msg().warning = True
            Msg.msg().title = 'Warning - Extension'
            Msg.msg().message = 'Warning! Extension is empty'
            return photos
        # receive data
        photos = self.getporn.select_xhtml(pornhtml=xhtml)
        # check success or not
        if photos.__len__() == 0:
            Msg.msg().error = True
            Msg.msg().title = 'Error - Photos'
            Msg.msg().message = 'Error! Photos not found'
        # return tuple of photos
        return photos
