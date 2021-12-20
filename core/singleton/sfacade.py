from core.facade.facade import Facade


class SFacade:
    """This method is a singleton pattern for
    Facade class.

    Author:
        xhottestxp
    """

    _instance = None

    def __init__(self):
        """Singleton Facade.
        """
        pass

    @classmethod
    def facade(cls) -> Facade:
        """New or existing instance from Facade.

        Returns:
            Facade: class instance.
        """
        if not cls._instance:
            cls._instance = Facade()
        return cls._instance
