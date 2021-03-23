from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (300, 500)
Builder.load_file("main.kv")


class Mylayout(Widget):

    def clear(self):
        self.ids.input_bar.text = "0"

    def button_press(self, num):
        prior = self.ids.input_bar.text

        if prior == '0':
            self.ids.input_bar.text = ''
            self.ids.input_bar.text = f"{num}"
        else:
            self.ids.input_bar.text = f"{prior}{num}"

    def add(self):
        prior = self.ids.input_bar.text

        self.ids.input_bar.text = f"{prior}+"

    def subtraction(self):
        prior = self.ids.input_bar.text

        self.ids.input_bar.text = f"{prior}-"

    def multiplication(self):
        prior = self.ids.input_bar.text

        self.ids.input_bar.text = f"{prior}*"

    def division(self):
        prior = self.ids.input_bar.text

        self.ids.input_bar.text = f"{prior}/"

    def evaluate(self):
        prior = self.ids.input_bar.text

        if prior == '0':
            pass
        else:
            try:
                x = eval(prior)
                self.ids.input_bar.text = f"{x}"
            except ZeroDivisionError:
                self.ids.input_bar.text = '0'
            except SyntaxError:
                self.ids.input_bar.text = '0'

    def decimal(self):
        prior = self.ids.input_bar.text
        self.ids.input_bar.text = f"{prior}."

    def percent(self):
        prior = self.ids.input_bar.text

        if prior == "0":
            pass
        else:
            prior = f'{prior}/100'
            x = eval(prior)
            self.ids.input_bar.text = f"{x}"

    def negatize(self):
        prior = self.ids.input_bar.text

        if prior == "0":
            pass
        else:
            self.ids.input_bar.text = f"-{prior}"

    def test_delete(self):
        prior = self.ids.input_bar.text

        if prior == "0":
            pass
        else:
            prior = prior[:-1]
            self.ids.input_bar.text = f'{prior}'


class Calculator(App):
    def build(self):
        return Mylayout()


if __name__ == "__main__":
    Calculator().run()
