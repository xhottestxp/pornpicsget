class XHtml:
    """This class is a model to download a
    page from Pornpics in HTML.

    Author:
        xhottestxp
    """

    def __init__(self):
        """New Pornpics page html download.
        """
        self._urlink = ''
        self._path = ''
        self._ext = ''

    # getter and setter

    @property
    def urlink(self):
        return self._urlink

    @urlink.setter
    def urlink(self, urlink: urlink):
        self._urlink = urlink

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path: str):
        self._path = path
    
    @property
    def ext(self):
        return self._ext
    
    @ext.setter
    def ext(self, ext: str):
        self._ext = ext
