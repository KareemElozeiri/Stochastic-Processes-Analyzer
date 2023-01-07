from kivy.uix.gridlayout import GridLayout 
from kivy.uix.button import Button 
from kivy.uix.filechooser import FileChooserIconView 
from kivy.clock import Clock
from kivy.uix.label import Label 


class LoadView(GridLayout):
    def __init__(self, app, **kwargs):
        super(LoadView, self).__init__(**kwargs)
        self.__app = app 
        self.cols = 1

        #file chooser
        self.__file_chooser = FileChooserIconView()
        self.add_widget(self.__file_chooser)

        subgrid0 = GridLayout(cols=2,size_hint_y=None,height=50)

        #load button 
        self.__load_btn = Button(text="Load")
        self.__load_btn.on_press = self.load_action
        self.__load_btn.background_color = (0,0,1,0.5)

        subgrid0.add_widget(self.__load_btn)
        #cancel button
        self.__cancel_btn = Button(text="Cancel")
        self.__cancel_btn.on_press = self.cancel_action
        self.__cancel_btn.background_color = (1,0,0,0.5)
        subgrid0.add_widget(self.__cancel_btn)

        self.add_widget(subgrid0)
        self.__status_bar = Label(size_hint_y=None, height=80)
        self.add_widget(self.__status_bar)
    
    def cancel_action(self):
        Clock.schedule_once(self.__app.switch_to_main_view,0.5)
    
    def load_action(self):
        if len(self.file_chooser.selection)!=0:
            #TODO: to be modified to suit tha application'
            pass 
    def empty_status_bar(self,dt):
        self.__status_bar.text = ""

    def add_status_bar_msg(self, msg:str):
        self.__status_bar.text = msg 
        Clock.schedule_once(self.empty_status_bar,2) 