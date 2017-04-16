from kivy.lang import Builder
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.colorpicker import ColorPicker

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
            size_hint: 1.0, 1.0

        Button:
            text: 'PICK AND CLOSE'
            color: 0.435, 0.725, 0.56, 1
            background_color: 0, 0.26, 0.27, 1
            size_hint: 1.0, 0.2
            on_press: popupcolor.on_press_dismiss()
''')


class PaintWindow(BoxLayout):
    pass


class PopupColor(Popup):
    def on_press_dismiss(self, *args):
        self.dismiss()
        return False


class PopupRun(App):
    def build(self):
        main_window = PaintWindow()
        popup = PopupColor()
        popup_color = ColorPicker()
        popup.open()

        def on_color(instance, value):
            print("RGBA = ", str(value))
            print("HSV = ", str(instance.hsv))
            print("HEX = ", str(instance.hex_color))
            hex_color = str(instance.hex_color)
            # Return hex color code without '#'
            return hex_color[1:]

        # Run function after change color in ColorPicker
        popup_color.bind(color=on_color)

        return main_window
