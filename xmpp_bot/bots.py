from base import BaseBot

class PingBot(BaseBot):
    def __init__(self, jid, password, nick, room):
        BaseBot.__init__(self, jid, password, nick, room)

    def handle_message(self, msg):
        if msg['body'] == '/ping' or msg['body'].startswith('/ping '):
            self.send_message(mto=msg['from'].bare,
                              mbody='pong',
                              mtype='groupchat')
