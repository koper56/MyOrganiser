from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.core.window import Window

Window.size = (400,650)


class MainWindow(FloatLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)

        # Main Label
        label_position = AnchorLayout(anchor_x='center',
                                      anchor_y='top')
        label_settings = Label(text='> > > MyOrganiser MainWindow < < <',
                               size=(200, 50),
                               size_hint=(None, None))
        label_position.add_widget(label_settings)
        self.add_widget(label_position)

        # Main Menu button 1
        button_position = AnchorLayout(anchor_x='left',
                                       anchor_y='center')
        button_settings = Button(text='button1',
                                 size=(200, 200),
                                 size_hint=(None, None))
        button_position.add_widget(button_settings)
        self.add_widget(button_position)

        # Main Menu button 2
        button_position = AnchorLayout(anchor_x='right',
                                       anchor_y='center')
        button_settings = Button(text='button2',
                                 size=(200, 200),
                                 size_hint=(None, None))
        button_position.add_widget(button_settings)
        self.add_widget(button_position)

        # Main Menu button 3
        button_position = AnchorLayout(anchor_x='left',
                                       anchor_y='bottom')
        button_settings = Button(text='button3',
                                 size=(200, 200),
                                 size_hint=(None, None))
        button_position.add_widget(button_settings)
        self.add_widget(button_position)

        # Main Menu button 4
        button_position = AnchorLayout(anchor_x='right',
                                       anchor_y='bottom')
        button_settings = Button(text='button4',
                                 size=(200, 200),
                                 size_hint=(None, None))
        button_position.add_widget(button_settings)
        self.add_widget(button_position)


class Button1(FloatLayout):
    def __init__(self, **kwargs):
        super(Button1, self).__init__(**kwargs)

        # Window Button1 Label
        label_position = AnchorLayout(anchor_x='center',
                                      anchor_y='top')
        label_settings = Label(text='> > > MyOrganiser Button1 < < <',
                               size=(200, 50),
                               size_hint=(None, None))
        label_position.add_widget(label_settings)
        self.add_widget(label_position)

        # back button for Button1 window
        button_position = AnchorLayout(anchor_x='left',
                                       anchor_y='bottom')
        button_settings = Button(text='back',
                                 size=(100, 50),
                                 size_hint=(None, None))
        button_position.add_widget(button_settings)
        self.add_widget(button_position)


class Button2(FloatLayout):
    def __init__(self, **kwargs):
        super(Button2, self).__init__(**kwargs)

        # Window Button2 Label
        label_position = AnchorLayout(anchor_x='center',
                                      anchor_y='top')
        label_settings = Label(text='> > > MyOrganiser Button2 < < <',
                               size=(200, 50),
                               size_hint=(None, None))
        label_position.add_widget(label_settings)
        self.add_widget(label_position)

        # back button for Button2 window
        button_position = AnchorLayout(anchor_x='left',
                                       anchor_y='bottom')
        button_settings = Button(text='back',
                                 size=(100, 50),
                                 size_hint=(None, None))
        button_position.add_widget(button_settings)
        self.add_widget(button_position)


class Button3(FloatLayout):
    def __init__(self, **kwargs):
        super(Button3, self).__init__(**kwargs)

        # Window Button3 Label
        label_position = AnchorLayout(anchor_x='center',
                                      anchor_y='top')
        label_settings = Label(text='> > > MyOrganiser Button3 < < <',
                               size=(200, 50),
                               size_hint=(None, None))
        label_position.add_widget(label_settings)
        self.add_widget(label_position)

        # back button for Button3 window
        button_position = AnchorLayout(anchor_x='left',
                                       anchor_y='bottom')
        button_settings = Button(text='back',
                                 size=(100, 50),
                                 size_hint=(None, None))
        button_position.add_widget(button_settings)
        self.add_widget(button_position)


class Button4(FloatLayout):
    def __init__(self, **kwargs):
        super(Button4, self).__init__(**kwargs)

        # Window Button4 Label
        label_position = AnchorLayout(anchor_x='center',
                                      anchor_y='top')
        label_settings = Label(text='> > > MyOrganiser Button4 < < <',
                               size=(200, 50),
                               size_hint=(None, None))
        label_position.add_widget(label_settings)
        self.add_widget(label_position)

        # back button for Button4 window
        button_position = AnchorLayout(anchor_x='left',
                                       anchor_y='bottom')
        button_settings = Button(text='back',
                                 size=(100, 50),
                                 size_hint=(None, None))
        button_position.add_widget(button_settings)
        self.add_widget(button_position)


class MyOrganiser(App):
    def build(self):
        return MainWindow()

if __name__ == '__main__':
    MyOrganiser().run()
