import os
os.environ['KIVY_IMAGE'] = 'pil'
import kivy
from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen 
from UI.views.main_view import MainView
from UI.views.load_view import LoadView
from kivy.core.window import Window 



class UI(App):
    def __init__(self, app_manager, **kwargs):
        super(UI, self).__init__(**kwargs)
        self.title = "Stochastics"
        self.app_manager = app_manager
    

    def build(self):
        self.screen_manager =ScreenManager()

        #main view
        self.main_view = MainView(self)
        screen0 = Screen(name="main")
        screen0.add_widget(self.main_view)
        self.screen_manager.add_widget(screen0)
        #load view 
        self.load_view = LoadView(self)
        screen1 = Screen(name="load")
        screen1.add_widget(self.load_view)
        self.screen_manager.add_widget(screen1)

        return self.screen_manager


    #screen switching functions
    def switch_to_load_view(self, dt=0):
        self.screen_manager.current = "load"
    
    def switch_to_main_view(self, dt=0):
        self.screen_manager.current = "main"


    