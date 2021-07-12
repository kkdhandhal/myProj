import json

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.navigationdrawer import MDNavigationDrawer,MDNavigationLayout,ScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
import requests


class MainGUI(MDBoxLayout):

    def ConnectMongoDBServer(self):
        firebase_url="https://sherp-bc544-default-rtdb.firebaseio.com/.json"
        json_data = {"name":"Surendranagar Circle","code":510}
        res=requests.patch(url=firebase_url, json=json.dumps(json_data))
        print(res)
        firebaseConfig = {
            "apiKey": "AIzaSyBYM_4EROM1iyG6x-YyjHOz5REohZtl_vY",
            "authDomain": "sherp-bc544.firebaseapp.com",
            "databaseURL": "https://sherp-bc544-default-rtdb.firebaseio.com/",
            "projectId": "sherp-bc544",
            "storageBucket": "sherp-bc544.appspot.com",
            "messagingSenderId": "971654757380",
            "appId": "1:971654757380:web:7435730fbe783dab2a8951",
            "measurementId": "G-YEYVNJQ2L8"
        }


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.adaptive_width = False
        #####   ToolBar Code Start
        self.ToolBar = MDToolbar()
        self.ToolBar.title =" IT Application"
        self.ToolBar.elevation =15
        self.ToolBar.height = 40
        self.ToolBar.left_action_items =[["menu", lambda x: self.nav.set_state("open")]]
        self.ToolBar.md_bg_color = [0.1,0.5,0.6,0.8]

        ###### ToolBar code end

        #### Screen1  Code Start
        self.Screen1 = MDScreen()
        self.Screen1.add_widget(MDLabel(text=self.ConnectMongoDBServer(), halign="center"))
        #### Screen1  Code End


        #### ScreenManager Layout Code Start
        self.ScrnMgr = ScreenManager()
        self.ScrnMgr.add_widget(self.Screen1)
        #### ScreenManager Layout Code End

        #### Navigation Code Start
        self.nav = MDNavigationDrawer()

        #### Navigation Code end

        #### Navigation Layout Code Start
        self.NavLayout = MDNavigationLayout()
        self.NavLayout.add_widget(self.ScrnMgr)
        self.NavLayout.add_widget(self.nav)
        #### Navigation Layout Code End

        self.add_widget(self.ToolBar)
        self.add_widget(self.NavLayout)

class MainApp(MDApp):
    def build(self):
        return MainGUI()


if __name__ == "__main__":
    Window.maximize()
    MainApp().run()
