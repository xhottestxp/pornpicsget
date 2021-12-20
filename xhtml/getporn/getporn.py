from requests import get as getpage, codes
from xhtml.model.xhtml import XHtml as Pornhtml


class GetPorn:
    """This class is to make download from a html page file.
    It's for pornpics.com/
    
    Author:
        xhottestxp
    """
    
    def __init__(self):
        """New PornPics hmtl download.
        """
        pass
    
    # make download, return data correct
    
    def download_xhmtl(self, pornhtml: Pornhtml) -> bool:
        """This method makes download from a pornpics
        page html.

        Args:
            xhmtl (XHtml): model class for pornpics.

        Returns:
            bool: True if success.
        """
        answer = getpage(url=pornhtml.urlink, stream=True)
        answer.encoding = 'utf-8'
        if answer.status_code == codes.OK:
            with open(pornhtml.path, 'w') as new:
                for line in answer.content.decode('utf-8'):
                    new.write(line)
                else:
                    return True
        else:
            return False

    def select_xhtml(self, pornhtml: Pornhtml) -> tuple:
        """This method get from XHtml page downloaded.

        Args:
            xhtml (XHtml): model to get html page.

        Returns:
            tuple: html page tuple data.
        """
        pass