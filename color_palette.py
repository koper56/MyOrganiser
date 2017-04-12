from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.colorpicker import ColorPicker


class ColorScreen(Screen):
    def __init__(self, **kwargs):
        super(ColorScreen, self).__init__(**kwargs)
        self.name = "ColorScreen"
        self.color_picker = ColorPicker()
        self.add_widget(self.color_picker)

        # To monitor changes, we can bind to color property changes
        def on_color(instance, value):
            print("RGBA = ", str(value))  # or instance.color
            print("HSV = ", str(instance.hsv))
            print("HEX = ", str(instance.hex_color))

        self.color_picker.bind(color=on_color)


class ColorPalette(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(ColorScreen())

        return screen_manager


ColorPalette().run()