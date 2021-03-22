from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDRaisedButton
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from builderstr import builderstr


class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        self.title = 'Learning Kivy'
        self.theme_cls.primary_palette = "Green"
        button = MDRectangleFlatButton(text="Proceed", pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                       on_release=self.show_data)
        self.username = Builder.load_string(builderstr)
        screen.add_widget(self.username)
        screen.add_widget(button)
        return screen

    def show_data(self, obj):
        if self.username.text == '':
            pass
        else:
            close = MDRaisedButton(text="Close", on_release=self.close_dialoge)
            More = MDRaisedButton(text="More")
            self.dialog = MDDialog(title="Corrent?",
                                   text=self.username.text,
                                   size_hint=(0.5, 0.5),
                                   buttons=[close, More])
            self.dialog.open()

    def close_dialoge(self, obj):
        self.dialog.dismiss()


if __name__ == "__main__":
    DemoApp().run()
