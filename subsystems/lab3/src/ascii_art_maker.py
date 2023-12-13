from ..config import *
from ..config import _

from share.config import Config

config = Config("data/lab3/config.json")

from .base_program import BaseProgram
from .validators.font import FontValidator
from .validators.color import ColorValidator

from consolemenu import *
from consolemenu.items import *
from consolemenu.prompt_utils import *

from art import *
from art.art_param import FONT_NAMES, DEFAULT_FONT

from pynput import keyboard
import threading

from termcolor import *
import msvcrt

import math
import os

import uuid

from share.menu import Menu, menu_item

class Art:
    def __init__(self, data, id = None, name = None) -> None:
        self.id = uuid.uuid4() if id == None else uuid.UUID(id) 
        self.name = self.id.hex if name == None else name
        self.data = data

class AsciiArtMaker(Menu):
    def __init__(self) -> None:
        super().__init__()
        logging.info("Initializing AsciiArtMaker")

        self.__default_font = DEFAULT_FONT
        self.__default_color = 'white'

        self.__font = self.__default_font
        self.__color = self.__default_color

        self.__arts = {}
        self.__save_folder = 'arts'
        self.__abs_save_path = os.path.join(abs_path, self.__save_folder)
        
        self.__load_arts()

    # WINDOWS ONLY
    @property
    def height(self):
        return os.get_terminal_size().lines
    @property 
    def width(self):
        return os.get_terminal_size().columns

    @menu_item(_("Show all arts"))
    def __show_arts(self):
        pu = PromptUtils(Screen())
        page_size = 2
        def split_page(elements, page, page_size):
            start_index = (page - 1) * page_size
            end_index = start_index + page_size
            return elements[start_index:end_index]
        
        arts_list = list(self.__arts.values())
        max_pages = math.ceil(len(arts_list) / page_size)

        def show_page(p):
            pu.clear()
            for idx, art in enumerate(split_page(arts_list, p, page_size)):
                pu.println(f'{(p - 1) * page_size + idx + 1} {art.id.hex}\n{art.data}')

        page = 1
        is_esc = False
        key_event = threading.Event()

        def on_press(key):
            nonlocal page
            nonlocal is_esc
            key_event.clear()

            if key == keyboard.Key.left:
                page -= 1 if page - 1 > 0 else 0
            elif key == keyboard.Key.right:
                page += 1 if page + 1 <= max_pages else 0
            elif key == keyboard.Key.esc:
                is_esc = True
                key_event.set()
                return False
            
            key_event.set()
        
        show_page(page)
        listener = keyboard.Listener(on_press)
        listener.start()
        
        while True:
            if is_esc:
                break

            key_event.wait()
            key_event.clear()
            
            show_page(page)

        listener.stop()

        logging.info("Showing all arts")

    def __save_art(self, art: Art) -> None:
        # path = os.path.join(self.__abs_save_path, self.__save_folder)
        if not os.path.isdir(self.__abs_save_path):
            os.mkdir(self.__abs_save_path)
        path_to_file = os.path.join(self.__abs_save_path, f'{art.name}.txt')
        if not os.path.exists(path_to_file):
            with open(path_to_file, 'w', encoding='utf-8') as file:
                file.write(art.data)
        logging.info("Saving art: %s", art.id)

    def __load_art(self, name) -> Art:
        art = Art(None, id=name)
        
        # path = os.path.join(self.__abs_save_path, self.__save_folder)
        if not os.path.isdir(self.__abs_save_path):
            os.mkdir(self.__abs_save_path)
        file_name = f'{name}.txt'
        if os.path.exists(os.path.join(self.__abs_save_path, file_name)):
            with open(os.path.join(self.__abs_save_path, file_name), 'r', encoding='utf-8') as file:
                art.data = file.read()
        logging.info("Loading art: %s", name)
        return art
    
    def __save_arts(self):
        for uuid in self.__arts:
            self.__save_art(self.__arts[uuid])

    def __load_arts(self):
        # path = os.path.join(self.__abs_save_path, self.__save_folder)
        if not os.path.isdir(self.__abs_save_path):
            os.mkdir(self.__abs_save_path)
        files = [f for f in os.listdir(self.__abs_save_path) if os.path.isfile(os.path.join(self.__abs_save_path, f))]
        for file in files:
            name = os.path.splitext(file)[0]
            self.__arts[name] = self.__load_art(name)
        logging.info("Loading arts from %s", self.__abs_save_path)

    @menu_item(_("Show all colors"))
    def __show_colors(self):
        pu = PromptUtils(Screen())
        for idx, color_name in enumerate(list(COLORS.keys())):
            pu.println(f'{idx} {colored(color_name, color_name)}')
        pu.enter_to_continue()

    @menu_item(_("Set color"))
    def __set_color(self):
        pu = PromptUtils(Screen())

        new_color = None
        while new_color == None:
            try:
                color_result = pu.input(_('Enter color name'), validators=[ColorValidator()], enable_quit=True)
                if not color_result[1]:
                    pu.println(_('Invalid color name, check all available colors in main menu'))
                    continue

                new_color = color_result[0]
                pu.println(_(f'Color "{new_color}" will look like'))
                pu.println(self.__text2art('Test', color=new_color))                
            except UserQuit:
                return
            
            if pu.prompt_for_yes_or_no(_('Do you agree?')):
                    self.__color = new_color
            else:
                new_color = None
                continue

    @menu_item(_("Set font"))
    def __set_font(self):
        pu = PromptUtils(Screen())
        new_font = None
        while new_font == None:
            try:
                font_name = pu.input(_('Enter font name'), validators=[FontValidator()], enable_quit=True)
                if not font_name[1]:
                    pu.println(_('Invalid font name, check all available fonts in main menu'))
                    continue
                
                new_font = font_name[0]
                pu.println(_(f'Font "{new_font}" will look like'))
                pu.println(text2art('Test', new_font))                
            
            except UserQuit:
                return
            
            if pu.prompt_for_yes_or_no(_('Do you agree?')):
                self.__font = new_font
            else:
                new_font = None
                continue

    @menu_item(_("Show fonts"))    
    def __show_fonts(self):
        pu = PromptUtils(Screen())
        page_size = 20
        def split_page(elements, page, page_size):
            start_index = (page - 1) * page_size
            end_index = start_index + page_size
            return elements[start_index:end_index]
        
        max_pages = math.ceil(len(FONT_NAMES) / page_size)

        def show_page(p):
            pu.clear()
            for idx, font in enumerate(split_page(FONT_NAMES, p, page_size)):
                pu.println(f'{(p - 1) * page_size + idx + 1} {font}')
                pu.println(text2art('Test', font))

        page = 1
        is_esc = False
        key_event = threading.Event()

        def on_press(key):
            nonlocal page
            nonlocal is_esc
            key_event.clear()

            if key == keyboard.Key.left:
                page -= 1 if page - 1 > 0 else 0
            elif key == keyboard.Key.right:
                page += 1 if page + 1 <= max_pages else 0
            elif key == keyboard.Key.esc:
                is_esc = True
                key_event.set()
                return False
            
            key_event.set()
        
        show_page(page)
        listener = keyboard.Listener(on_press)
        listener.start()

        while True:
            if is_esc:
                break

            key_event.wait()
            key_event.clear()

            show_page(page)

        listener.stop()

    def __text2art(self, text, font = None, color = None, no_color=False):
        logging.info("Converting text to ASCII art: '%s'", text)
        if no_color:
            return text2art(text, self.__font if font == None else font)
        else:
            return colored(text2art(text, self.__font if font == None else font), self.__color if color == None else color)

    @menu_item(_("Create ASCII art"))
    def __create_art(self) -> None:
        pu = PromptUtils(Screen())
        pu.println(_('Enter text'))

        while True:
            is_esc = False
            is_enter = False
            text = ''

            def is_fit(matrix: list[str]):
                if len(matrix) > self.height:
                    return False
                for line in matrix:
                    if len(line) > self.width:
                        return False
                return True

            def on_key_press(key):
                nonlocal text
                nonlocal is_esc
                nonlocal is_enter

                enable_write = True
            
                if key == keyboard.Key.esc or key == keyboard.Key.enter:
                    if key == keyboard.Key.esc:
                        is_esc = True
                    elif key == keyboard.Key.enter:
                        is_enter = True
                    return False
                elif key == keyboard.Key.backspace:
                    text = text[:-1]

                enable_write = is_fit(self.__text2art(text, no_color=True).splitlines())
                
                if enable_write:
                    if key == keyboard.Key.space:
                        text += ' '
                    elif isinstance(key, keyboard.KeyCode) == 1:
                        text += key.char
                
                enable_write = is_fit(self.__text2art(text, no_color=True).splitlines())

                if enable_write:
                    pu.clear()
                    pu.println(self.__text2art(text))
                
            
            with keyboard.Listener(on_key_press) as listener:
                listener.join()
            
            # ONLY WINDOWS
            while msvcrt.kbhit():
                msvcrt.getch()

            if is_esc:
                return

            if not pu.prompt_for_yes_or_no(_('Art are sutible?')):
                pu.clear()
                continue
            else:
                break
        
        ascii_art = self.__text2art(text)

        if pu.prompt_for_yes_or_no(_('Do you want to change color?')):
            pu.clear()
            ascii_art = self.__text2art(text, no_color=True)
            while True:
                available_colors = []
                color_list = list(COLORS.keys())
                for color in color_list:
                    available_colors.append(f'{color}\n{colored(ascii_art, color)}')
                color_index = pu.prompt_for_numbered_choice(available_colors, _('Choose color'))
                chosen_art = colored(ascii_art, color_list[color_index])
                pu.clear()
                pu.println(chosen_art)
                if not pu.prompt_for_yes_or_no(_('Color are sutible?')):
                    pu.clear()
                    continue
                else:
                    ascii_art = chosen_art
                    break
        
        pu.clear()
        pu.println(ascii_art)
        pu.enter_to_continue()

        art = Art(data=ascii_art)
        self.__arts[art.id] = art

    def run(self) -> None:
        self.menu.show()
        self.__save_arts()