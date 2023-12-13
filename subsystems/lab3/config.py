import gettext
import os.path
import logging

app_name = "ASCII Art Maker"
localization_name = 'ascii_art_maker'
abs_path = os.path.abspath(os.path.dirname(__file__))
localization_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'locale'))

logging.info("Setting up localization for %s. Absolute path: %s. Localization folder: %s", app_name, abs_path, localization_folder)

gettext.bindtextdomain(localization_name, localization_folder)
gettext.textdomain(localization_name)
_ = gettext.gettext

logging.info("Localization for %s is set up successfully", app_name)
