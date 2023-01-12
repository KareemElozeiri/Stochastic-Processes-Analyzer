import kivy
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.button import Button 
from kivy.uix.filechooser import FileChooserIconView 
from kivy.clock import Clock
from kivy.uix.label import Label 
from kivy.uix.textinput import TextInput



class MainView(GridLayout):
    def __init__(self, app, **kwargs):
        super(MainView, self).__init__(**kwargs)
        self.__app  = app
        self.cols = 2
        self.spacing = 5

        self.__left_section = GridLayout(cols=1)
        self.__left_section.spacing = 3
        self.__right_section = GridLayout(cols=1)
        self.__right_section.spacing = 3

        #left section items
        self.__load_section = GridLayout(cols=1,size_hint_y=None,height=100)
        self.__load_sub_section = GridLayout(cols=2)

        self.__loaded_file_label = Label(text="",font_size="12dp",size_hint_y=None,height=50)
        self.__loaded_file_label.texture_update()
        self.__load_btn = Button(text="Load Signal",size_hint_y=None,height=50,background_color=(0,0,1,1))
        self.__load_btn.on_press = self.__app.switch_to_load_view

        self.__load_sub_section.add_widget(self.__loaded_file_label)
        self.__load_sub_section.add_widget(self.__load_btn)

        self.__load_section.add_widget(Label(text="Add Your Signal",size_hint_y=None, color=(1,0,0,1), height=30))
        self.__load_section.add_widget(self.__load_sub_section)
        self.__left_section.add_widget(self.__load_section)


        self.__time_statistics__section = GridLayout(cols=1)
        self.__time_statistics__section.add_widget(Label(text="Random Process Time Statistics", color=(0,1,0,1)))

        self.__time_mean_section = GridLayout(cols=2)
        self.__time_mean_label = Label(text="Time Mean: ")

        self.__time_mean_section.add_widget(self.__time_mean_label)

        

        self.__time_ACF_section = GridLayout(cols=2)
        self.__time_ACF_label = Label(text="Time ACF: ")

        self.__time_ACF_section.add_widget(self.__time_ACF_label)


        self.__total_average_power_label = Label(text="Total Average Power: ")

        self.__time_statistics__section.add_widget(self.__time_mean_section)
        self.__time_statistics__section.add_widget(self.__time_ACF_section)
        self.__time_statistics__section.add_widget(self.__total_average_power_label)


        self.__left_section.add_widget(self.__time_statistics__section)


        #right section items
        
        #plot m samples section
        self.M_textinput = TextInput(size_hint_y=None,height=50)
        self.__plot_sample_functions = Button(size_hint_y=None,height=75,text="Plot M Sample Functions",background_color=(0,0,1,1))
        self.__plot_sample_functions.on_press = self.plot_m_samples
        plot_sample_function_sec = GridLayout(cols=1,size_hint_y=None,height=150,spacing=0)
        plot_sample_function_sub_sec = GridLayout(size_hint_y=None,height=75,cols=2)
        plot_sample_function_sub_sec.add_widget(Label(size_hint_y=None,height=50,text="Enter M: "))
        plot_sample_function_sub_sec.add_widget(self.M_textinput)
        plot_sample_function_sec.add_widget(plot_sample_function_sub_sec)
        plot_sample_function_sec.add_widget(self.__plot_sample_functions)

        self.__plot_ensemble_mean = Button(size_hint_y=None,height=75,text="Plot Ensemble Mean",background_color=(0,0,1,1))
        self.__plot_ensemble_mean.on_press = self.plot_ensemble_mean_func

        self.__plot_time_mean = Button(size_hint_y=None,height=75,text="Plot Time Mean",background_color=(0,0,1,1))
        self.__plot_time_mean.on_press = self.plot_time_mean_func
        
        self.__plot_statistical_ACF = Button(size_hint_y=None,height=75,text="Plot Statistical ACF",background_color=(0,0,1,1))
        self.__plot_statistical_ACF.on_press = self.plot_stat_ACF_func
        
        self.__plot_PSD = Button(size_hint_y=None,height=75,text="Plot PSD",background_color=(0,0,1,1))


        #title
        self.__right_section.add_widget(Label(size_hint_y=None,height=75,text="Plots"))
        
        self.__right_section.add_widget(plot_sample_function_sec)

        self.__right_section.add_widget(self.__plot_ensemble_mean)
        self.__right_section.add_widget(self.__plot_time_mean)
        self.__right_section.add_widget(self.__plot_statistical_ACF)
        self.__right_section.add_widget(self.__plot_PSD)


        self.add_widget(self.__left_section)
        self.add_widget(self.__right_section)

    def set_loaded_file_txt(self, file_dir):
        self.__loaded_file_label.text = file_dir

    def plot_ensemble_mean_func(self):
        if self.__app.app_manager.stochastics_analyzer != None:
            self.__app.app_manager.stochastics_analyzer.plot_ensemble_mean()
    
    def plot_time_mean_func(self):
        if self.__app.app_manager.stochastics_analyzer != None:
            self.__app.app_manager.stochastics_analyzer.plot_time_mean()
    
    def plot_m_samples(self):
        if self.__app.app_manager.stochastics_analyzer != None:
            m = 0
            try:
                m = int(self.M_textinput.text.strip())
            except:
                self.M_textinput.text="Invalid"
            
            self.__app.app_manager.stochastics_analyzer.plot_M_samples(m)
    
    def plot_stat_ACF_func(self):
        if self.__app.app_manager.stochastics_analyzer != None:
            self.__app.app_manager.stochastics_analyzer.plot_stat_ACF()

    def plot_time_ACF_func(self):
        pass 

    def plot_PSD_func(self):
        pass 

