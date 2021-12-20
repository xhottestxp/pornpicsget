class Msg:
    """This class is a Msg for created message
    for inform to user.

    Author:
        xhottestxp
    """

    def __init__(self):
        """New Message
        """
        self._message = ''
        self._title = ''
        self._warning = False
        self._info = False
        self._error = False

    # getter and setter

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message: str):
        self._message = message

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title: str):
        self._title = title

    @property
    def warning(self):
        return self._warning

    @warning.setter
    def warning(self, warning: bool):
        self._error = False
        self._info = False
        self._warning = warning

    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, info: bool):
        self._error = False
        self._warning = False
        self._info = info

    @property
    def error(self):
        return self._error

    @error.setter
    def error(self, error: bool):
        self._warning = False
        self._info = False
        self._error = error
