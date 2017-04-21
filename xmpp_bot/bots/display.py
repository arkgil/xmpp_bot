import re
from ..base import BaseBot
from sense_hat import SenseHat

class DisplayBot(BaseBot):
    def __init__(self, jid, password, nick, room):
        BaseBot.__init__(self, jid, password, nick, room)
        self.sense = SenseHat()
        self.degree = 0

    def handle_message(self, msg):
        split_body = re.split(r'\s+', msg['body'], 2)
        if len(split_body) == 3 and split_body[0] == '/display':
            command = split_body[1]
            args = split_body[2]
            if command == 'show':
                self.display_msg(args)
            elif command == 'rotate':
                self.rotate(args)

    def display_msg(self, msg):
        self.sense.show_message(msg)

    def rotate(self, degree_str):
        try:
            degree = int(degree_str)
            if degree in [0, 90, 180, 270]:
                self.degree = (self.degree + degree) % 360
                self.sense.set_rotation(self.degree)
        except ValueError:
            pass
