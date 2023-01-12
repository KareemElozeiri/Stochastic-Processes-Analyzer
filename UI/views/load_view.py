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
        self.__file_chooser.path = "."
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
    
    #load functions
    def load_action(self):
        if len(self.__file_chooser.selection)!=0:
            if self.__file_chooser.selection[0][-4:] !=".csv":
                self.add_status_bar_msg("Invalid file: .csv extension is the only type allowed")
            else:
                self.__app.app_manager.set_loaded_file(self.__file_chooser.selection[0])
                self.__app.main_view.set_loaded_file_txt(self.__file_chooser.selection[0])
                self.__app.switch_to_main_view()
        else:
            self.add_status_bar_msg("")


    # status bar functions
    def empty_status_bar(self,dt):
        self.__status_bar.text = ""

    def add_status_bar_msg(self, msg:str):
        self.__status_bar.text = msg 
        Clock.schedule_once(self.empty_status_bar,2) 