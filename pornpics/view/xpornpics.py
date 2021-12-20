from os.path import expanduser, isdir
from clipboard import paste
from tkinter import Entry, Button, Checkbutton, NORMAL, DISABLED
from tkinter import Tk, Frame, Label, PhotoImage, BooleanVar
from tkinter.constants import LEFT
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showerror as error
from tkinter.messagebox import showinfo as info
from tkinter.messagebox import showwarning as warning
# local modules
from tools.tools import pathtofile, configtext
from core.singleton.sfacade import SFacade
from core.singleton.smsg import SMsg
from pornpics.model.pornpics import Pornpics


class XPornPics:
    """Project GUI - Pornpics images download.

    Author:
        xhottestxp
    """

    # constants
    BLACK = '#2d2d2d'
    PINK = '#eb008b'
    WHITE = '#ffffff'
    # fonts
    FSmall = ('Ubuntu', 12)
    FMedium = ('Ubuntu', 14)
    FLarge = ('Ubuntu', 18, 'bold')
    # config file - config.porn
    CONFIG = pathtofile(back=1, file='config.porn')
    # logo file
    LOGO = (pathtofile(back=1, dire='img', file='pornpics-light.png'),
            pathtofile(back=1, dire='img', file='pornpics-dark.png'))
    # pornpics.html path
    PORNHTML = pathtofile(back=1, dire='pages', file='pornpics.html')

    def __init__(self):
        """New GUI Pornpics
        """
        # creating window
        self.window = Tk()
        self.window.minsize(720, 520)
        self.window.title('Pornpics Download')
        # frame theme
        self.frame_theme = Frame(self.window)
        self.frame_theme.pack(pady=4)
        # check light
        self._boollight = BooleanVar()
        self.check_light = Checkbutton(self.frame_theme, var=self._boollight)
        self.check_light['font'] = self.FMedium
        self.check_light['text'] = 'Light'
        self.check_light['width'] = 7
        self.check_light['command'] = self.select_light
        self.check_light.pack(side=LEFT)
        # check dark
        self._booldark = BooleanVar()
        self.check_dark = Checkbutton(self.frame_theme, var=self._booldark)
        self.check_dark['font'] = self.FMedium
        self.check_dark['text'] = 'Dark'
        self.check_dark['width'] = 7
        self.check_dark['command'] = self.select_dark
        self.check_dark.pack(side=LEFT)
        # frame title
        self.frame_title = Frame(self.window)
        self.frame_title.pack(pady=4)
        # label title
        self.label_title = Label(self.frame_title)
        self.label_title['font'] = self.FLarge
        self.label_title['text'] = 10 * '\\' + \
            '  PORNPICS DOWNLOADER  ' + 10 * '/'
        self.label_title.pack()
        # frane logo pornpics
        self.frame_logo = Frame(self.window)
        self.frame_logo.pack(pady=4)
        # label logo
        # !!!!!!!!!!!!!!!! Photo Logo
        self.logo_dark = PhotoImage(file=self.LOGO[0])
        self.logo_light = PhotoImage(file=self.LOGO[1])
        # !!!!!!!!!!!!!!!! Photo Logo
        self.label_logo = Label(self.frame_logo)
        self.label_logo.pack()
        # frame url
        self.frame_url = Frame(self.window)
        self.frame_url.pack(pady=4)
        # label url
        self.label_url = Label(self.frame_url)
        self.label_url['font'] = self.FMedium
        self.label_url['text'] = 'Pornpics URL for download *'
        self.label_url.pack()
        # entry url
        self.entry_url = Entry(self.frame_url)
        self.entry_url['font'] = self.FSmall
        self.entry_url['width'] = 62
        self.entry_url['bd'] = 0
        self.entry_url.bind('<Button-1>', self.clearurl)
        self.entry_url.pack(side=LEFT)
        # button url paste
        self.button_url = Button(self.frame_url)
        self.button_url['bd'] = 0
        self.button_url['pady'] = 0
        self.button_url['font'] = self.FSmall
        self.button_url['text'] = 'Paste'
        self.button_url['width'] = 6
        self.button_url.bind('<Button-1>', self.action_press_url)
        self.button_url.pack(side=LEFT)
        # frame path select
        self.frame_path = Frame(self.window)
        self.frame_path.pack(pady=4)
        # label path select
        self.label_path = Label(self.frame_path)
        self.label_path['font'] = self.FMedium
        self.label_path['text'] = 'Select Saving Directory *'
        self.label_path.pack()
        # entry path select
        self.entry_path = Entry(self.frame_path)
        self.entry_path['font'] = self.FSmall
        self.entry_path['width'] = 62
        self.entry_path['bd'] = 0
        self.entry_path.pack(side=LEFT)
        # button path select
        self.button_path = Button(self.frame_path)
        self.button_path['bd'] = 0
        self.button_path['pady'] = 0
        self.button_path['font'] = self.FSmall
        self.button_path['text'] = 'Select'
        self.button_path['width'] = 6
        self.button_path.bind('<Button-1>', self.action_press_select)
        self.button_path.pack(side=LEFT)
        # frame param
        self.frame_param = Frame(self.window)
        self.frame_param.pack(pady=8)
        # label param
        self.label_param = Label(self.frame_param)
        self.label_param['font'] = self.FMedium
        self.label_param['text'] = 'Extension* '
        self.label_param.pack(side=LEFT)
        # check jpg
        self._booljpg = BooleanVar()
        self.check_jpg = Checkbutton(self.frame_param, var=self._booljpg)
        self.check_jpg['font'] = self.FMedium
        self.check_jpg['text'] = '.jpg'
        self.check_jpg['width'] = 7
        self._booljpg.set(True)
        self.check_jpg['command'] = self.select_jpg
        self.check_jpg.pack(side=LEFT)
        # check gif
        self._boolgif = BooleanVar()
        self.check_gif = Checkbutton(self.frame_param, var=self._boolgif)
        self.check_gif['font'] = self.FMedium
        self.check_gif['text'] = '.gif'
        self.check_gif['width'] = 7
        self.check_gif['command'] = self.select_gif
        self.check_gif.pack(side=LEFT)
        # check png
        self._boolpng = BooleanVar()
        self.check_png = Checkbutton(self.frame_param, var=self._boolpng)
        self.check_png['font'] = self.FMedium
        self.check_png['text'] = '.jpg'
        self.check_png['width'] = 7
        self.check_png['command'] = self.select_png
        self.check_png.pack(side=LEFT)
        # check othe
        self._boolother = BooleanVar()
        self.check_other = Checkbutton(self.frame_param, var=self._boolother)
        self.check_other['font'] = self.FMedium
        self.check_other['text'] = 'other'
        self.check_other['width'] = 7
        self.check_other['command'] = self.select_other
        self.check_other.pack(side=LEFT)
        # entry other
        self.entry_other = Entry(self.frame_param)
        self.entry_other['font'] = self.FSmall
        self.entry_other['width'] = 10
        self.entry_other['bd'] = 0
        self.entry_other['state'] = DISABLED
        self.entry_other.pack(side=LEFT)
        # frame button download
        self.frame_download = Frame(self.window)
        self.frame_download.pack(pady=32)
        # button download
        self.button_download = Button(self.frame_download)
        self.button_download['bd'] = 0
        self.button_download['pady'] = 5
        self.button_download['font'] = self.FSmall
        self.button_download['text'] = 'Download'
        self.button_download['width'] = 15
        self.button_download.bind('<Button>', self.makedownload)
        self.button_download.pack(side=LEFT)
        # config file
        self.setorgetconfig()
        # showing window
        self.window.mainloop()

    # --------------------------------------------------------------------------

    # change theme

    def select_light(self):
        """Select Light theme.
        """
        self._booldark.set(value=False)
        self._boollight.set(value=True)
        with open(file=self.CONFIG, mode='r') as porn:
            data = porn.readlines()
        data[6:8] = ('light=True\n', 'dark=False\n')
        with open(file=self.CONFIG, mode='w') as porn:
            porn.writelines(data)
        # setting theme
        self.theme_switch()

    def select_dark(self):
        """Select Dark theme.
        """
        self._boollight.set(value=False)
        self._booldark.set(value=True)
        with open(file=self.CONFIG, mode='r') as porn:
            data = porn.readlines()
        data[6:8] = ('light=False\n', 'dark=True\n')
        with open(file=self.CONFIG, mode='w') as porn:
            porn.writelines(data)
        # setting theme
        self.theme_switch()

    def theme_switch(self):
        """This method can switch between themes.
        """
        # window
        self.window['bg'] = self.backgroundcolor()
        # frame title
        self.frame_theme['bg'] = self.backgroundcolor()
        # check light
        self.check_light['bg'] = self.backgroundcolor()
        self.check_light['fg'] = self.foregroundcolor()
        self.check_light['activebackground'] = self.backgroundcolor()
        self.check_light['activeforeground'] = self.foregroundcolor()
        self.check_light['selectcolor'] = self.foregroundcolor(pink=True)
        self.check_light['highlightbackground'] = self.backgroundcolor()
        # check dark
        self.check_dark['bg'] = self.backgroundcolor()
        self.check_dark['fg'] = self.foregroundcolor()
        self.check_dark['activebackground'] = self.backgroundcolor()
        self.check_dark['activeforeground'] = self.foregroundcolor()
        self.check_dark['selectcolor'] = self.foregroundcolor(pink=True)
        self.check_dark['highlightbackground'] = self.backgroundcolor()
        # frame title
        self.frame_title['bg'] = self.backgroundcolor()
        # label title
        self.label_title['bg'] = self.backgroundcolor()
        self.label_title['fg'] = self.foregroundcolor()
        # frame logo
        self.frame_logo['bg'] = self.backgroundcolor()
        # label logo
        self.label_logo['bg'] = self.backgroundcolor()
        self.label_logo['image'] = self.logo_light if self._boollight.get(
        ) else self.logo_dark
        # frame url
        self.frame_url['bg'] = self.backgroundcolor()
        # label url
        self.label_url['bg'] = self.backgroundcolor()
        self.label_url['fg'] = self.foregroundcolor()
        # entry url
        self.entry_url['bg'] = self.foregroundcolor()
        self.entry_url['fg'] = self.backgroundcolor()
        self.entry_url['selectbackground'] = self.foregroundcolor(pink=True)
        self.entry_url['selectforeground'] = self.foregroundcolor()
        # button url
        self.button_url['bg'] = self.foregroundcolor(pink=True)
        self.button_url['fg'] = self.backgroundcolor()
        self.button_url['activebackground'] = self.foregroundcolor()
        self.button_url['activeforeground'] = self.backgroundcolor()
        self.button_url['highlightbackground'] = self.foregroundcolor(
            pink=True)
        # frame path
        self.frame_path['bg'] = self.backgroundcolor()
        # label path
        self.label_path['bg'] = self.backgroundcolor()
        self.label_path['fg'] = self.foregroundcolor()
        # entry path
        self.entry_path['bg'] = self.foregroundcolor()
        self.entry_path['fg'] = self.backgroundcolor()
        self.entry_path['selectbackground'] = self.foregroundcolor(pink=True)
        self.entry_path['selectforeground'] = self.foregroundcolor()
        # button path
        self.button_path['bg'] = self.foregroundcolor(pink=True)
        self.button_path['fg'] = self.backgroundcolor()
        self.button_path['activebackground'] = self.foregroundcolor()
        self.button_path['activeforeground'] = self.backgroundcolor()
        self.button_path['highlightbackground'] = self.foregroundcolor(
            pink=True)
        # frame param
        self.frame_param['bg'] = self.backgroundcolor()
        # label param
        self.label_param['bg'] = self.backgroundcolor()
        self.label_param['fg'] = self.foregroundcolor()
        # check jpg
        self.check_jpg['bg'] = self.backgroundcolor()
        self.check_jpg['fg'] = self.foregroundcolor()
        self.check_jpg['activebackground'] = self.backgroundcolor()
        self.check_jpg['activeforeground'] = self.foregroundcolor()
        self.check_jpg['selectcolor'] = self.foregroundcolor(pink=True)
        self.check_jpg['highlightbackground'] = self.backgroundcolor()
        # check gif
        self.check_gif['bg'] = self.backgroundcolor()
        self.check_gif['fg'] = self.foregroundcolor()
        self.check_gif['activebackground'] = self.backgroundcolor()
        self.check_gif['activeforeground'] = self.foregroundcolor()
        self.check_gif['selectcolor'] = self.foregroundcolor(pink=True)
        self.check_gif['highlightbackground'] = self.backgroundcolor()
        # check png
        self.check_png['bg'] = self.backgroundcolor()
        self.check_png['fg'] = self.foregroundcolor()
        self.check_png['activebackground'] = self.backgroundcolor()
        self.check_png['activeforeground'] = self.foregroundcolor()
        self.check_png['selectcolor'] = self.foregroundcolor(pink=True)
        self.check_png['highlightbackground'] = self.backgroundcolor()
        # check other
        self.check_other['bg'] = self.backgroundcolor()
        self.check_other['fg'] = self.foregroundcolor()
        self.check_other['activebackground'] = self.backgroundcolor()
        self.check_other['activeforeground'] = self.foregroundcolor()
        self.check_other['selectcolor'] = self.foregroundcolor(pink=True)
        self.check_other['highlightbackground'] = self.backgroundcolor()
        # entry other
        self.entry_other['bg'] = self.foregroundcolor()
        self.entry_other['fg'] = self.backgroundcolor()
        self.entry_other['disabledbackground'] = self.foregroundcolor(
            pink=True)
        self.entry_other['highlightbackground'] = self.foregroundcolor(
            pink=True)
        self.entry_other['selectbackground'] = self.foregroundcolor(pink=True)
        self.entry_other['selectforeground'] = self.foregroundcolor()
        # frame download
        self.frame_download['bg'] = self.backgroundcolor()
        # button download
        self.button_download['bg'] = self.foregroundcolor(pink=True)
        self.button_download['fg'] = self.backgroundcolor()
        self.button_download['activebackground'] = self.foregroundcolor()
        self.button_download['activeforeground'] = self.backgroundcolor()
        self.button_download['highlightbackground'] = self.foregroundcolor(
            pink=True)

    def backgroundcolor(self):
        """Select background color.

        Returns:
            str: color hex.
        """
        return self.WHITE if self._boollight.get() else self.BLACK

    def foregroundcolor(self, pink=False):
        """Select foreground color.

        Args:
            pink (bool, optional): if font color is pink. Defaults to False.

        Returns:
            str: color hex.
        """
        return self.PINK if pink else self.BLACK if self._boollight.get() else self.WHITE

    # --------------------------------------------------------------------------
    
    # cleans url entry
    
    def clearurl(self, evt):
        """This method can cleans entry url.

        Args:
            evt (<Button-1>): left button click event
        """
        self.entry_url.delete(0, 'end')
    
    # --------------------------------------------------------------------------
    
    # paste and select buttons events

    def action_press_url(self, evt):
        """This method represents the act to paste content at entry url.

        Args:
            evt (Mouse Event): <Button-1>
        """
        self.entry_url.delete(0, 'end')
        self.entry_url.insert(0, paste())

    def action_press_select(self, evt):
        """This method represents the act to paste content at entry path.

        Args:
            evt (Mouse Event): <Button-1>
        """
        direct = ()
        if isdir(self.entry_path.get()):
            direct += (self.entry_path.get(),)
        else:
            direct += (expanduser('~'),)
        direct += (askdirectory(initialdir=direct),)
        self.entry_path.delete(0, 'end')
        self.entry_path.insert(0, direct[1] if direct[1] else direct[0])

    # --------------------------------------------------------------------------
    
    # param checkbuttons command
    
    def select_jpg(self):
        """Select jpg.
        """
        self._boolgif.set(False)
        self._boolpng.set(False)
        self._boolother.set(False)
        self.entry_other['state'] = DISABLED
        self._booljpg.set(True)
    
    def select_gif(self):
        """Select gif.
        """
        self._booljpg.set(False)
        self._boolpng.set(False)
        self._boolother.set(False)
        self.entry_other['state'] = DISABLED
        self._boolgif.set(True)
    
    def select_png(self):
        """Select png.
        """
        self._booljpg.set(False)
        self._boolgif.set(False)
        self._boolother.set(False)
        self.entry_other['state'] = DISABLED
        self._boolpng.set(True)
    
    def select_other(self):
        """Select png.
        """
        self._booljpg.set(False)
        self._boolgif.set(False)
        self._boolpng.set(False)
        self._boolother.set(True)
        self.entry_other['state'] = NORMAL
        self.entry_other.focus()
    
    # --------------------------------------------------------------------------
    
    # download button event
    
    def makedownload(self, evt):
        """This method is responsible to try to make download from photos
        inside pornpics url.

        Args:
            evt (<Button-1>): left button mouse.
        """
        pass
    
    # --------------------------------------------------------------------------

    # file with configuration

    def setorgetconfig(self):
        """This method create or load a configuration file.
        """
        try:
            with open(file=self.CONFIG, mode='r') as porn:
                data = (i for i in porn.readlines()[6:8])
                data = tuple(i for i in data if 'True' in i)[0][:-1]
                if 'light' in data:
                    self.select_light()
                elif 'dark' in data:
                    self.select_dark()
        except FileNotFoundError:
            with open(file=self.CONFIG, mode='w') as porn:
                porn.writelines(configtext())
                self.select_light()
