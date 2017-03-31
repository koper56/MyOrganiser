from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
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
window_background_color = 0.047, 0.2, 0.11, 1
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

        # Define position, size of choose
        self.Anchor_Layout = AnchorLayout(anchor_x='left',
                                          anchor_y='center')
        self.button = Button(text='Choose',
                             valign='top',
                             color=button_text_color,
                             size=(200, 200),
                             size_hint=(None, None),
                             background_color=button_background)

        self.button.bind(on_release=self.move_direction_choose_window)
        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

        # Define position, size of rate
        self.Anchor_Layout = AnchorLayout(anchor_x='right',
                                          anchor_y='center')
        self.button = Button(text='Rate',
                             color=button_text_color,
                             size=(200, 200),
                             size_hint=(None, None),
                             background_color=button_background)

        self.button.bind(on_release=self.move_direction_rate_window)
        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

        # Define position, size of history
        self.Anchor_Layout = AnchorLayout(anchor_x='left',
                                          anchor_y='bottom')
        self.button = Button(text='History',
                             color=button_text_color,
                             size=(200, 200),
                             size_hint=(None, None),
                             background_color=button_background)

        self.button.bind(on_release=self.move_direction_history_window)
        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

        # Define position, size of change data
        self.Anchor_Layout = AnchorLayout(anchor_x='right',
                                          anchor_y='bottom')
        self.button = Button(text='Change data',
                             color=button_text_color,
                             size=(200, 200),
                             size_hint=(None, None),
                             background_color=button_background)

        self.button.bind(on_release=self.move_direction_change_window)
        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

    # Define move after press buttons from main window
    def move_direction_choose_window(self, *args):
        self.manager.current = "choosewindow"

    def move_direction_rate_window(self, *args):
        self.manager.current = "ratewindow"

    def move_direction_history_window(self, *args):
        self.manager.current = "historywindow"

    def move_direction_change_window(self, *args):
        self.manager.current = "changewindow"


# Back button settings
# back_button = Button(text='back',
#                      size=(100, 100),
#                      size_hint=(None, None),
#                      background_normal="./back.png",
#                      background_down="./back.png",
#                      size_hint_x=None)


class ChooseWindow(Screen):
    # by kind
    # by name
    # by color
    # by rate
    # by sets

    def __init__(self, **kwargs):
        super(ChooseWindow, self).__init__(**kwargs)
        self.name = "choosewindow"

        # Define position of choose window label
        label_position = AnchorLayout(anchor_x='center',
                                      anchor_y='top')
        label_settings = Label(text='> > > Choose by... < < <',
                               font_size='20sp',
                               size=(200, 50),
                               size_hint=(None, None),
                               color=label_text_color)
        label_position.add_widget(label_settings)
        self.add_widget(label_position)

        # Define position, size of kinds button
        self.Float_Layout = FloatLayout(size=(450, 100))

        self.button = Button(text='Kinds',
                             size_hint=(None, None),
                             size=(450, 50),
                             pos=(0, 400),
                             color=button_text_color,
                             background_color=button_background)
        self.button.bind(on_release=self.move_direction_choose_kinds_window)

        self.Float_Layout.add_widget(self.button)
        self.add_widget(self.Float_Layout)

        # Define position, size of names button
        self.Float_Layout = FloatLayout(size=(450, 100))

        self.button = Button(text='Names',
                             size_hint=(None, None),
                             size=(450, 50),
                             pos=(0, 350),
                             color=button_text_color,
                             background_color=button_background)
        self.button.bind(on_release=self.move_direction_choose_names_window)

        self.Float_Layout.add_widget(self.button)
        self.add_widget(self.Float_Layout)

        # Define position, size of colors button
        self.Float_Layout = FloatLayout(size=(450, 100))

        self.button = Button(text='Colors',
                             size_hint=(None, None),
                             size=(450, 50),
                             pos=(0, 300),
                             color=button_text_color,
                             background_color=button_background)
        self.button.bind(on_release=self.move_direction_choose_colors_window)

        self.Float_Layout.add_widget(self.button)
        self.add_widget(self.Float_Layout)

        # Define position, size of rates button
        self.Float_Layout = FloatLayout(size=(450, 100))

        self.button = Button(text='Rates',
                             size_hint=(None, None),
                             size=(450, 50),
                             pos=(0, 250),
                             color=button_text_color,
                             background_color=button_background)
        self.button.bind(on_release=self.move_direction_choose_rates_window)

        self.Float_Layout.add_widget(self.button)
        self.add_widget(self.Float_Layout)

        # Define position, size of sets button
        self.Float_Layout = FloatLayout(size=(450, 100))

        self.button = Button(text='Sets',
                             size_hint=(None, None),
                             size=(450, 50),
                             pos=(0, 200),
                             color=button_text_color,
                             background_color=button_background)
        self.button.bind(on_release=self.move_direction_choose_sets_window)

        self.Float_Layout.add_widget(self.button)
        self.add_widget(self.Float_Layout)

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

    # Define move after press kinds button
    def move_direction_choose_kinds_window(self, *args):
        self.manager.current = "choosekindswindow"

    # Define move after press names button
    def move_direction_choose_names_window(self, *args):
        self.manager.current = "choosenameswindow"

    # Define move after press colors button
    def move_direction_choose_colors_window(self, *args):
        self.manager.current = "choosecolorswindow"

    # Define move after press rates button
    def move_direction_choose_rates_window(self, *args):
        self.manager.current = "chooserateswindow"

    # Define move after press sets button
    def move_direction_choose_sets_window(self, *args):
        self.manager.current = "choosesetswindow"

    # Define move after press back button
    def move_direction_main_window(self, *args):
        self.manager.current = "mainwindow"


class RateWindow(Screen):
    # 5 stars rate
    # based in data base

    def __init__(self, **kwargs):
        super(RateWindow, self).__init__(**kwargs)
        self.name = "ratewindow"

        # Define position of rate rate window label
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


class HistoryWindow(Screen):
    # day by day
    # photo option
    # based in data base

    def __init__(self, **kwargs):
        super(HistoryWindow, self).__init__(**kwargs)
        self.name = "historywindow"

        # Define position of history window label
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


class ChangeWindow(Screen):
    # add new cloth
    # change data
    # change clear
    # delete cloth

    def __init__(self, **kwargs):
        super(ChangeWindow, self).__init__(**kwargs)
        self.name = "changewindow"

        # Define position of change window label
        label_position = AnchorLayout(anchor_x='center',
                                      anchor_y='top')
        label_settings = Label(text='> > > Add, change, delete < < <',
                               font_size='20sp',
                               size=(200, 50),
                               size_hint=(None, None),
                               color=label_text_color)
        label_position.add_widget(label_settings)
        self.add_widget(label_position)

        # Define position, size of add new cloth button
        self.Float_Layout = FloatLayout(size=(450, 100))

        self.button = Button(text='Add new cloth',
                             size_hint=(None, None),
                             size=(450, 50),
                             pos=(0, 400),
                             color=button_text_color,
                             background_color=button_background)
        self.button.bind(on_release=self.move_direction_add_new_cloth_window)

        self.Float_Layout.add_widget(self.button)
        self.add_widget(self.Float_Layout)

        # Define position, size of change cloth clear button
        self.Float_Layout = FloatLayout(size=(450, 100))

        self.button = Button(text='Change cloth clear',
                             size_hint=(None, None),
                             size=(450, 50),
                             pos=(0, 350),
                             color=button_text_color,
                             background_color=button_background)
        self.button.bind(on_release=self.move_direction_change_clear_window)

        self.Float_Layout.add_widget(self.button)
        self.add_widget(self.Float_Layout)

        # Define position, size of change cloth data button
        self.Float_Layout = FloatLayout(size=(450, 100))

        self.button = Button(text='Change cloth data',
                             size_hint=(None, None),
                             size=(450, 50),
                             pos=(0, 300),
                             color=button_text_color,
                             background_color=button_background)
        self.button.bind(on_release=self.move_direction_change_clear_data)

        self.Float_Layout.add_widget(self.button)
        self.add_widget(self.Float_Layout)

        # Define position, size of delete cloth button
        self.Float_Layout = FloatLayout(size=(450, 100))

        self.button = Button(text='Delete cloth',
                             size_hint=(None, None),
                             size=(450, 50),
                             pos=(0, 250),
                             color=button_text_color,
                             background_color=button_background)
        self.button.bind(on_release=self.move_direction_delete_cloth_window)

        self.Float_Layout.add_widget(self.button)
        self.add_widget(self.Float_Layout)

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

    # Define move after press add new cloth button
    def move_direction_add_new_cloth_window(self, *args):
        self.manager.current = "addnewclothwindow"

    # Define move after press change cloth clear
    def move_direction_change_clear_window(self, *args):
        self.manager.current = "changeclearwindow"

    # Define move after press change cloth data
    def move_direction_change_clear_data(self, *args):
        self.manager.current = "changeclothdatawindow"

    # Define move after press change cloth data
    def move_direction_delete_cloth_window(self, *args):
        self.manager.current = "deleteclothwindow"


class ChooseNames(Screen):
    def __init__(self, **kwargs):
        super(ChooseNames, self).__init__(**kwargs)
        self.name = "choosenameswindow"

        # Define position of choose by names window label
        label_position = AnchorLayout(anchor_x='center',
                                      anchor_y='top')
        label_settings = Label(text='> > > Choose by names < < <',
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
        self.button.bind(on_release=self.move_direction_choose_window)

        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

    # Define move after press back button
    def move_direction_choose_window(self, *args):
        self.manager.current = "choosewindow"


class ChooseKinds(Screen):
    def __init__(self, **kwargs):
        super(ChooseKinds, self).__init__(**kwargs)
        self.name = "choosekindswindow"

        # Define position of choose by kinds window label
        label_position = AnchorLayout(anchor_x='center',
                                      anchor_y='top')
        label_settings = Label(text='> > > Choose by kinds < < <',
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
        self.button.bind(on_release=self.move_direction_choose_window)

        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

    # Define move after press back button
    def move_direction_choose_window(self, *args):
        self.manager.current = "choosewindow"


class ChooseColors(Screen):
    def __init__(self, **kwargs):
        super(ChooseColors, self).__init__(**kwargs)
        self.name = "choosecolorswindow"

        # Define position of choose by colors window label
        label_position = AnchorLayout(anchor_x='center',
                                      anchor_y='top')
        label_settings = Label(text='> > > Choose by colors < < <',
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
        self.button.bind(on_release=self.move_direction_choose_window)

        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

    # Define move after press back button
    def move_direction_choose_window(self, *args):
        self.manager.current = "choosewindow"


class ChooseRates(Screen):
    def __init__(self, **kwargs):
        super(ChooseRates, self).__init__(**kwargs)
        self.name = "chooserateswindow"

        # Define position of choose by rates window label
        label_position = AnchorLayout(anchor_x='center',
                                      anchor_y='top')
        label_settings = Label(text='> > > Choose by rates < < <',
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
        self.button.bind(on_release=self.move_direction_choose_window)

        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

    # Define move after press back button
    def move_direction_choose_window(self, *args):
        self.manager.current = "choosewindow"


class ChooseSets(Screen):
    def __init__(self, **kwargs):
        super(ChooseSets, self).__init__(**kwargs)
        self.name = "choosesetswindow"

        # Define position of choose by sets window label
        label_position = AnchorLayout(anchor_x='center',
                                      anchor_y='top')
        label_settings = Label(text='> > > Choose by sets < < <',
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
        self.button.bind(on_release=self.move_direction_choose_window)

        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

    # Define move after press back button
    def move_direction_choose_window(self, *args):
        self.manager.current = "choosewindow"


class AddNewClothWindow(Screen):
    def __init__(self, **kwargs):
        super(AddNewClothWindow, self).__init__(**kwargs)
        self.name = "addnewclothwindow"

        # Define position of add cloth window label
        label_position = AnchorLayout(anchor_x='center',
                                      anchor_y='top')
        label_settings = Label(text='> > > Add new cloth < < <',
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
        self.button.bind(on_release=self.move_direction_change_window)

        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

    # Define move after press back button
    def move_direction_change_window(self, *args):
        self.manager.current = "changewindow"


class ChangeClearWindow(Screen):
    def __init__(self, **kwargs):
        super(ChangeClearWindow, self).__init__(**kwargs)
        self.name = "changeclearwindow"

        # Define position of change clear of cloth window label
        label_position = AnchorLayout(anchor_x='center',
                                      anchor_y='top')
        label_settings = Label(text='> > > Change clear < < <',
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
        self.button.bind(on_release=self.move_direction_change_window)

        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

    # Define move after press back button
    def move_direction_change_window(self, *args):
        self.manager.current = "changewindow"


class ChangeClearData(Screen):
    def __init__(self, **kwargs):
        super(ChangeClearData, self).__init__(**kwargs)
        self.name = "changeclothdatawindow"

        # Define position of change cloth data window label
        label_position = AnchorLayout(anchor_x='center',
                                      anchor_y='top')
        label_settings = Label(text='> > > Change data < < <',
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
        self.button.bind(on_release=self.move_direction_change_window)

        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

    # Define move after press back button
    def move_direction_change_window(self, *args):
        self.manager.current = "changewindow"


class DeleteCloth(Screen):
    def __init__(self, **kwargs):
        super(DeleteCloth, self).__init__(**kwargs)
        self.name = "deleteclothwindow"

        # Define position of delete cloth window label
        label_position = AnchorLayout(anchor_x='center',
                                      anchor_y='top')
        label_settings = Label(text='> > > Delete cloth < < <',
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
        self.button.bind(on_release=self.move_direction_change_window)

        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

    # Define move after press back button
    def move_direction_change_window(self, *args):
        self.manager.current = "changewindow"


class MyOrganiser(App):
    def build(self):
        screen_manager = ScreenManager()

        # For Main Window
        screen_manager.add_widget(MainWindow())
        screen_manager.add_widget(ChooseWindow())
        screen_manager.add_widget(RateWindow())
        screen_manager.add_widget(HistoryWindow())
        screen_manager.add_widget(ChangeWindow())

        # For Choose Window
        screen_manager.add_widget(ChooseKinds())
        screen_manager.add_widget(ChooseNames())
        screen_manager.add_widget(ChooseColors())
        screen_manager.add_widget(ChooseRates())
        screen_manager.add_widget(ChooseSets())

        # For Change Window
        screen_manager.add_widget(AddNewClothWindow())
        screen_manager.add_widget(ChangeClearWindow())
        screen_manager.add_widget(ChangeClearData())
        screen_manager.add_widget(DeleteCloth())

        return screen_manager


MyOrganiser().run()
