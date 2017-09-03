import kivy
kivy.require("1.10.0")

from kivy.app import App
from kivy.config import Config
from kivy.graphics import *
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout


class CGraphicsMenu(BoxLayout):
    pass

class CGraphicsApp(App):
    
    def build(self):
        return CGraphicsMenu()

# def dda(self):
#     pass

# def bresenham(self):
#     pass

# def parametric(self):
#     pass

cgApp = CGraphicsApp()
cgApp.run()