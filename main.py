#[Kivy        ] v1.9.1
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.size = (600,400)


class MainWindow(Widget):
    pass


class MainWindowApp(App):
    def build(self):
        return MainWindow()


if __name__ == '__main__':
    MainWindowApp().run()
