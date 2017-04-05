# basic code from https://github.com/kivy/kivy/blob/master/examples/camera/main.py

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
import time
Builder.load_string('''
<CameraClick>:
    Camera:
        id: camera
        resolution: (640, 480)
        play: False
    ToggleButton:
        text: 'Turn on/off camera'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '50dp'
        pos: 0, 100
    Button:
        text: 'Take photo'
        size_hint_y: None
        height: '50dp'
        pos: 0, 150
        on_press: root.take_photo()
        on_press: app.stop()
''')


class CameraClick(FloatLayout):
    # Function to capture the images and give them the names
    # according to their captured date F. ex 'Captured as IMG_2017_04_05.png'.
    def take_photo(self):
        camera = self.ids['camera']
        time_format = time.strftime("%Y_%m_%d")
        camera.export_to_png("Set_from_{}.png".format(time_format))
        print("Captured as IMG_{}.png".format(time_format))


class CameraModule(App):
    def build(self):
        return CameraClick()
