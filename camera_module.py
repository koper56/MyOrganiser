from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from kivy.app import App
from kivy.lang import Builder
import time

# Camera module for History/Sets

Builder.load_string('''
<ConfirmPopup>:
    cols:1
	Label:
		text: root.text
	GridLayout:
		cols: 1
		size_hint_y: None
		height: '44sp'
    Camera:
        id: camera
        play: True
        resolution: (600, 600)
		Button:
			text: 'TAKE PHOTO'
			color: 0.435, 0.725, 0.56, 1
            background_color: 0, 0.26, 0.27, 1
            size_hint_y: None
            height: '50dp'
            pos: 500, 500
			on_press: root.take_photo()
			on_release: root.dispatch('on_answer')
''')


class ConfirmPopup(GridLayout):
    text = StringProperty()

    def __init__(self, **kwargs):
        self.register_event_type('on_answer')
        super(ConfirmPopup, self).__init__(**kwargs)

    def on_answer(self, *args):
        pass

    # Function to capture the images and give them the names
    # according to their captured date F. ex 'Captured as IMG_2017_04_05.png'.
    # Store photos in /sets directory
    def take_photo(self):
        camera = self.ids['camera']
        time_format = time.strftime("%d_%m_%Y")
        camera.export_to_png("sets/Set_from_{}.png".format(time_format))
        print("Captured as 'Set_from_{}.png'".format(time_format))


class PopupRun(App):
    def build(self):
        content = ConfirmPopup()
        content.bind(on_answer=self._on_answer)
        self.popup = Popup(title="Camera module for sets",
                           content=content,
                           size_hint=(None, None),
                           size=(600, 600),
                           auto_dismiss=False)
        self.popup.open()

    def _on_answer(self, instance):
        self.popup.dismiss()