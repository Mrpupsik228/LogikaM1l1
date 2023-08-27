from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class Myapp(App):
    def build(self):
        
        btn = Button(text = "Download CS2 + Virus")
        btn.on_press = test
        txt = Label(text = "Download CS2 Free Game")
        layout = BoxLayout()
        layout.add_widget(btn)
        layout.add_widget(txt)
        
        return layout

def test ():
    print("hello")    
    
app = Myapp()
app.run()