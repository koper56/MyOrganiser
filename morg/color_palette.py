import time
import logging

from kivy.lang import Builder
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.colorpicker import ColorPicker

from morg import LOG_FILE_PATH

# Take time and store in format day_month_year - 09_05_2017
time_format = time.strftime("%Y_%m_%d")

# Create specific logger different than Kivy logger
logger = logging.getLogger(__name__)

# Set level of logger
logger.setLevel(logging.INFO)

# Logging info format f.ex.
# "[2017-05-09 15:33:58,217]	data_base_test_log.py	message"
format_of_logger = logging.Formatter('[%(asctime)s]\t%(pathname)s\t%(message)s')

# Create file with logging info f.ex. "morg_09_05_2017.log"
file_handler = logging.FileHandler(LOG_FILE_PATH)
file_handler.setFormatter(format_of_logger)
logger.addHandler(file_handler)

Builder.load_string('''
<PaintWindow>:
    orientation: 'vertical'

<PopupColor>:
    title: 'Pick a Color'
    size_hint: 1.0, 0.6
    id: popupcolor

    BoxLayout:
        orientation: 'vertical'

        ColorPicker:
            id: colorpicker
            size_hint: 1.0, 1.0

        Button:
            text: 'PICK AND CLOSE'
            color: 0.435, 0.725, 0.56, 1
            background_color: 0, 0.26, 0.27, 1
            size_hint: 1.0, 0.2
            on_press: popupcolor.on_press_dismiss(colorpicker)
''')


class PaintWindow(BoxLayout):
    pass


class PopupColor(Popup):
    def on_press_dismiss(self, colorpicker, *args):
        self.dismiss()
        # Take hex color code without #
        hex_color = str(colorpicker.hex_color)[1:]
        logger.info('Picked color HEX code: #{}'.format(hex_color))

        return hex_color


class PopupRunColorPalette(App):
    def build(self):
        main_window = PaintWindow()
        popup = PopupColor()
        popup.open()

        return main_window
