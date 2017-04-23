from ..base import BaseBot
from sense_hat import SenseHat

class HumidityBot(BaseBot):
    def __init__(self, jid, password, nick, room):
        BaseBot.__init__(self, jid, password, nick, room)
        self.sense = SenseHat()

    def handle_message(self, msg):
        if msg['body'].strip() == '/humidity':
            humid = self.sense.get_humidity()
            resp = "Current relative humidity is %.2f %%" % humid
            self.send_message(mto=msg['from'].bare,
                              mbody=resp,
                              mtype='groupchat')
