from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from weather import print_weather_warsaw

Window.size = (400, 650)
Window.clearcolor = (0.8, 0.8, 0.8, 1)

# colors:
#    from rgba to kivy code: 255.0/rgba code
# window background:
#   Hex: #CCCCCC
#   Kivy: 0.8, 0.8, 0.8, 1
# window title:
#   Hex: #666666
#   Kivy: 0.4, 0.4, 0.4, 1
# button background:
#   Hex: #CCCC9A
#   Kivy: 0.8, 0.8, 0.6, 1
# button title:
#   Hex: #999967
#   Kivy: 0.6, 0.6, 0.6, 1


class MainWindow(Screen):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.name = "mainwindow"

        # Define position of main window label
        label_position = AnchorLayout(anchor_x='center',
                                      anchor_y='top')
        label_settings = Label(text='> > > MyOrganiser MainWindow < < <',
                               font_size='20sp',
                               size=(200, 50),
                               size_hint=(None, None),
                               color=(0.4, 0.4, 0.4, 1))
        label_position.add_widget(label_settings)
        self.add_widget(label_position)

        # Define position, size of button 1
        self.Anchor_Layout = AnchorLayout(anchor_x='left',
                                          anchor_y='center')
        self.button = Button(text='button1',
                             valign='top',
                             color=(0.6, 0.6, 0.6, 1),
                             size=(200, 200),
                             size_hint=(None, None),
                             background_color=(0.8, 0.8, 0.6, 1))

        self.button.bind(on_release=self.move_direction_button1)
        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

        # Define position, size of button 2
        self.Anchor_Layout = AnchorLayout(anchor_x='right',
                                          anchor_y='center')
        self.button = Button(text='button2',
                             color=(0.6, 0.6, 0.6, 1),
                             size=(200, 200),
                             size_hint=(None, None),
                             background_color=(0.8, 0.8, 0.6, 1))

        self.button.bind(on_release=self.move_direction_button2)
        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

        # Define position, size of button 3
        self.Anchor_Layout = AnchorLayout(anchor_x='left',
                                          anchor_y='bottom')
        self.button = Button(text='button3',
                             color=(0.6, 0.6, 0.6, 1),
                             size=(200, 200),
                             size_hint=(None, None),
                             background_color=(0.8, 0.8, 0.6, 1))

        self.button.bind(on_release=self.move_direction_button3)
        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

        # Define position, size of button 4
        self.Anchor_Layout = AnchorLayout(anchor_x='right',
                                          anchor_y='bottom')
        self.button = Button(text='button4',
                             color=(0.6, 0.6, 0.6, 1),
                             size=(200, 200),
                             size_hint=(None, None),
                             background_color=(0.8, 0.8, 0.6, 1))

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


class Button1(Screen):
    def __init__(self, **kwargs):
        super(Button1, self).__init__(**kwargs)
        self.name = "button1"

        # Define position of button1 label
        label_position = AnchorLayout(anchor_x='center',
                                      anchor_y='top')
        label_settings = Label(text='> > > MyOrganiser Button1 Window < < <',
                               font_size='20sp',
                               size=(200, 50),
                               size_hint=(None, None),
                               color=(0.4, 0.4, 0.4, 1))
        label_position.add_widget(label_settings)
        self.add_widget(label_position)

        # Define position, size of back button
        self.Anchor_Layout = AnchorLayout(anchor_x='left',
                                          anchor_y='bottom')
        self.button = Button(text='back',
                             size=(100, 50),
                             size_hint=(None, None),
                             # dark red
                             background_color=(1, 0, 0, 1))
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
    def __init__(self, **kwargs):
        super(Button2, self).__init__(**kwargs)
        self.name = "button2"

        # Define position of button2 label
        label_position = AnchorLayout(anchor_x='center',
                                      anchor_y='top')
        label_settings = Label(text='> > > MyOrganiser Button2 Window < < <',
                               font_size='20sp',
                               size=(200, 50),
                               size_hint=(None, None),
                               color=(0.4, 0.4, 0.4, 1))
        label_position.add_widget(label_settings)
        self.add_widget(label_position)

        # Define position, size of back button
        self.Anchor_Layout = AnchorLayout(anchor_x='left',
                                          anchor_y='bottom')
        self.button = Button(text='back',
                             size=(100, 50),
                             size_hint=(None, None),
                             background_color=(1, 0, 0, 1))
        self.button.bind(on_release=self.move_direction_main_window)

        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

    # Define move after press back button
    def move_direction_main_window(self, *args):
        self.manager.current = "mainwindow"


class Button3(Screen):
    def __init__(self, **kwargs):
        super(Button3, self).__init__(**kwargs)
        self.name = "button3"

        # Define position of button3 label
        label_position = AnchorLayout(anchor_x='center',
                                      anchor_y='top')
        label_settings = Label(text='> > > MyOrganiser Button3 Window < < <',
                               font_size='20sp',
                               size=(200, 50),
                               size_hint=(None, None),
                               color=(0.4, 0.4, 0.4, 1))
        label_position.add_widget(label_settings)
        self.add_widget(label_position)

        # Define position, size of back button
        self.Anchor_Layout = AnchorLayout(anchor_x='left',
                                          anchor_y='bottom')
        self.button = Button(text='back',
                             size=(100, 50),
                             size_hint=(None, None),
                             background_color=(1, 0, 0, 1))
        self.button.bind(on_release=self.move_direction_main_window)

        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

    # Define move after press back button
    def move_direction_main_window(self, *args):
        self.manager.current = "mainwindow"


class Button4(Screen):
    def __init__(self, **kwargs):
        super(Button4, self).__init__(**kwargs)
        self.name = "button4"

        # Define position of button4 label
        label_position = AnchorLayout(anchor_x='center',
                                      anchor_y='top')
        label_settings = Label(text='> > > MyOrganiser Button4 Window < < <',
                               font_size='20sp',
                               size=(200, 50),
                               size_hint=(None, None),
                               color=(0.4, 0.4, 0.4, 1))
        label_position.add_widget(label_settings)
        self.add_widget(label_position)

        # Define position, size of back button
        self.Anchor_Layout = AnchorLayout(anchor_x='left',
                                          anchor_y='bottom')
        self.button = Button(text='back',
                             size=(100, 50),
                             size_hint=(None, None),
                             background_color=(1, 0, 0, 1))
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
