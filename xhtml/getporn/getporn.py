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
            with open(pornhtml.path, 'w') as porn:
                for line in answer.content.decode('utf-8'):
                    porn.write(line)
                else:
                    return True
        else:
            return False

    def select_xhtml(self, pornhtml: Pornhtml) -> 'generator':
        """This method get from XHtml page downloaded.

        Args:
            xhtml (XHtml): model to get html page.

        Returns:
            generator: html page generator data.
        """
        # checks if file exists
        try:
            porn = open(pornhtml.path, 'r')
        except FileNotFoundError:
            return ()
        finally:
            porn.close()
        # getting data from file
        with open(file=pornhtml.path, mode='r') as porn:
            data = porn.readlines()
            title = data[5].strip()[7:-8]
            data = (la for la in data if 'https://' in la)
            data = (la.strip() for la in data)
            data = (la for la in data if pornhtml.ext in la)
            data = [la.split() for la in data]
        photos = ()
        # improving data
        for dat in data:
            for porn in dat:
                photos += (porn,) if 'https://' in porn else ()
        else:
            data = (porn for porn in photos if pornhtml.ext in porn)
            data = (tuple(porn.split('=')) for porn in data)
            data = (porn[1][1:-1] for porn in data)
            data = tuple(porn for porn in data)[1:]
        # getting the best and becoming a generator
        try:
            porn = data.__len__()
            data = tuple(data[dat] for dat in range(0, porn, 2))
        except IndexError:
            pass
        finally:
            porn = photos = dat = None
            return data
