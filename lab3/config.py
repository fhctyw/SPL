import gettext
import os.path

app_name = "ASCII Art Maker"
localization_name = 'ascii_art_maker'
abs_path = os.path.abspath(os.path.dirname(__file__))
localization_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'locale'))

gettext.bindtextdomain(localization_name, localization_folder)
gettext.textdomain(localization_name)
_ = gettext.gettext
