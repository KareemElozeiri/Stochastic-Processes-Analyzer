from kivy.uix.gridlayout import GridLayout 
from kivy.uix.button import Button 
from kivy.uix.filechooser import FileChooserIconView 
from kivy.clock import Clock
from kivy.uix.label import Label 
from kivy.uix.dropdown import DropDown



class MainView(GridLayout):
    def __init__(self, app, **kwargs):
        super(MainView, self).__init__(**kwargs)
        self.__app  = app
        self.cols = 2

        self.__left_section = GridLayout(cols=1)
        self.__right_section = GridLayout(cols=1)

        #left section items
        self.__load_section = GridLayout(cols=1)
        self.__load_sub_section = GridLayout(cols=2)

        self.__loaded_file_label = Label()
        self.__load_btn = Button(text="Load Signal",background_color=(0,0,1,1))
        self.__load_btn.on_press = self.__app.switch_to_load_view

        self.__load_sub_section.add_widget(self.__loaded_file_label)
        self.__load_sub_section.add_widget(self.__load_btn)

        self.__load_section.add_widget(Label(text="Add Your Signal"))
        self.__load_section.add_widget(self.__load_sub_section)
        self.__left_section.add_widget(self.__load_section)


        self.__time_statistics__section = GridLayout(cols=1)
        self.__time_statistics__section.add_widget(Label(text="Random Process Time Statistics"))

        self.__time_mean_section = GridLayout(cols=2)
        self.__time_mean_label = Label(text="Time Mean: ")
        self.__time_mean_sample_num_dropdown = DropDown()

        self.__time_mean_section.add_widget(self.__time_mean_label)
        self.__time_mean_section.add_widget(self.__time_mean_sample_num_dropdown)

        

        self.__time_ACF_section = GridLayout(cols=2)
        self.__time_ACF_label = Label(text="Time ACF: ")
        self.__time_ACF_sample_num_dropdown =DropDown()

        self.__time_ACF_section.add_widget(self.__time_ACF_label)
        self.__time_ACF_section.add_widget(self.__time_ACF_sample_num_dropdown)


        self.__total_average_power_label = Label(text="Total Average Power: ")

        self.__time_statistics__section.add_widget(self.__time_mean_section)
        self.__time_statistics__section.add_widget(self.__time_ACF_section)
        self.__time_statistics__section.add_widget(self.__total_average_power_label)


        self.__left_section.add_widget(self.__time_statistics__section)


        #right section items
        self.__plot_sample_functions = Button(text="Plot M Sample Functions",background_color=(0,0,1,1))
        self.__plot_ensemble_mean = Button(text="Plot Ensemble Mean",background_color=(0,0,1,1))
        self.__plot_statistical_ACF = Button(text="Plot Statistical ACF",background_color=(0,0,1,1))
        self.__plot_PSD = Button(text="Plot PSD",background_color=(0,0,1,1))



        self.__right_section.add_widget(Label(text="Plots"))
        self.__right_section.add_widget(self.__plot_sample_functions)
        self.__right_section.add_widget(self.__plot_ensemble_mean)
        self.__right_section.add_widget(self.__plot_statistical_ACF)
        self.__right_section.add_widget(self.__plot_PSD)


        self.add_widget(self.__left_section)
        self.add_widget(self.__right_section)

