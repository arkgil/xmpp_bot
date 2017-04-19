from sleekxmpp import ClientXMPP

class BaseBot(ClientXMPP):
    def __init__(self, jid, password, nick, room):
        ClientXMPP.__init__(self, jid, password)

        self.nick = nick
        self.room = room

        self.register_plugin('xep_0045')

        self.add_event_handler("session_start", self.session_start)
        self.add_event_handler("groupchat_message", self.groupchat_message)


    def session_start(self, event):
        self.get_roster()
        self.send_presence()
        self.plugin['xep_0045'].joinMUC(self.room,
                                        self.nick,
                                        wait=True)
        self.plugin['xep_0045'].configureRoom(room = self.room)

    def groupchat_message(self, msg):
        if msg['mucnick'] != self.nick:
            self.handle_message(msg)
