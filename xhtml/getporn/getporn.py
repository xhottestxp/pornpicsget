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
        self._title = ''

    # getter and setter

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title: str):
        self._title = title

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
        # checks if file empty
        with open(file=pornhtml.path, mode='r') as porn:
            if not porn.readline():
                return ()
        # generating data
        data = self._gettinglinks(
            self._improvedata, self._gettingdata, pornhtml)
        return (self.title,) + data

    # -------------------------------------------------------------

    def _gettingdata(self, pornhtml: Pornhtml) -> tuple:
        """This method takes data from pornpics.html

        Args:
            pornhtml (Pornhtml): instance.

        Returns:
            tuple: data getter.
        """
        with open(file=pornhtml.path, mode='r') as porn:
            data = porn.readlines()
            self.title = data[5].strip()[7:-8]
            data = (la for la in data if 'https://' in la)
            data = (la.strip() for la in data)
            data = (la for la in data if pornhtml.ext in la)
            data = [la.split() for la in data]
        # prevent to not have duplicate data
        del data[0]
        # returning tuple
        return tuple(data)

    def _improvedata(self, getdata: _gettingdata, *args):
        """This method can improve data to do something new.

        Args:
            getdata (_gettingdata): method _gettingdata
        """
        photos = ()
        data = getdata(args[0])
        # improving data
        for dat in data:
            for porn in dat:
                photos += (porn,) if 'https://' in porn else ()
        else:
            data = (porn for porn in photos if args[0].ext in porn)
            data = (tuple(porn.split('=')) for porn in data)
            data = tuple(porn[1][1:-1] for porn in data)
        # returning improved data
        return data

    def _gettinglinks(self, improve: _improvedata, *args) -> tuple:
        """This method gets the links to make download from pornpics.

        Args:
            improve (_improvedata): function.

        Returns:
            tuple: complete data links.
        """
        data = improve(args[0], args[1])
        try:
            porn = data.__len__()
            data = tuple(data[dat] for dat in range(0, porn, 2))
        except IndexError:
            pass
        finally:
            porn = dat = None
        # returning complete data
        return data
