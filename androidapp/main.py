from kivy.app import App
import json
from kivy.graphics.instructions import Canvas
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget

#####API libraries#############"
import requests

class Mygrid(GridLayout):
    def __init__(self, **kwargs):
        super(Mygrid,self).__init__(**kwargs)

        self.inside = GridLayout(spacing = 50, size_hint_y=None, padding = (10,10))
        self.banner = GridLayout(spacing = 4,size_hint_y = 0.1, padding = (1,1))
        self.serchbar=GridLayout(spacing = 4,size_hint_y = 0.1, padding = (1,1))



        self.inside.cols = 4
        self.banner.cols = 4
        self.serchbar.cols = 8
        # self.inside.height = self.minimum_height
        self.cols = 1
        # self.rows = 9
        self.inside.bind(minimum_height=self.inside.setter('height'))
        self.banner.add_widget(Label(text = 'id'))
        self.banner.add_widget(Label(text = 'First Name'))
        self.banner.add_widget(Label(text = 'Last Name'))
        self.banner.add_widget(Label(text = 'Birthdate'))


        self.get_rows(self.cols)
        self.insidescr = ScrollView(size_hint=(1, 1), size=(Window.width, Window.height))
        self.insidescr.add_widget(self.inside)
        self.add_widget(self.banner)
        self.add_widget(self.insidescr)

        # self.get = Button (text = "get from API", font_size = 20, padding = (10,10))
        # self.get.bind(on_press = self.press)
        # self.add_widget(self.get )


    def press(self, instance):
        base = "http://127.0.0.1:5000/"
        ScreenManager.current = 'Add Entry'
        result =requests.get(base + "apidan/user/50" )
        print( result.json())

    def get_rows(self,instance):
        base = "http://127.0.0.1:5000/"
        result = requests.get(base + "apidan")
        employees = result.json()['result']
        print(employees[0]['id'])
        fontsize = 15
        for i in range(50):
            self.inside.add_widget(Label(text=str(employees[i]['id']), font_size=fontsize))
            self.inside.add_widget(Label(text=employees[i]['prenom'],font_size = fontsize))
            self.inside.add_widget(Label(text=employees[i]['nom'], font_size = fontsize))
            self.inside.add_widget(Label(text= str (employees[i]['birthdate']) , font_size = fontsize))



class NewEntry(GridLayout):
    def __init__(self, **kwargs):
        super(NewEntry,self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='id'))
        self.id = TextInput(multiline = False)
        self.add_widget(self.id)
        self.add_widget(Label(text='First Name'))
        self.first_name = TextInput(multiline=False)
        self.add_widget(self.first_name)
        self.add_widget(Label(text='Last Name'))
        self.last_name = TextInput(multiline=False)
        self.add_widget(self.last_name)
        self.add_widget(Label(text='Birthdate'))
        self.birthdate= TextInput(multiline=False)
        self.add_widget(self.birthdate)



class ListScreen(Screen):
    def __init__(self, **kwargs):
        super(ListScreen,self).__init__(**kwargs)
        self.grid = Mygrid()
        self.add_widget(self.grid)
        self.get = Button(text="get from API", font_size=20, padding=(10, 10))
        self.get.bind(on_press=self.press)
        self.grid.add_widget(self.get)

    def press(self, instance):
        self.manager.current = 'Add Entry'

class AddScreen(Screen):
    def __init__(self, **kwargs):
        super(AddScreen,self).__init__(**kwargs)
        self.grid = NewEntry()
        self.add_widget(self.grid)



class MainWidget(Widget):
    pass

class JobseekerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(AddScreen(name="Add Entry"))
        sm.add_widget(ListScreen(name = 'listScreen'))

        sm.current = 'listScreen'

        return sm

class CanvasExample1(Widget):
    pass

if __name__ == "__main__":
    # test = requests()
    JobseekerApp().run()
