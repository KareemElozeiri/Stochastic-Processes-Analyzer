from kivy.uix.gridlayout import GridLayout 
from kivy.uix.button import Button 
from kivy.uix.filechooser import FileChooserIconView 
from kivy.clock import Clock
from kivy.uix.label import Label 


class MainView(GridLayout):
    def __init__(self, app, **kwargs):
        super(MainView, self).__init__(**kwargs)
        self.__app  = app
