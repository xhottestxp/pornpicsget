from xhtml.model.xhtml import XHtml


class ServiceXHtml:
    """Service XHtml to checks data from make
    download from a Pornpics page.

    Author:
        xhottestxp
    """

    def __init__(self):
        """New ServiceXHtml.
        """
        pass

    def download_xhmtl(self, xhmtl: XHtml) -> bool:
        """This method makes download from a pornpics
        page html.

        Args:
            xhmtl (XHtml): model class for pornpics.

        Returns:
            bool: True if success.
        """
        pass

    def select_xhtml(self, xhtml: XHtml) -> tuple:
        """This method get from XHtml page downloaded.

        Args:
            xhtml (XHtml): model to get html page.

        Returns:
            tuple: html page tuple data.
        """
        pass
