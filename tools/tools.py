"""This module has functions to auxiliary content control.

    Author:
        xhottestxp
    """


from pathlib import Path


def pathtofile(file='', dire='', back=0) -> str:
    """This method is for generate a path to a file.

    Args:
        file (str, optional): name file to use. Defaults to ''.
        dire (str, optional): directory where file must have. Defaults to ''.
        back (int, optional): how many dirs to come back. Defaults to 0.

    Returns:
        str: path to file and file.
    """
    path = Path(__file__).parent.absolute().__str__()
    path = [bk for bk in path]
    for bk in range(back):
        path.reverse()
        path = path[path.index('/')+1:]
        path.reverse()
    else:
        path = ''.join(i for i in path)
        path += '/' if path[-1] != '/' else ''
        path += f'{dire}/' if dire else ''
        path += file if file else ''
    return path


def configtext() -> tuple:
    """This function returns a tuple with
    data to insert into config file by default.

    Returns:
        tuple: with default data.
    """
    textconfig = (40 * '-' + '\n',)
    textconfig += ('PornPics Configuration File -> Theme\n',)
    textconfig += (textconfig[0],)
    textconfig += ('Here are the variables boolean for each\n',)
    textconfig += ('theme, by default it\'s -> light=True\n',)
    textconfig += (textconfig[0],)
    textconfig += ('light=True\n',)
    textconfig += ('dark=False\n',)
    textconfig += (textconfig[0],)
    return textconfig