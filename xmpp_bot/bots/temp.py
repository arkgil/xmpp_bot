from ..base import BaseBot
from sense_hat import SenseHat

class TempBot(BaseBot):
    def __init__(self, jid, password, nick, room):
        BaseBot.__init__(self, jid, password, nick, room)
        self.sense = SenseHat()

    def handle_message(self, msg):
        if msg['body'].strip() == '/temp':
            temp = self.sense.get_temperature()
            resp = "Current temperature is %.2f C" % temp
            self.send_message(mto=msg['from'].bare,
                              mbody=resp,
                              mtype='groupchat')
