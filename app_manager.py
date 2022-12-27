from UI.UI import UI
from src.stochastics_analyzer import StochasticsAnalyzer


class AppManager:
    def __init__(self) -> None:
        self.stochastics_analyzer = StochasticsAnalyzer()
        self.UI = UI()
        print("App Manager started...")
        