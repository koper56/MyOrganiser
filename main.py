from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
import data_base
from weather import print_weather_warsaw

'''
from rgba to kivy code: rgba code/255.0
window background = hex(#021C1E); rgba(2, 28, 30, 1), 
                    kivy(0.007, 0.1, 0.11, 1)
label text color = hex(#2C7873); rgba(44, 120, 115, 1), 
                   kivy(0.17, 0.47, 0.45, 1)
button background = hex(#004445); rgba(0, 68, 69, 1), 
                    kivy(0, 0.26, 0.27, 1)
button text color = hex(#6FB98F); rgba(111, 185, 143, 1), 
                    kivy(0.435, 0.725, 0.56, 1)
'''

# Colors in app
window_background_color = 0.047, 0.2, 0.11, 1
label_text_color = 0.17, 0.47, 0.45, 1
button_background = 0, 0.26, 0.27, 1
button_text_color = 0.435, 0.725, 0.56, 1
data_text_color = 0.17, 0.47, 1, 1
data_label_background_color = 1, 0.2, 0.11, 1


# Window.clearcolor = window_background_color
# Window.size = (400, 650)


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
    # weather info

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
                             color=button_text_color,
                             size_hint=(None, None),
                             background_normal="./png/back.png",
                             background_down="./png/back.png",
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
                               color=data_text_color)

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
    # rate cloth
    # rate set
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

        # Define position, size of rate cloth button
        self.Float_Layout = FloatLayout(size=(450, 100))

        self.button = Button(text='Cloth',
                             size_hint=(None, None),
                             size=(450, 50),
                             pos=(0, 400),
                             color=button_text_color,
                             background_color=button_background)
        self.button.bind(on_release=self.move_direction_rate_cloth_window)

        self.Float_Layout.add_widget(self.button)
        self.add_widget(self.Float_Layout)

        # Define position, size of rate set button
        self.Float_Layout = FloatLayout(size=(450, 100))

        self.button = Button(text='Set',
                             size_hint=(None, None),
                             size=(450, 50),
                             pos=(0, 350),
                             color=button_text_color,
                             background_color=button_background)
        self.button.bind(on_release=self.move_direction_rate_set_window)

        self.Float_Layout.add_widget(self.button)
        self.add_widget(self.Float_Layout)

        # Define position, size of back button
        self.Anchor_Layout = AnchorLayout(anchor_x='left',
                                          anchor_y='bottom')
        self.button = Button(text='back',
                             size=(100, 100),
                             color=button_text_color,
                             size_hint=(None, None),
                             background_normal="./png/back.png",
                             background_down="./png/back.png",
                             size_hint_x=None)
        self.button.bind(on_release=self.move_direction_main_window)

        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

    # Define move after press cloth button
    def move_direction_rate_cloth_window(self, *args):
        self.manager.current = "rateclothwindow"

    # Define move after press set button
    def move_direction_rate_set_window(self, *args):
        self.manager.current = "ratesetwindow"

    # Define move after press back button
    def move_direction_main_window(self, *args):
        self.manager.current = "mainwindow"


class HistoryWindow(Screen):
    # day by day
    # photo option

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

        # Define position, size of history day by day button
        self.Float_Layout = FloatLayout(size=(450, 100))

        self.button = Button(text='Day by day',
                             size_hint=(None, None),
                             size=(450, 50),
                             pos=(0, 400),
                             color=button_text_color,
                             background_color=button_background)
        self.button.bind(on_release=self.move_direction_day_history)

        self.Float_Layout.add_widget(self.button)
        self.add_widget(self.Float_Layout)

        # Define position, size of photo button
        self.Float_Layout = FloatLayout(size=(450, 100))

        self.button = Button(text='Photo',
                             size_hint=(None, None),
                             size=(450, 50),
                             pos=(0, 350),
                             color=button_text_color,
                             background_color=button_background)
        self.button.bind(on_release=self.move_direction_photo)

        self.Float_Layout.add_widget(self.button)
        self.add_widget(self.Float_Layout)

        # Define position, size of back button
        self.Anchor_Layout = AnchorLayout(anchor_x='left',
                                          anchor_y='bottom')
        self.button = Button(text='back',
                             size=(100, 100),
                             color=button_text_color,
                             size_hint=(None, None),
                             background_normal="./png/back.png",
                             background_down="./png/back.png",
                             size_hint_x=None)
        self.button.bind(on_release=self.move_direction_main_window)

        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

    # Define move after press day by day button
    def move_direction_day_history(self, *args):
        self.manager.current = "dayhistorywindow"

    # Define move after press photo button
    def move_direction_photo(self, *args):
        self.manager.current = "photowindow"

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
                             color=button_text_color,
                             size_hint=(None, None),
                             background_normal="./png/back.png",
                             background_down="./png/back.png",
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
        label_settings = Label(text='> > > Choose by name < < <',
                               font_size='20sp',
                               size=(200, 50),
                               size_hint=(None, None),
                               color=label_text_color)
        label_position.add_widget(label_settings)
        self.add_widget(label_position)

        # Define position of text input box
        self.input_box_pos = AnchorLayout(anchor_x='center',
                                          anchor_y='bottom')
        self.input_box = TextInput(text='Type name',
                                   multiline=False,
                                   size=(200, 50),
                                   size_hint=(None, None))
        self.input_box_pos.add_widget(self.input_box)
        self.add_widget(self.input_box_pos)

        # Define position of search button
        self.search_button_pos = AnchorLayout(anchor_x='right',
                                              anchor_y='bottom')
        self.search_button = Button(text='OK',
                                    size=(100, 50),
                                    color=button_text_color,
                                    background_color=button_background,
                                    size_hint=(None, None))
        self.search_button_pos.add_widget(self.search_button)
        self.add_widget(self.search_button_pos)

        # Run function press button after press OK
        self.search_button.bind(on_press=self.press_button)

        # Search result label, shows full data of clothes
        # Define position of search result label
        self.search_result_pos = AnchorLayout(anchor_y='center',
                                              anchor_x='center')
        # text_size=self.size -> Wrapping text
        self.search_result = Label(text='[i]Search result[/i]',
                                   markup=True,
                                   font_size='16sp',
                                   text_size=(250, 400),
                                   valign='middle',
                                   halign='left',
                                   size_hint=(None, None),
                                   color=data_text_color)
        self.search_result_pos.add_widget(self.search_result)
        self.add_widget(self.search_result_pos)

        # Define position of label with all data
        self.all_data_pos = AnchorLayout(anchor_y='center',
                                         anchor_x='left')
        # Take all names from data_base.py get_names_clothes_data_row func
        # and return in label
        names_from_database = str(data_base.get_names_clothes_data_row())
        self.all_data = Label(text=names_from_database,
                              markup=True,
                              font_size='16sp',
                              text_size=(100, 400),
                              valign='middle',
                              halign='left',
                              size_hint=(None, None),
                              color=data_text_color)
        self.all_data_pos.add_widget(self.all_data)
        self.add_widget(self.all_data_pos)

        # Define position of label with photo
        self.show_photo_pos = AnchorLayout(anchor_y='center',
                                           anchor_x='right')
        # Default icon in source
        self.show_photo = Image(source='png/database.png',
                                size=(200, 360),
                                size_hint=(None, None))
        self.show_photo_pos.add_widget(self.show_photo)
        self.add_widget(self.show_photo_pos)

        # Define position, size of back button
        self.Anchor_Layout = AnchorLayout(anchor_x='left',
                                          anchor_y='bottom')
        self.button = Button(text='back',
                             size=(100, 100),
                             color=button_text_color,
                             size_hint=(None, None),
                             background_normal="./png/back.png",
                             background_down="./png/back.png",
                             size_hint_x=None)
        self.button.bind(on_release=self.move_direction_choose_window)

        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

    def press_button(self, btn):
        # Send text after press button OK from input box to function in data
        # base, take data and return in search_result label and photo_source

        # Connect with function print_one_data_by_name form data_base.py
        # Give data from list row, return from  print_one_data_by_name
        function_from_database = \
            data_base.print_one_data_by_name(self.input_box.text)

        # Data for source in show_photo from photo_source in data base
        # for typed data in input_box
        self.show_photo.source = str(function_from_database[5])

        # Data for text in search_result from all columns in data base
        # for typed data in input_box
        # Colors take hex color code from data base and set this code for
        # ███ characters
        self.search_result.text = "[i]Result:[/i] \n" \
                                  "[b]ID:[/b] {}\n" \
                                  "[b]Name:[/b] {}\n" \
                                  "[b]Colors: " \
                                  "[color={}]███ [/color]" \
                                  "[color={}]███ [/color]" \
                                  "[color={}]███[/color][/b] \n" \
                                  "[b]Photo:[/b] {}\n" \
                                  "[b]Description:[/b] {}\n" \
                                  "[b]Exclusions:[/b] {}\n" \
                                  "[b]Clear:[/b] {}\n" \
                                  "[b]Rate:[/b] {}\n" \
                                  "[b]Kind:[/b] {}".format \
            (function_from_database[0],
             function_from_database[1],
             function_from_database[2],
             function_from_database[3],
             function_from_database[4],
             function_from_database[5],
             function_from_database[6],
             function_from_database[7],
             function_from_database[8],
             function_from_database[9],
             function_from_database[10])

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
        label_settings = Label(text='> > > Choose kind < < <',
                               font_size='20sp',
                               size=(200, 50),
                               size_hint=(None, None),
                               color=label_text_color)
        label_position.add_widget(label_settings)
        self.add_widget(label_position)

        # buttons with kinds (t_shirts, tank_tops, hoodies, shirts,
        # trousers, shorts, shoes, hats, jackets, sunglasses, necklaces,
        # piercing, rings, bracelets, bags, gloves, scarfs
        # after press kind button print clothes from selected kind
        # after type name print full info and photo
        self.kind_t_shirts_pos = FloatLayout(size=(100, 50))
        self.kind_t_shirts = Button(text='T-shirts',
                                    size_hint=(None, None),
                                    size=(100, 50),
                                    pos=(0, 500),
                                    color=button_text_color,
                                    background_color=button_background)
        self.kind_t_shirts_pos.add_widget(self.kind_t_shirts)
        self.add_widget(self.kind_t_shirts_pos)
        # Run function press_button_t_shirts after press T-shirts
        self.kind_t_shirts.bind(on_press=self.press_button_t_shirts)

        self.kind_tank_tops_pos = FloatLayout(size=(100, 50))
        self.kind_tank_tops = Button(text='Tank tops',
                                     size_hint=(None, None),
                                     size=(100, 50),
                                     pos=(0, 450),
                                     color=button_text_color,
                                     background_color=button_background)
        self.kind_tank_tops_pos.add_widget(self.kind_tank_tops)
        self.add_widget(self.kind_tank_tops_pos)
        # Run function press_button_tank_tops after press Tank tops
        self.kind_tank_tops.bind(on_press=self.press_button_tank_tops)

        self.kind_hoodies_pos = FloatLayout(size=(100, 50))
        self.kind_hoodies = Button(text='Hoodies',
                                   size_hint=(None, None),
                                   size=(100, 50),
                                   pos=(0, 400),
                                   color=button_text_color,
                                   background_color=button_background)
        self.kind_hoodies_pos.add_widget(self.kind_hoodies)
        self.add_widget(self.kind_hoodies_pos)
        # Run function press_button_hoodies after press Hoodies
        self.kind_hoodies.bind(on_press=self.press_button_hoodies)

        self.kind_shirts_pos = FloatLayout(size=(100, 50))
        self.kind_shirts = Button(text='Shirts',
                                  size_hint=(None, None),
                                  size=(100, 50),
                                  pos=(0, 350),
                                  color=button_text_color,
                                  background_color=button_background)
        self.kind_shirts_pos.add_widget(self.kind_shirts)
        self.add_widget(self.kind_shirts_pos)
        # Run function press_button_shirts after press Shirts
        self.kind_shirts.bind(on_press=self.press_button_shirts)

        self.kind_trousers_pos = FloatLayout(size=(100, 50))
        self.kind_trousers = Button(text='Trousers',
                                    size_hint=(None, None),
                                    size=(100, 50),
                                    pos=(0, 300),
                                    color=button_text_color,
                                    background_color=button_background)
        self.kind_trousers_pos.add_widget(self.kind_trousers)
        self.add_widget(self.kind_trousers_pos)
        # Run function press_button_trousers after press Trousers
        self.kind_trousers.bind(on_press=self.press_button_trousers)

        self.kind_shorts_pos = FloatLayout(size=(100, 50))
        self.kind_shorts = Button(text='Shorts',
                                  size_hint=(None, None),
                                  size=(100, 50),
                                  pos=(0, 250),
                                  color=button_text_color,
                                  background_color=button_background)
        self.kind_shorts_pos.add_widget(self.kind_shorts)
        self.add_widget(self.kind_shorts_pos)
        # Run function press_button_shorts after press Shorts
        self.kind_shorts.bind(on_press=self.press_button_shorts)

        self.kind_shoes_pos = FloatLayout(size=(100, 50))
        self.kind_shoes = Button(text='Shoes',
                                 size_hint=(None, None),
                                 size=(100, 50),
                                 pos=(0, 200),
                                 color=button_text_color,
                                 background_color=button_background)
        self.kind_shoes_pos.add_widget(self.kind_shoes)
        self.add_widget(self.kind_shoes_pos)
        # Run function press_button_shoes after press Shoes
        self.kind_shoes.bind(on_press=self.press_button_shoes)

        self.kind_hats_pos = FloatLayout(size=(100, 50))
        self.kind_hats = Button(text='Hats',
                                size_hint=(None, None),
                                size=(100, 50),
                                pos=(0, 150),
                                color=button_text_color,
                                background_color=button_background)
        self.kind_hats_pos.add_widget(self.kind_hats)
        self.add_widget(self.kind_hats_pos)
        # Run function press_button_hats after press Hats
        self.kind_hats.bind(on_press=self.press_button_hats)

        self.kind_jackets_pos = FloatLayout(size=(100, 50))
        self.kind_jackets = Button(text='Jackets',
                                   size_hint=(None, None),
                                   size=(100, 50),
                                   pos=(100, 500),
                                   color=button_text_color,
                                   background_color=button_background)
        self.kind_jackets_pos.add_widget(self.kind_jackets)
        self.add_widget(self.kind_jackets_pos)
        # Run function press_button_jackets after press Jackets
        self.kind_jackets.bind(on_press=self.press_button_jackets)

        self.kind_sunglasses_pos = FloatLayout(size=(100, 50))
        self.kind_sunglasses = Button(text='Sunglasses',
                                      size_hint=(None, None),
                                      size=(100, 50),
                                      pos=(100, 450),
                                      color=button_text_color,
                                      background_color=button_background)
        self.kind_sunglasses_pos.add_widget(self.kind_sunglasses)
        self.add_widget(self.kind_sunglasses_pos)
        # Run function press_button_sunglasses after press Sunglasses
        self.kind_sunglasses.bind(on_press=self.press_button_sunglasses)

        self.kind_necklaces_pos = FloatLayout(size=(100, 50))
        self.kind_necklaces = Button(text='Necklaces',
                                     size_hint=(None, None),
                                     size=(100, 50),
                                     pos=(100, 400),
                                     color=button_text_color,
                                     background_color=button_background)
        self.kind_necklaces_pos.add_widget(self.kind_necklaces)
        self.add_widget(self.kind_necklaces_pos)
        # Run function press_button_necklaces after press Necklaces
        self.kind_necklaces.bind(on_press=self.press_button_necklaces)

        self.kind_piercing_pos = FloatLayout(size=(100, 50))
        self.kind_piercing = Button(text='Piercing',
                                    size_hint=(None, None),
                                    size=(100, 50),
                                    pos=(100, 350),
                                    color=button_text_color,
                                    background_color=button_background)
        self.kind_piercing_pos.add_widget(self.kind_piercing)
        self.add_widget(self.kind_piercing_pos)
        # Run function press_button_piercing after press Piercing
        self.kind_piercing.bind(on_press=self.press_button_piercing)

        self.kind_rings_pos = FloatLayout(size=(100, 50))
        self.kind_rings = Button(text='Rings',
                                 size_hint=(None, None),
                                 size=(100, 50),
                                 pos=(100, 300),
                                 color=button_text_color,
                                 background_color=button_background)
        self.kind_rings_pos.add_widget(self.kind_rings)
        self.add_widget(self.kind_rings_pos)
        # Run function press_button_rings after press Rings
        self.kind_rings.bind(on_press=self.press_button_rings)

        self.kind_bracelets_pos = FloatLayout(size=(100, 50))
        self.kind_bracelets = Button(text='Bracelets',
                                     size_hint=(None, None),
                                     size=(100, 50),
                                     pos=(100, 250),
                                     color=button_text_color,
                                     background_color=button_background)
        self.kind_bracelets_pos.add_widget(self.kind_bracelets)
        self.add_widget(self.kind_bracelets_pos)
        # Run function press_button_bracelets after press bracelets
        self.kind_bracelets.bind(on_press=self.press_button_bracelets)

        self.kind_bags_pos = FloatLayout(size=(100, 50))
        self.kind_bags = Button(text='Bags',
                                size_hint=(None, None),
                                size=(100, 50),
                                pos=(100, 200),
                                color=button_text_color,
                                background_color=button_background)
        self.kind_bags_pos.add_widget(self.kind_bags)
        self.add_widget(self.kind_bags_pos)
        # Run function press_button_bags after press Bags
        self.kind_bags.bind(on_press=self.press_button_bags)

        self.kind_gloves_pos = FloatLayout(size=(100, 50))
        self.kind_gloves = Button(text='Gloves',
                                  size_hint=(None, None),
                                  size=(100, 50),
                                  pos=(100, 150),
                                  color=button_text_color,
                                  background_color=button_background)
        self.kind_gloves_pos.add_widget(self.kind_gloves)
        self.add_widget(self.kind_gloves_pos)
        # Run function press_button_gloves after press Gloves
        self.kind_gloves.bind(on_press=self.press_button_gloves)

        self.kind_scarfs_pos = FloatLayout(size=(100, 50))
        self.kind_scarfs = Button(text='Scarfs',
                                  size_hint=(None, None),
                                  size=(100, 50),
                                  pos=(200, 500),
                                  color=button_text_color,
                                  background_color=button_background)
        self.kind_scarfs_pos.add_widget(self.kind_scarfs)
        self.add_widget(self.kind_scarfs_pos)
        # Run function press_button_scarfs after press Scarfs
        self.kind_scarfs.bind(on_press=self.press_button_scarfs)

        # Define position of search result label
        self.search_result_pos = AnchorLayout(anchor_y='center',
                                              anchor_x='center')
        # Search result label, shows names of clothes and full data of clothes
        # text_size=self.size -> Wrapping text
        self.search_result = Label(text='[i]Search result[/i]',
                                   markup=True,
                                   font_size='16sp',
                                   text_size=(250, 400),
                                   valign='middle',
                                   halign='left',
                                   size_hint=(None, None),
                                   color=data_text_color)
        self.search_result_pos.add_widget(self.search_result)
        self.add_widget(self.search_result_pos)

        # Define position of text input box
        self.input_box_pos = AnchorLayout(anchor_x='center',
                                          anchor_y='bottom')
        self.input_box = TextInput(text='Type name',
                                   multiline=False,
                                   size=(200, 50),
                                   size_hint=(None, None))
        self.input_box_pos.add_widget(self.input_box)
        self.add_widget(self.input_box_pos)

        # Define position of search button
        self.search_button_pos = AnchorLayout(anchor_x='right',
                                              anchor_y='bottom')
        self.search_button = Button(text='OK',
                                    size=(100, 50),
                                    color=button_text_color,
                                    background_color=button_background,
                                    size_hint=(None, None))
        self.search_button_pos.add_widget(self.search_button)
        self.add_widget(self.search_button_pos)

        # Run function press button after press OK
        self.search_button.bind(on_press=self.press_button_ok)

        # Define position of label with photo
        self.show_photo_pos = AnchorLayout(anchor_y='center',
                                           anchor_x='right')
        # Default icon in source
        self.show_photo = Image(source='png/database.png',
                                size=(200, 360),
                                size_hint=(None, None))
        self.show_photo_pos.add_widget(self.show_photo)
        self.add_widget(self.show_photo_pos)

        # Define position, size of back button
        self.Anchor_Layout = AnchorLayout(anchor_x='left',
                                          anchor_y='bottom')
        self.button = Button(text='back',
                             size=(100, 100),
                             color=button_text_color,
                             size_hint=(None, None),
                             background_normal="./png/back.png",
                             background_down="./png/back.png",
                             size_hint_x=None)
        self.button.bind(on_release=self.move_direction_choose_window)

        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

    def press_button_t_shirts(self, btn):
        # Function return all names from kind in search_result label
        function_from_database = data_base.get_names_clothes_by_kind('t_shirts')
        self.search_result.text = \
            "[i]Results:[/i] \n{}" .format(function_from_database)

    def press_button_tank_tops(self, btn):
        # Function return all names from kind in search_result label
        function_from_database = data_base.get_names_clothes_by_kind('tank_tops')
        self.search_result.text = \
            "[i]Results:[/i] \n{}" .format(function_from_database)

    def press_button_hoodies(self, btn):
        # Function return all names from kind in search_result label
        function_from_database = data_base.get_names_clothes_by_kind('hoodies')
        self.search_result.text = \
            "[i]Results:[/i] \n{}" .format(function_from_database)

    def press_button_shirts(self, btn):
        # Function return all names from kind in search_result label
        function_from_database = data_base.get_names_clothes_by_kind('shirts')
        self.search_result.text = \
            "[i]Results:[/i] \n{}" .format(function_from_database)

    def press_button_trousers(self, btn):
        # Function return all names from kind in search_result label
        function_from_database = data_base.get_names_clothes_by_kind('trousers')
        self.search_result.text = \
            "[i]Results:[/i] \n{}" .format(function_from_database)

    def press_button_shorts(self, btn):
        # Function return all names from kind in search_result label
        function_from_database = data_base.get_names_clothes_by_kind('shorts')
        self.search_result.text = \
            "[i]Results:[/i] \n{}" .format(function_from_database)

    def press_button_shoes(self, btn):
        # Function return all names from kind in search_result label
        function_from_database = data_base.get_names_clothes_by_kind('shoes')
        self.search_result.text = \
            "[i]Results:[/i] \n{}" .format(function_from_database)

    def press_button_hats(self, btn):
        # Function return all names from kind in search_result label
        function_from_database = data_base.get_names_clothes_by_kind('hats')
        self.search_result.text = \
            "[i]Results:[/i] \n{}" .format(function_from_database)

    def press_button_jackets(self, btn):
        # Function return all names from kind in search_result label
        function_from_database = data_base.get_names_clothes_by_kind('jackets')
        self.search_result.text = \
            "[i]Results:[/i] \n{}" .format(function_from_database)

    def press_button_sunglasses(self, btn):
        # Function return all names from kind in search_result label
        function_from_database = data_base.get_names_clothes_by_kind('sunglasses')
        self.search_result.text = \
            "[i]Results:[/i] \n{}" .format(function_from_database)

    def press_button_necklaces(self, btn):
        # Function return all names from kind in search_result label
        function_from_database = data_base.get_names_clothes_by_kind('necklaces')
        self.search_result.text = \
            "[i]Results:[/i] \n{}" .format(function_from_database)

    def press_button_piercing(self, btn):
        # Function return all names from kind in search_result label
        function_from_database = data_base.get_names_clothes_by_kind('piercing')
        self.search_result.text = \
            "[i]Results:[/i] \n{}" .format(function_from_database)

    def press_button_rings(self, btn):
        # Function return all names from kind in search_result label
        function_from_database = data_base.get_names_clothes_by_kind('rings')
        self.search_result.text = \
            "[i]Results:[/i] \n{}" .format(function_from_database)

    def press_button_bracelets(self, btn):
        # Function return all names from kind in search_result label
        function_from_database = data_base.get_names_clothes_by_kind('bracelets')
        self.search_result.text = \
            "[i]Results:[/i] \n{}" .format(function_from_database)

    def press_button_bags(self, btn):
        # Function return all names from kind in search_result label
        function_from_database = data_base.get_names_clothes_by_kind('bags')
        self.search_result.text = \
            "[i]Results:[/i] \n{}" .format(function_from_database)

    def press_button_gloves(self, btn):
        # Function return all names from kind in search_result label
        function_from_database = data_base.get_names_clothes_by_kind('gloves')
        self.search_result.text = \
            "[i]Results:[/i] \n{}" .format(function_from_database)

    def press_button_scarfs(self, btn):
        # Function return all names from kind in search_result label
        function_from_database = data_base.get_names_clothes_by_kind('scarfs')
        self.search_result.text = \
            "[i]Results:[/i] \n{}" .format(function_from_database)

    def press_button_ok(self, btn):
        # After press kind button print names from choose kind in search_
        # result label

        # Send text after press button OK from input box to function in data
        # base, take data and return in search_result label and photo_source

        # Connect with function print_one_data_by_name form data_base.py
        # Give data from list row, return from  print_one_data_by_name
        function_from_database = \
            data_base.print_one_data_by_name(self.input_box.text)

        # Data for source in show_photo from photo_source in data base
        # for typed data in input_box
        self.show_photo.source = str(function_from_database[5])

        # Data for text in search_result from all columns in data base
        # for typed data in input_box
        # Colors take hex color code from data base and set this code for
        # ███ characters
        self.search_result.text = "[i]Result:[/i] \n" \
                                  "[b]ID:[/b] {}\n" \
                                  "[b]Name:[/b] {}\n" \
                                  "[b]Colors: " \
                                  "[color={}]███ [/color]" \
                                  "[color={}]███ [/color]" \
                                  "[color={}]███[/color][/b] \n" \
                                  "[b]Photo:[/b] {}\n" \
                                  "[b]Description:[/b] {}\n" \
                                  "[b]Exclusions:[/b] {}\n" \
                                  "[b]Clear:[/b] {}\n" \
                                  "[b]Rate:[/b] {}\n" \
                                  "[b]Kind:[/b] {}".format \
            (function_from_database[0],
             function_from_database[1],
             function_from_database[2],
             function_from_database[3],
             function_from_database[4],
             function_from_database[5],
             function_from_database[6],
             function_from_database[7],
             function_from_database[8],
             function_from_database[9],
             function_from_database[10])


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
                             color=button_text_color,
                             size_hint=(None, None),
                             background_normal="./png/back.png",
                             background_down="./png/back.png",
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
                             color=button_text_color,
                             size_hint=(None, None),
                             background_normal="./png/back.png",
                             background_down="./png/back.png",
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
                             color=button_text_color,
                             size_hint=(None, None),
                             background_normal="./png/back.png",
                             background_down="./png/back.png",
                             size_hint_x=None)
        self.button.bind(on_release=self.move_direction_choose_window)

        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

    # Define move after press back button
    def move_direction_choose_window(self, *args):
        self.manager.current = "choosewindow"


class RateClothWindow(Screen):
    def __init__(self, **kwargs):
        super(RateClothWindow, self).__init__(**kwargs)
        self.name = "rateclothwindow"

        # Define position of delete cloth window label
        label_position = AnchorLayout(anchor_x='center',
                                      anchor_y='top')
        label_settings = Label(text='> > > Rate cloth < < <',
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
                             color=button_text_color,
                             size_hint=(None, None),
                             background_normal="./png/back.png",
                             background_down="./png/back.png",
                             size_hint_x=None)
        self.button.bind(on_release=self.move_direction_change_window)

        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

    # Define move after press back button
    def move_direction_change_window(self, *args):
        self.manager.current = "ratewindow"


class RateSetWindow(Screen):
    def __init__(self, **kwargs):
        super(RateSetWindow, self).__init__(**kwargs)
        self.name = "ratesetwindow"

        # Define position of delete cloth window label
        label_position = AnchorLayout(anchor_x='center',
                                      anchor_y='top')
        label_settings = Label(text='> > > Rate set < < <',
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
                             color=button_text_color,
                             size_hint=(None, None),
                             background_normal="./png/back.png",
                             background_down="./png/back.png",
                             size_hint_x=None)
        self.button.bind(on_release=self.move_direction_change_window)

        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

    # Define move after press back button
    def move_direction_change_window(self, *args):
        self.manager.current = "ratewindow"


class HistoryDayWindow(Screen):
    # Rate of set
    # Photo of set
    # Elements of set

    def __init__(self, **kwargs):
        super(HistoryDayWindow, self).__init__(**kwargs)
        self.name = "dayhistorywindow"

        # Define position of photo label
        label_position = AnchorLayout(anchor_x='center',
                                      anchor_y='top')
        label_settings = Label(text='> > > History by day < < <',
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
                             color=button_text_color,
                             size_hint=(None, None),
                             background_normal="./png/back.png",
                             background_down="./png/back.png",
                             size_hint_x=None)
        self.button.bind(on_release=self.move_direction_change_window)

        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

    # Define move after press back button
    def move_direction_change_window(self, *args):
        self.manager.current = "historywindow"


class PhotoWindow(Screen):
    import camera_module

    def __init__(self, **kwargs):
        super(PhotoWindow, self).__init__(**kwargs)
        self.name = "photowindow"

        # Define position of photo window label
        label_position = AnchorLayout(anchor_x='center',
                                      anchor_y='top')
        label_settings = Label(text='> > > Photo < < <',
                               font_size='20sp',
                               size=(200, 50),
                               size_hint=(None, None),
                               color=label_text_color)
        label_position.add_widget(label_settings)
        self.add_widget(label_position)

        # Take camera screen from camera_module.py after press button
        self.Float_Layout = FloatLayout(size=(450, 100))
        self.button = Button(text='Turn on camera',
                             size_hint=(None, None),
                             size=(450, 50),
                             pos=(0, 400),
                             color=button_text_color,
                             background_color=button_background)
        self.button.bind(on_release=self.camera_run)

        self.Float_Layout.add_widget(self.button)
        self.add_widget(self.Float_Layout)

        # Define position, size of back button
        self.Anchor_Layout = AnchorLayout(anchor_x='left',
                                          anchor_y='bottom')
        self.button = Button(text='back',
                             size=(100, 100),
                             color=button_text_color,
                             size_hint=(None, None),
                             background_normal="./png/back.png",
                             background_down="./png/back.png",
                             size_hint_x=None)
        self.button.bind(on_release=self.move_direction_change_window)

        self.Anchor_Layout.add_widget(self.button)
        self.add_widget(self.Anchor_Layout)

    def camera_run(self, *args):
        return self.camera_module.CameraModule().run()

    # Define move after press back button
    def move_direction_change_window(self, *args):
        self.manager.current = "historywindow"


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
                             color=button_text_color,
                             size_hint=(None, None),
                             background_normal="./png/back.png",
                             background_down="./png/back.png",
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
                             color=button_text_color,
                             size_hint=(None, None),
                             background_normal="./png/back.png",
                             background_down="./png/back.png",
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
                             color=button_text_color,
                             size_hint=(None, None),
                             background_normal="./png/back.png",
                             background_down="./png/back.png",
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
                             color=button_text_color,
                             size_hint=(None, None),
                             background_normal="./png/back.png",
                             background_down="./png/back.png",
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

        # For Rate Window
        screen_manager.add_widget(RateClothWindow())
        screen_manager.add_widget(RateSetWindow())

        # For History Window
        screen_manager.add_widget(HistoryDayWindow())
        screen_manager.add_widget(PhotoWindow())

        # For Change Window
        screen_manager.add_widget(AddNewClothWindow())
        screen_manager.add_widget(ChangeClearWindow())
        screen_manager.add_widget(ChangeClearData())
        screen_manager.add_widget(DeleteCloth())

        return screen_manager


MyOrganiser().run()
