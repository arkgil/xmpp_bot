from serial import Serial
import logging
import re
import sys

from sleekxmpp import ClientXMPP
from sleekxmpp.xmlstream import ET

class DashboardController(ClientXMPP):
    def __init__(self, jid, password, pubsub_server):
        ClientXMPP.__init__(self, jid, password)

        self.serial = Serial('/dev/ttyS0', 38400, timeout=1)

        self.node = 'copernicus_dashboard'
        self.pubsub_server = pubsub_server

        self.register_plugin('xep_0030')
        self.register_plugin('xep_0059')
        self.register_plugin('xep_0060')

        self.add_event_handler("session_start", self.session_start)
        self.add_event_handler('pubsub_publish', self.handle_publish)


    def session_start(self, event):
        self.get_roster()
        self.send_presence()
        self.create_pubsub_node()
        self.subscribe()
        logging.info("Finished initialization")

    def handle_publish(self, msg):
        data = msg['pubsub_event']['items']['item']['payload']
        if data is not None:
            logging.info("Received data from pubsub: %s" % ET.tostring(data))
            try:
                ## Yes, parsing xml with regex.... No idea how to handle custom elements
                ## with sleekxmpp
                m = re.match(r".*?>(\d+?)</.*", ET.tostring(data))
                angle = int(m.group(1))
                logging.info("Setting dashboard angle to: %d" % angle)
                self.set_dashboard(angle)
            except:
                logging.error("Unexpected error: %s" % sys.exc_info()[0])
                logging.error("Failed to set dashboard angle")

    def create_pubsub_node(self):
        try:
            self['xep_0060'].create_node(self.pubsub_server, self.node)
            logging.info("Created pubsub node: %s" % self.node)
        except:
            logging.error("Couldn't create pubsub node: %s" % self.node)

    def subscribe(self):
        try:
            result = self['xep_0060'].subscribe(self.pubsub_server, self.node)
            logging.info('Subscribed to node %s' % self.node)
        except:
            logging.error('Couldn\'t subscribe %s to node %s' % (self.boundjid.bare, self.node))

    def set_dashboard(self, angle):
        ser.write(chr(angle))
