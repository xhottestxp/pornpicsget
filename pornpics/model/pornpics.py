class Pornpics:
    """This Pornpics class is a model
    to make download from photos at Pornpics
    site.

    Author:
        xhottestxp
    """

    def __init__(self):
        """New Pornpics model photos download.
        """
        self._urlink = ''
        self._path = ''
        self._photos = tuple()

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
    def photos(self):
        return self._photos

    @photos.setter
    def photos(self, photos: tuple):
        self._photos = photos
