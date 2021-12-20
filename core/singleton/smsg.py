from tools.msg import Msg


class SMsg:
    """Singleton pattern for Msg.

    Author:
        xhottestxp
    """

    _instance = None

    def __init__(self):
        """Singleton Msg.
        """
        pass

    @classmethod
    def msg(cls) -> Msg:
        """This method Msg return it instance.

        Returns:
            Msg: class instance.
        """
        if not cls._instance:
            cls._instance = Msg()
        return cls._instance
