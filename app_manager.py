from UI.UI import UI
from src.stochastics_analyzer import StochasticsAnalyzer
import numpy as np 

class AppManager:
    def __init__(self) -> None:
        self.stochastics_analyzer = None
        self.UI = UI(self)
        self.loaded_file = ""
        print("App Manager started...")
    

    def set_loaded_file(self, file_dir):
        self.loaded_file = file_dir
        T_S = np.loadtxt(open(file_dir, "rb"), delimiter=",")
        time = T_S[0]
        signal = T_S[1:]
        self.stochastics_analyzer = StochasticsAnalyzer(time, signal)

    def run(self):
        self.UI.run()
        