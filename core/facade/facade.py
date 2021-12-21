from xhtml.model.xhtml import XHtml
from pornpics.model.pornpics import Pornpics
from xhtml.service.servicexhtml import ServiceXHtml
from pornpics.service.servicepornpics import ServicePornpics


class Facade:
    """This class a project facade to communicate with backend.
    Facade.

    Author:
        xhottestxp
    """

    _svxhtml = ServiceXHtml()
    _svpornpics = ServicePornpics()

    def __init__(self):
        """New Facade.
        """
        pass

    # service xhtml

    def download_xhtml(self, xhtml: XHtml) -> bool:
        """This method makes download from a pornpics
        page html.

        Args:
            xhtml (XHtml): model class for pornpics.

        Returns:
            bool: True if success.
        """
        return self._svxhtml.download_xhtml(xhtml=xhtml)

    def select_xhtml(self, xhtml: XHtml) -> tuple:
        """This method get from XHtml page downloaded.

        Args:
            xhtml (XHtml): model to get html page.

        Returns:
            tuple: html page tuple data.
        """
        return self._svxhtml.select_xhtml(xhtml=xhtml)

    # service pornpics

    def download_pornpics(self, pornpics: Pornpics) -> bool:
        """This method checks and try to make download from files
        and returns boolean types.

        Args:
            pornpics (Pornpics): model Pornpics.

        Returns:
            bool: True if success.
        """
        return self._svpornpics.download_pornpics(pornpics=pornpics)
