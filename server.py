# install_twisted_rector must be called before importing  and using the reactor
from kivy.support import install_twisted_reactor
install_twisted_reactor()
import win32com.client
from twisted.internet import reactor
from twisted.internet import protocol


class EchoProtocol(protocol.Protocol):
    def dataReceived(self, data):
        self.factory.app.handle_message(data)
        


class EchoFactory(protocol.Factory):
    protocol = EchoProtocol

    def __init__(self, app):
        self.app = app


from kivy.app import App
from kivy.uix.label import Label


class TwistedServerApp(App):
    def build(self):
        self.label = Label(text="server started\n")
        reactor.listenTCP(8000, EchoFactory(self))
        return self.label

    def handle_message(self, msg):
        win32com.client.Dispatch("WScript.Shell").SendKeys(msg)


if __name__ == '__main__':
    TwistedServerApp().run()
