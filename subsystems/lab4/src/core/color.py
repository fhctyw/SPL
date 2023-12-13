
class Color:
    color_dict = {
        "black": "\033[0;30m",
        "red": "\033[0;31m",
        "green": "\033[0;32m",
        "brown": "\033[0;33m",
        "blue": "\033[0;34m",
        "purple": "\033[0;35m",
        "cyan": "\033[0;36m",
        "light_gray": "\033[0;37m",
        "dark_gray": "\033[1;30m",
        "light_red": "\033[1;31m",
        "light_green": "\033[1;32m",
        "yellow": "\033[1;33m",
        "light_blue": "\033[1;34m",
        "light_purple": "\033[1;35m",
        "light_cyan": "\033[1;36m",
        "light_white": "\033[1;37m"
    }
    __end = "\033[0m"
    color_list = list(color_dict.keys())

    def __getitem__(self, key: str):
        return self.color_dict.get(key)
    
    def colored(string, color):
        return Color.color_dict[color] + string + Color.__end