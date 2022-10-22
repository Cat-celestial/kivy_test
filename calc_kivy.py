from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget


class BoxApp(App):
    def count_eval(self, ins):
        self.lbl.text = str(eval(self.lbl.text))

    def update_label(self):
        self.lbl.text = self.formula

    def number_b_click(self, ins):
        if self.formula == "0":
            self.formula = ""

        self.formula += str(ins.text)
        self.update_label()

    def operation_click(self, ins):
        if str(ins.text).lower() == "x":
            self.formula += "*"
        else:
            self.formula += str(ins.text)
        self.update_label()

    def build(self):
        self.formula = "0"
        bl = BoxLayout(orientation="vertical", padding=25)
        gl = GridLayout(cols=4, spacing=4, size_hint=(1, .6))

        self.lbl = Label(text="0", font_size=40, valign="center", halign="right", size_hint=(1, .4), text_size=(400 - 50, 500 * 0.4 - 50))
        bl.add_widget(self.lbl)

        gl.add_widget(Button(text="7", font_size='20', on_press=self.number_b_click))
        gl.add_widget(Button(text="8", font_size='20', on_press=self.number_b_click))
        gl.add_widget(Button(text="9", font_size='20', on_press=self.number_b_click))
        gl.add_widget(Button(text="x", font_size='25', on_press=self.operation_click))

        gl.add_widget(Button(text="4", font_size='20', on_press=self.number_b_click))
        gl.add_widget(Button(text="5", font_size='20', on_press=self.number_b_click))
        gl.add_widget(Button(text="6", font_size='20', on_press=self.number_b_click))
        gl.add_widget(Button(text="-", font_size='35', on_press=self.operation_click))

        gl.add_widget(Button(text="1", font_size='20', on_press=self.number_b_click))
        gl.add_widget(Button(text="2", font_size='20', on_press=self.number_b_click))
        gl.add_widget(Button(text="3", font_size='20', on_press=self.number_b_click))
        gl.add_widget(Button(text="+", font_size='25', on_press=self.operation_click))

        gl.add_widget(Widget())
        gl.add_widget(Button(text="0", font_size='20', on_press=self.operation_click))
        gl.add_widget(Button(text=".", font_size='35', on_press=self.operation_click))
        gl.add_widget(Button(text="=", font_size='30', on_press=self.count_eval))

        bl.add_widget(gl)
        return bl


if __name__ == "__main__":
    from kivy.core.window import Window
    Window.size = (400, 500)
    BoxApp().run()

