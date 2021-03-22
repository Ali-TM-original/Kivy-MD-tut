from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (300, 500)
Builder.load_file("main.kv")


class Mylayout(Widget):

    def clear(self):
        self.ids.input_bar.text = "0"


class Calculator(App):
    def build(self):
        return Mylayout()


if __name__ == "__main__":
    Calculator().run()
