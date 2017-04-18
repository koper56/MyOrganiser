from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from kivy.app import App
from kivy.lang import Builder
from data_base import next_id_value

# Camera module for Add New Cloth

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
        resolution: (480, 600)
        play: True
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
    # according to their captured date F. ex 'Captured as '001.jpg' in photo/.
    # Store photos in /photo directory
    def take_photo(self):
        camera = self.ids['camera']
        # Function takes next ID value for new cloth from data base
        id_data = next_id_value()
        camera.export_to_png("photo/{}.png".format(id_data))
        print("Captured as '{}.png' in photo/ ".format(id_data))


class PopupRun(App):
    def build(self):
        content = ConfirmPopup()
        content.bind(on_answer=self._on_answer)
        self.popup = Popup(title="Camera module for new cloth",
                           content=content,
                           size_hint=(None, None),
                           size=(480, 600),
                           auto_dismiss=False)
        self.popup.open()

    def _on_answer(self, instance):
        self.popup.dismiss()
