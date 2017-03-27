from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from weather import print_weather_warsaw

'''
from rgba to kivy code: rgba code/255.0
window background = hex(#021C1E); rgba(2, 28, 30, 1), kivy(0.007, 0.1, 0.11, 1)
label text color = hex(#2C7873); rgba(44, 120, 115, 1), kivy(0.17, 0.47, 0.45, 1)
button background = hex(#004445); rgba(0, 68, 69, 1), kivy(0, 0.26, 0.27, 1)
button text color = hex(#6FB98F); rgba(111, 185, 143, 1), kivy(0.435, 0.725, 0.56, 1)
'''

# Colors in app
window_background_color = 0.007, 0.1, 0.11, 1
label_text_color = 0.17, 0.47, 0.45, 1
button_background = 0, 0.26, 0.27, 1
button_text_color = 0.435, 0.725, 0.56, 1

Window.clearcolor = window_background_color
Window.size = (400, 650)


class MainWindow(Screen):

    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.name = "mainwindow"

        # Define position of main window label
        label_position = AnchorLayout(anchor_x='center',
                                      anchor_y='top')
        label_settings = Label(text='> > > My Clothes Organiser < < <',
                               font_size='20sp',
                               size=(200, 50),
                               size_hint=(None, None),
                               color=label_text_color)
        label_position.add_widget(label_settings)
        self.add_widget(label_position)

        # Define position, size of button 1
        self.Anchor_Layout = AnchorLayout(anchor_x='left',
                                          anchor_y='center')
        self.button = Button(text='Choose',
                             valign='top',
                             color=button_text_color,
                             size=(200, 200),
                             size_hint=(None, None),
                             background_color=button_background)

        self.button.bind(on_release=self.move_direction_button1)
        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

        # Define position, size of button 2
        self.Anchor_Layout = AnchorLayout(anchor_x='right',
                                          anchor_y='center')
        self.button = Button(text='Rate',
                             color=button_text_color,
                             size=(200, 200),
                             size_hint=(None, None),
                             background_color=button_background)

        self.button.bind(on_release=self.move_direction_button2)
        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

        # Define position, size of button 3
        self.Anchor_Layout = AnchorLayout(anchor_x='left',
                                          anchor_y='bottom')
        self.button = Button(text='History',
                             color=button_text_color,
                             size=(200, 200),
                             size_hint=(None, None),
                             background_color=button_background)

        self.button.bind(on_release=self.move_direction_button3)
        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

        # Define position, size of button 4
        self.Anchor_Layout = AnchorLayout(anchor_x='right',
                                          anchor_y='bottom')
        self.button = Button(text='Change data',
                             color=button_text_color,
                             size=(200, 200),
                             size_hint=(None, None),
                             background_color=button_background)

        self.button.bind(on_release=self.move_direction_button4)
        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)


    # Define move after press buttons from main window
    def move_direction_button1(self, *args):
        self.manager.current = "button1"

    def move_direction_button2(self, *args):
        self.manager.current = "button2"

    def move_direction_button3(self, *args):
        self.manager.current = "button3"

    def move_direction_button4(self, *args):
        self.manager.current = "button4"


# Back button settings
# back_button = Button(text='back',
#                      size=(100, 100),
#                      size_hint=(None, None),
#                      background_normal="./back.png",
#                      background_down="./back.png",
#                      size_hint_x=None)


class Button1(Screen):

# by kind
# by name
# by color
# by rate
# by sets

    def __init__(self, **kwargs):
        super(Button1, self).__init__(**kwargs)
        self.name = "button1"

        # Define position of button1 label
        label_position = AnchorLayout(anchor_x='center',
                                      anchor_y='top')
        label_settings = Label(text='> > > Choose < < <',
                               font_size='20sp',
                               size=(200, 50),
                               size_hint=(None, None),
                               color=label_text_color)
        label_position.add_widget(label_settings)
        self.add_widget(label_position)

        # Define position, size of back button
        self.Anchor_Layout = AnchorLayout(anchor_x='left',
                                          anchor_y='bottom')
        self.button = Button(text='back',
                             size=(100, 100),
                             size_hint=(None, None),
                             background_normal="./back.png",
                             background_down="./back.png",
                             size_hint_x=None)
        self.button.bind(on_release=self.move_direction_main_window)

        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

        # Define position of weather label,
        # run print_weather_warsaw from weather.py,
        # print text from weatherdata.txt
        with open('weatherdata.txt', encoding='utf-8') as weatherdata:
            read_weatherdata = weatherdata.read()

        label_position = AnchorLayout(anchor_x='right',
                                      anchor_y='bottom')
        label_settings = Label(text=read_weatherdata,
                               font_size='12sp',
                               size_hint=(None, None),
                               size=(200, 200),
                               color=(0.4, 0.4, 0.4, 1))

        label_position.add_widget(label_settings)
        self.add_widget(label_position)

    # Define move after press back button
    def move_direction_main_window(self, *args):
        self.manager.current = "mainwindow"


class Button2(Screen):

# 5 stars rate
# based in data base

    def __init__(self, **kwargs):
        super(Button2, self).__init__(**kwargs)
        self.name = "button2"

        # Define position of button2 label
        label_position = AnchorLayout(anchor_x='center',
                                      anchor_y='top')
        label_settings = Label(text='> > > Rate < < <',
                               font_size='20sp',
                               size=(200, 50),
                               size_hint=(None, None),
                               color=label_text_color)
        label_position.add_widget(label_settings)
        self.add_widget(label_position)

        # Define position, size of back button
        self.Anchor_Layout = AnchorLayout(anchor_x='left',
                                          anchor_y='bottom')
        self.button = Button(text='back',
                             size=(100, 100),
                             size_hint=(None, None),
                             background_normal="./back.png",
                             background_down="./back.png",
                             size_hint_x=None)
        self.button.bind(on_release=self.move_direction_main_window)

        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

    # Define move after press back button
    def move_direction_main_window(self, *args):
        self.manager.current = "mainwindow"


class Button3(Screen):

# day by day
# photo option
# based in data base

    def __init__(self, **kwargs):
        super(Button3, self).__init__(**kwargs)
        self.name = "button3"

        # Define position of button3 label
        label_position = AnchorLayout(anchor_x='center',
                                      anchor_y='top')
        label_settings = Label(text='> > > History < < <',
                               font_size='20sp',
                               size=(200, 50),
                               size_hint=(None, None),
                               color=label_text_color)
        label_position.add_widget(label_settings)
        self.add_widget(label_position)

        # Define position, size of back button
        self.Anchor_Layout = AnchorLayout(anchor_x='left',
                                          anchor_y='bottom')
        self.button = Button(text='back',
                             size=(100, 100),
                             size_hint=(None, None),
                             background_normal="./back.png",
                             background_down="./back.png",
                             size_hint_x=None)
        self.button.bind(on_release=self.move_direction_main_window)

        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

    # Define move after press back button
    def move_direction_main_window(self, *args):
        self.manager.current = "mainwindow"


class Button4(Screen):

# add new cloth
# change data
# delete cloth

    def __init__(self, **kwargs):
        super(Button4, self).__init__(**kwargs)
        self.name = "button4"

        # Define position of button4 label
        label_position = AnchorLayout(anchor_x='center',
                                      anchor_y='top')
        label_settings = Label(text='> > > Add, change, delete < < <',
                               font_size='20sp',
                               size=(200, 50),
                               size_hint=(None, None),
                               color=label_text_color)
        label_position.add_widget(label_settings)
        self.add_widget(label_position)

        # Define position, size of back button
        self.Anchor_Layout = AnchorLayout(anchor_x='left',
                                          anchor_y='bottom')
        self.button = Button(text='back',
                             size=(100, 100),
                             size_hint=(None, None),
                             background_normal="./back.png",
                             background_down="./back.png",
                             size_hint_x=None)
        self.button.bind(on_release=self.move_direction_main_window)

        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

    # Define move after press back button
    def move_direction_main_window(self, *args):
        self.manager.current = "mainwindow"


class MyOrganiser(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainWindow())
        screen_manager.add_widget(Button1())
        screen_manager.add_widget(Button2())
        screen_manager.add_widget(Button3())
        screen_manager.add_widget(Button4())
        return screen_manager


MyOrganiser().run()
