from xhtml.model.xhtml import XHtml
from xhtml.getporn.getporn import GetPorn


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
        #self.getporn.download_xhmtl(pornhtml=xhmtl)
        return True

    def select_xhtml(self, xhtml: XHtml) -> tuple:
        """This method get from XHtml page downloaded.

        Args:
            xhtml (XHtml): model to get html page.

        Returns:
            tuple: html page tuple data.
        """
        self.getporn.select_xhtml(pornhtml=xhtml)
