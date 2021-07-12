from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel

class NavMenu(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__()
        self.orientation = "vertical"
        self.padding = "8dp"
        self.spacing ="8dp"
        self.add_widget(MDLabel(text="Menu list",halign="center"))