from serial import Serial
import logging

from ..base import BaseBot

from sleekxmpp.xmlstream import ET

class DashboardBot(BaseBot):
    def __init__(self, jid, password, nick, room, pubsub_server):
        BaseBot.__init__(self, jid, password, nick, room)

        self.register_plugin('xep_0030')
        self.register_plugin('xep_0059')
        self.register_plugin('xep_0060')

        self.node = 'copernicus_dashboard'
        self.pubsub_server = pubsub_server


    def handle_message(self, msg):
        split_body = msg['body'].split()
        if len(split_body) >= 2 and split_body[0] == '/dashboard':
            angle = int(split_body[1])
            if angle >= 0 and angle <= 32:
                resp = "Setting dashboard angle to %d" % angle
                self.publish(angle)
            else:
                resp = "Invalid argument. Angle must be between 0 and 32"
            logging.info("Sent: " + resp)
            self.send_message(mto=msg['from'].bare,
                              mbody=resp,
                              mtype='groupchat')

    def publish(self, angle):
        payload = ET.fromstring("<angle xmlns='angle'>%d</angle>" % angle)
        try:
            result = self['xep_0060'].publish(self.pubsub_server, self.node, payload=payload)
            id = result['pubsub']['publish']['item']['id']
            logging.info('Published at item id: %s' % id)
        except:
            logging.error('Could not publish to: %s' % self.node)
