import kivy
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.button import Button 
from kivy.uix.filechooser import FileChooserIconView 
from kivy.clock import Clock
from kivy.uix.label import Label 
from kivy.uix.textinput import TextInput
import numpy as np 


class MainView(GridLayout):
    def __init__(self, app, **kwargs):
        super(MainView, self).__init__(**kwargs)
        self.__app  = app
        self.cols = 2
        self.spacing = 3
        self.__item_height = 50
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

        stat_ACF_sec = GridLayout(cols=1)
        stat_ACF_sec.add_widget(Label(text="Statistical ACF", color=(0,1,0,1), size_hint_y=None, height=self.__item_height))
        i_sec = GridLayout(cols=2)
        j_sec = GridLayout(cols=2)

        i_sec.add_widget(Label(text="Enter i: ", size_hint_y=None, height=self.__item_height))
        j_sec.add_widget(Label(text="Enter j: ", size_hint_y=None, height=self.__item_height))

        self.__i_textinput = TextInput()
        self.__j_textinput = TextInput()
        
        i_sec.add_widget(self.__i_textinput)
        j_sec.add_widget(self.__j_textinput)

        self.eval_stat_ACF_btn  = Button(text="Evaluate",background_color=(0,0,1,1))
        self.eval_stat_ACF_btn.on_press = self.evaluate_stat_ACF

        self.__stat_ACF_label = Label(text="ACF Value", color=(0,1,1,1))

        stat_ACF_sec.add_widget(i_sec)
        stat_ACF_sec.add_widget(j_sec)
        stat_ACF_sec.add_widget(self.eval_stat_ACF_btn)
        stat_ACF_sec.add_widget(self.__stat_ACF_label)



        self.__time_statistics__section = GridLayout(cols=1)
        self.__time_statistics__section.add_widget(Label(text="Random Process Time Statistics", color=(0,1,0,1)))


        self.__sample_index_textinput = TextInput()
        self.__time_stats_eval_btn = Button(text="Evaluate", size_hint_y=None, height=50, background_color=(0,0,1,1))
        self.__time_stats_eval_btn.on_press = self.eval_time_stats_func
        self.__time_mean_label = Label(text="Time Mean: ")


        

        self.__time_ACF_for_sample_btn = Button(text="Show Time ACF For Sample", size_hint_y=None, height=50, background_color=(0,0,1,1))
        self.__time_ACF_for_sample_btn.on_press = self.show_time_ACF_sample


        self.__total_average_power_label = Label(text="Total Average Power: ")

        sample_index_sec = GridLayout(cols=1, height=100, size_hint_y=None)
        sample_index_sub_sec = GridLayout(cols=2)
        sample_index_sub_sec.add_widget(Label(text="Enter Sample Function Index: "))
        sample_index_sub_sec.add_widget(self.__sample_index_textinput)
        sample_index_sec.add_widget(sample_index_sub_sec)
        sample_index_sec.add_widget(self.__time_stats_eval_btn)
        self.__time_statistics__section.add_widget(sample_index_sec)
        self.__time_statistics__section.add_widget(self.__time_mean_label)
        self.__time_statistics__section.add_widget(self.__time_ACF_for_sample_btn)
        self.__time_statistics__section.add_widget(self.__total_average_power_label)

        self.__left_section.add_widget(stat_ACF_sec)
        self.__left_section.add_widget(self.__time_statistics__section)


        #right section items
        
        #plot m samples section
        self.M_textinput = TextInput(size_hint_y=None,height=50)
        self.__plot_sample_functions = Button(size_hint_y=None,height=self.__item_height,text="Plot M Sample Functions",background_color=(0,0,1,1))
        self.__plot_sample_functions.on_press = self.plot_m_samples
        plot_sample_function_sec = GridLayout(cols=1,size_hint_y=None,height=150,spacing=0)
        plot_sample_function_sub_sec = GridLayout(size_hint_y=None,height=self.__item_height,cols=2)
        plot_sample_function_sub_sec.add_widget(Label(size_hint_y=None,height=50,text="Enter M: "))
        plot_sample_function_sub_sec.add_widget(self.M_textinput)
        plot_sample_function_sec.add_widget(plot_sample_function_sub_sec)
        plot_sample_function_sec.add_widget(self.__plot_sample_functions)
        #plot buttons
        self.__plot_ensemble_mean = Button(size_hint_y=None,height=self.__item_height,text="Plot Ensemble Mean",background_color=(0,0,1,1))
        self.__plot_ensemble_mean.on_press = self.plot_ensemble_mean_func

        self.__plot_time_mean = Button(size_hint_y=None,height=self.__item_height,text="Plot Time Mean",background_color=(0,0,1,1))
        self.__plot_time_mean.on_press = self.plot_time_mean_func
        
        self.__plot_statistical_ACF = Button(size_hint_y=None,height=self.__item_height,text="Plot Statistical ACF",background_color=(0,0,1,1))
        self.__plot_statistical_ACF.on_press = self.plot_stat_ACF_func

        
        
        self.__plot_PSD = Button(size_hint_y=None,height=self.__item_height,text="Plot PSD",background_color=(0,0,1,1))
        self.__plot_PSD.on_press = self.plot_PSD_func

        #title
        self.__right_section.add_widget(Label(size_hint_y=None,height=self.__item_height,text="Plots"))
        
        self.__right_section.add_widget(plot_sample_function_sec)
        self.__right_section.add_widget(self.__plot_ensemble_mean)
        self.__right_section.add_widget(self.__plot_time_mean)
        self.__right_section.add_widget(self.__plot_statistical_ACF)
        self.__right_section.add_widget(self.__plot_PSD)


        self.add_widget(self.__left_section)
        self.add_widget(self.__right_section)
    
    def set_total_average_power_label_text(self,text):
        self.__total_average_power_label.text = text 

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

            if m==0:
                self.M_textinput.text="Invalid"
                return
            
            self.__app.app_manager.stochastics_analyzer.plot_M_samples(m)
    
    def plot_stat_ACF_func(self):
        if self.__app.app_manager.stochastics_analyzer != None:
            self.__app.app_manager.stochastics_analyzer.plot_stat_ACF()

 
    def plot_PSD_func(self):
        if self.__app.app_manager.stochastics_analyzer != None:
            self.__app.app_manager.stochastics_analyzer.plot_PSD()

    def eval_time_stats_func(self):
        if self.__app.app_manager.stochastics_analyzer != None:
            try:
                n = int(self.__sample_index_textinput.text.strip())
                time_mean = np.round(self.__app.app_manager.stochastics_analyzer.calc_time_mean(n),3)

                self.__time_mean_label.text = f"Time Mean: {time_mean}"
            except:
                self.__sample_index_textinput.text = "Invalid"

    
    def show_time_ACF_sample(self):
        if self.__app.app_manager.stochastics_analyzer != None:
            try:
                n = int(self.__sample_index_textinput.text.strip())
                self.__app.app_manager.stochastics_analyzer.plot_time_ACF_for_sample(n)
            except:
                self.__sample_index_textinput.text = "Invalid"
    
    def evaluate_stat_ACF(self):
        if self.__app.app_manager.stochastics_analyzer != None:
            try:
                i = int(self.__i_textinput.text.strip())
                j = int(self.__j_textinput.text.strip())

                ACF_Value = self.__app.app_manager.stochastics_analyzer.calc_ACF(i,j)
                ACF_Value = np.round(ACF_Value, 3)
                self.__stat_ACF_label.text = f"Statistical ACF Value: {ACF_Value}"

            except:
                self.__i_textinput.text = "Invalid"
                self.__j_textinput.text = "Invalid"

