import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class Yuva_HariGrid(GridLayout):
    def __init__(self, **kwargs):
        super(Yuva_HariGrid, self).__init__()
        self.cols = 2
        self.add_widget(Label(text="Student name:"))
        self.S_name = TextInput()
        self.add_widget(self.S_name)
        self.add_widget(Label(text="Student marks:"))
        self.S_marks = TextInput()
        self.add_widget(self.S_marks)
        self.add_widget(Label(text="Student Gender:"))
        self.S_gender = TextInput()
        self.add_widget(self.S_gender)
        self.press = Button(text="SUBMIT")
        self.press.bind(on_press = self.click_me)
        self.add_widget(self.press)

    def click_me(self, instance):
        print("Student Name: "+self.S_name.text)
        print("Student Marks: "+self.S_marks.text)
        print("Student Gender: "+self.S_gender.text)
        
class Yuva_HariApp(App):
    def build(self):
        return Yuva_HariGrid()
    
if __name__ == "__main__":
    Yuva_HariApp().run()