#Kivy v1.9.1
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

Window.size = (400,650)


class MainWindow(Screen):
    pass

class Button1(Screen):
    pass

class Button2(Screen):
    pass

class Button3(Screen):
    pass

class Button4(Screen):
    pass

#control move between screens
screen_manager = ScreenManager()

#define all screens of app
screen_manager.add_widget(MainWindow(name='MainWindow'))
screen_manager.add_widget(Button1(name='Button1'))
screen_manager.add_widget(Button2(name='Button2'))
screen_manager.add_widget(Button3(name='Button3'))
screen_manager.add_widget(Button4(name='Button4'))

class MainWindowApp(App):
    def build(self):
        return screen_manager

if __name__ == '__main__':
    MainWindowApp().run()

