from kivy.app import App
from kivy.lang import Builder


class HelloWorldApp(App):
    def build(self):
        return Builder.load_file('main.kv')
    
HelloWorldApp().run()    

#A label make text appear on the screen
#A button has a customizable thing that shows certan behavior.
#Text input is where your user will put in text
#hint_text allows for you to put something in the box where some one is typing that disappers when typed in. Ex: "Your name"
#An Id is a key for information in diffrent section/page
#Progresss bar allows you to make a visable progress bar
#Oreintation allows you organize your screen
#Image allows you import images.
#Streatch allows you to make imgaes lareger or smaller
#keep ration allows you to keep the same ratio of the img while streaching and deacreasing the img.
