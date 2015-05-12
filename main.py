#install_twisted_rector must be called before importing the reactor
from kivy.support import install_twisted_reactor
install_twisted_reactor()
#A simple Client that send messages to the echo server
from twisted.internet import reactor, protocol


class EchoClient(protocol.Protocol):
    def connectionMade(self):
        print "connection"
        self.factory.app.on_connection(self.transport)

    def dataReceived(self, data):
        self.factory.app.print_message(data)


class EchoFactory(protocol.ClientFactory):
    protocol = EchoClient

    def __init__(self, app):
        self.app = app

    def clientConnectionLost(self, conn, reason):
        self.app.print_message("connection lost")

    def clientConnectionFailed(self, conn, reason):
        self.app.print_message("connection failed")

# -*- coding: utf-8 -*-


import kivy
kivy.require('1.8.0')
from kivy.app import App
from kivy.uix.behaviors import DragBehavior
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.uix.screenmanager import *
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
#layout = FloatLayout(size=(300, 300))button1 = Button(text='Hello world',
#size_hint=(.6, .6), pos_hint={'x':.2, 'y':.2})button2 = Button(text='Hello world',
#size_hint=(.3, .2), pos_hint={'x':.3, 'y':.1})layout.add_widget(button1)layout.add_widget(button2)



class ButtonsApp(BoxLayout):
    def __init__(self, **kwargs):
        super(ButtonsApp, self).__init__(**kwargs)

Builder.load_string("""
<ButtonsApp>:
    orientation: "vertical"
    Button:
        text: "B1"
        Image:
            source: '1.png'
            y: self.parent.y + self.parent.height - 250
            x: self.parent.x
            allow_stretch: True
    Label:
        text: "A label"
""")









#######################################
#######################################



#######popup########
class ButtonOptionsPopUp(Popup):
    def __init__(self, caller_screen, **kwargs):
        super(ButtonOptionsPopUp, self).__init__(**kwargs)
        self.caller_screen = caller_screen
        self.size_hint = (None, None)
        self.size = ("200pt", "125pt")
        self.title = "Button Options"
        layout = BoxLayout(orientation="vertical")
        self.textInput = TextInput()
        print "112345678",self.textInput
        self.textInput.font_size = "10pt"
        layout.add_widget(self.textInput)

        layout.add_widget(Button(text="ok", on_press=self.ok_click))
        self.content = layout

    def ok_click(self, btn):
        self.dismiss()
        self.caller_screen.drawing = "toBeTrueSoon"
        print self.textInput.text
        self.caller_screen.key[self.caller_screen.clicked_button_id] = self.textInput.text
        # self.caller_screen.undo(None)














class ButtonNamePopUp(Popup):
    def __init__(self, caller_screen, **kwargs):
        super(ButtonNamePopUp, self).__init__(**kwargs)
        self.caller_screen = caller_screen
        self.size_hint = (None, None)
        self.size = ("200pt", "125pt")
        self.title = "JoyStick Name"
        layout = BoxLayout(orientation="vertical")
        self.textInput = TextInput()
        layout.add_widget(self.textInput)

        layout.add_widget(Button(text="ok", on_press=self.ok_click))
        self.content = layout

    def ok_click(self, btn):
        self.dismiss()
        sm.current = "page1"

        print self.textInput.text
        self.caller_screen.nameZ = self.textInput.text
        print self.caller_screen.nameZ,"bande namz hastam"

        for looper in range (len(self.caller_screen.location)):
            for i in range (len(self.caller_screen.location[looper])):
                f = open("joystick/"+self.caller_screen.nameZ,'a')
                f.write(str(self.caller_screen.location[looper][i])+" ")
                f.close()

            f = open("joystick/"+self.caller_screen.nameZ,'a')
            f.write(str(self.caller_screen.key[looper])+"\n")
            f.close()
        f = open("joystick/joystick_list.txt","a")
        f.write(self.caller_screen.nameZ+"\n")
        sm.current = "page3"
        f.close()












#####################
# keshidane dokme ha ha va ...

class Safhe2(Screen):
    def __init__(self, **kwargs):
        super(Safhe2, self).__init__(**kwargs)
        self.nameZ = "joystick1"
        with self.canvas:
             Rectangle(source = 'joystick.png', size = (Window.width,Window.height))
        self.layout = FloatLayout(size=(300, 300))
        self.key = []
        self.button1 = []
        self.location = []
        self.tolocation = []
        self.x = 0
        self.draw_button()
        self.add_widget(self.layout)
        self.drawing = "true"


    def clear_button(self,bt):
        self.key = []
        self.layout.clear_widgets()
        self.draw_button()
        self.button1 = []
        self.location = []
        self.tolocation = []

    def undo(self,bt):
        i = 0

        if len(self.location)!=0:
            del self.location [-1]
            del self.key [-1]

            self.layout.clear_widgets()
            self.draw_button()

            for x,y,x1,y1 in self.location:
                i = i+1
                thebuttons = Button(background_color =(0.3,0.9,1,0.9),size_hint= (None,None),size = (x1 - x, y1 - y),pos=(x,y), border=(1,1,1,1), text = str(self.key[i-1]))
                self.layout.add_widget(thebuttons)



    def draw_button(self):
        self.nextpage = Button(text = "Previous page",size_hint= (None,None),size = ("75pt","25pt"),on_press = self.next )
        self.save = Button(text = "Save",size_hint= (None,None),pos = ("75pt","0pt"),size = ("75pt","25pt"),on_press = self.saving )
        self.clearbutton = Button(text = "Clear",size_hint= (None,None),pos = ("150pt","0pt"),size = ("75pt","25pt"),on_press = self.clear_button )
        self.Undo = Button(text = "Undo",size_hint= (None,None),pos = ("225pt","0pt"),size = ("75pt","25pt"),on_press = self.undo )
        self.layout.add_widget(self.clearbutton)
        self.layout.add_widget(self.Undo)
        self.layout.add_widget(self.save)
        self.layout.add_widget(self.nextpage)

    def next(self, btn):
        self.draw_button()
        sm.current = "page3"

    def saving(self, btn):
        q = ButtonNamePopUp(self)
        q.open()

    def saved(self):
        self.location.append(100,300,200,300)

    def clear(self):
        i = 0
        self.layout.clear_widgets()
        self.draw_button()

        self.location.append(self.tolocation)

        #print self.tolocation, self.location

        #main buuton

        for x,y,x1,y1 in self.location:
            # print "rastin"
            i = i + 1
            # print "salam aghaye x1 va x","1",x1,"0",x
            # print "salam aghaye y1 va y","1",y1,"0",y
            thebuttons = Button(background_color =(0.3,0.9,1,0.9),size_hint= (None,None),size = (x1 - x, y1 - y)
                                ,pos=(x,y), border=(1,1,1,1), text = str(self.key[i-1]))
            self.layout.add_widget(thebuttons)

        self.tolocation = []
        self.button1 = []


    def on_touch_down(self, touch):
        super(Safhe2, self).on_touch_down(touch)
        q = []
        q.append(touch.x)
        q.append(touch.y)
        # check if its in one of the buttons in self.location

        x, y = touch.x, touch.y
        cntr = 0




        if x>100 and x<200 and y>0 and y<50:
            self.drawing = "saving"
            print "saving"

        for x1,y1,x2,y2 in self.location:
            if (x1<=x<=x2 or x2<=x<=x1) and (y1<=y<=y2 or y2<=y<=y1):
                self.drawing = "options"
                self.clicked_button_id = cntr
                print "Sajad sedasho kam kon ye zarre, ye zarre az ye zarre bishtar"
            cntr += 1




        if not( (touch.x<200 and touch.x>100 and touch.y<50 and touch.y>0) or (touch.x<100 and touch.x>0 and touch.y<50 and touch.y>0)
                or (touch.x<300 and touch.x>200 and touch.y<50 and touch.y>0) or (touch.x<400 and touch.x>300 and touch.y<50 and touch.y>0)):
            self.button1.append(touch.x)
            self.button1.append(touch.y)
            self.tolocation.append(touch.x)
            self.tolocation.append(touch.y)

    def on_touch_move(self, touch):
        super(Safhe2, self).on_touch_move(touch)
        if self.drawing != "true":
            return
        if not( (touch.x<200 and touch.x>100 and touch.y<50 and touch.y>0) or (touch.x<100 and touch.x>0 and touch.y<50 and touch.y>0)
                or (touch.x<300 and touch.x>200 and touch.y<50 and touch.y>0) or (touch.x<400 and touch.x>300 and touch.y<50 and touch.y>0)):

            self.layout.clear_widgets()
            for x,y,x1,y1 in self.location:
                thebuttons = Button(background_color =(0,0.8,0.8,0.4),size_hint= (None,None),size = (x1 - x, y1 - y),pos=(x,y), border=(1,1,1,1))
                self.layout.add_widget(thebuttons)
            self.draw_button()

            self.button1.append(touch.x)
            self.button1.append(touch.y)
            button = Button(background_color =(0,0.8,0.8,0.4),size_hint= (None,None),size = (self.button1[2] - self.button1[0], self.button1[3] - self.button1[1]) , pos_hint={'x':self.button1[0]/Window.width , 'y':self.button1[1]/Window.height}, border=(1,1,1,1))
            self.layout.add_widget(button)

            del self.button1[-1]
            del self.button1[-1]

    def on_touch_up(self, touch):
        super(Safhe2, self).on_touch_up(touch)

        if self.drawing == "options":
            q = ButtonOptionsPopUp(self)
            q.open()
            return


        if not( (touch.x<200 and touch.x>100 and touch.y<50 and touch.y>0) or (touch.x<100 and touch.x>0 and touch.y<50 and touch.y>0)
                or (touch.x<300 and touch.x>200 and touch.y<50 and touch.y>0) or (touch.x<400 and touch.x>300 and touch.y<50 and touch.y>0)):
            self.key.append(-1)
            del self.button1[-1]
            del self.button1[-1]
            self.tolocation.append(touch.x)
            self.tolocation.append(touch.y)
            self.clear()
            #print self.location
        print self.key

        if self.drawing == "toBeTrueSoon":
            print "Salam"
            self.drawing = "true"
            self.undo(None)







class Safhe1(Screen):
    def __init__(self,app, **kwargs):
        super(Safhe1, self).__init__(**kwargs)
        self.joyname = ""
        self.app = app
        self.update()


    def update(self):
        self.clear_widgets()
        a = open("joystick/joystick_list.txt","r")
        p = a.readlines()
        Window.clearcolor = (0.3,0.6,0.7,0)
        self.lay1 = ScrollView()
        self.lay2 = GridLayout(cols=4, padding="10pt", spacing="5pt", size_hint_y= None)
        self.lay2.bind(minimum_height=self.lay2.setter('height'))
        self.lay1.add_widget(self.lay2)
        self.add_widget(self.lay1)

        for i in range(len(p)):
            b = Button(text = p[i],size_hint_y=None, height="200pt" ,on_press = self.next)
            self.lay2.add_widget(b)

        c = Button(background_normal = "creat3.png",size_hint_y=None, height="200pt" ,on_press = self.create)
        self.lay2.add_widget(c)
        a.close()

    def on_enter(self, *args):
        self.update()

    def create(self,btn):
        sm.current = "page2"


    def next(self, btn):
        p3.update()
        print "salam omadam dar next class e safhe1"
       # print namebutton
        self.joyname = btn.text
        sm.page = self
        p4 = Safhe3(self.joyname,self.app,name="page4")
        sm.add_widget(p4)
        sm.current = "page4"






#a = open("joystick/joystick_list.txt","r")



class Safhe3(Screen):
    def __init__(self , joyText,app,**kwargs):
        super(Safhe3, self).__init__(**kwargs)
        self.app = app
        self.joyText = joyText
        self.layout = FloatLayout(size=(3000, 3000))
        with self.canvas:
            Rectangle(source = 'joystick.png', size = (Window.width,Window.height))

        self.add_widget(self.layout)
        self.update()

    def update(self):
        self.layout.clear_widgets()
        self.nextpage = Button(text = "Previous page",size_hint= (None,None),size = (100,50),on_press = self.next )
        self.layout.add_widget(self.nextpage)
        self.joyText2 = self.joyText.split("\n")
        self.joyText = self.joyText2[0]
        a = open("joystick/" + self.joyText.replace("\r",""),"r")
        self.p = a.readlines()
        print "man p hastam ",self.p
        Window.clearcolor = (0.3,0.6,0.7,0)
        print "salam baba golam"
        for looper in range (len(self.p)):
            q = self.p[looper].split(" ")
            print q,"hi"
            for x,y,x1,y1,t in [q]:
                print x,y,x1,y1
                x = int(float(x))
                y = int(float(y))
                x1 = int(float(x1))
                y1 = int(float(y1))
                t = t.split("\n")
                t = t[0]
                thebuttons = Button(background_color =(0.3,0.9,1,0.9),size_hint= (None,None),size = (abs(x1 - x), abs(y1 - y))
                                    ,pos=(x,y), border=(1,1,1,1), text = t , on_press=self.press , on_release = self.release )
                print x1-x, y1-y
                self.layout.add_widget(thebuttons)
        a.close()

    def on_enter(self, *args):
        self.update()


    def next(self, btn):
        sm.current = "page3"

    def press(self,btn):
        self.app.connection.write(btn.text.replace("\n","").replace("\r","") + "$")

    def release(self, btn):
        self.app.connection.write(btn.text.replace("\n","").replace("\r","")+"#UP" + "$")




sm = ScreenManager(transition=FadeTransition())

p3 = None

class CatomapApp(App):
    def build(self):
        global p3
        self.title = "Catomap"
        p2 = Safhe2(name="page2")
        p3 = Safhe1(self,name="page3")

        sm.add_widget(p3)
        sm.add_widget(p2)

        self.connect_to_server()
        return sm

    def connect_to_server(self):
        reactor.connectTCP('192.168.1.126', 8000, EchoFactory(self))

    def on_connection(self, connection):
        self.connection = connection

if __name__ == '__main__':
    CatomapApp().run()
