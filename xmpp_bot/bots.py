from base import BaseBot
from subprocess import call

class PingBot(BaseBot):
    def __init__(self, jid, password, nick, room):
        BaseBot.__init__(self, jid, password, nick, room)

    def handle_message(self, msg):
        if msg['body'].strip() == '/ping':
            self.send_message(mto=msg['from'].bare,
                              mbody='pong',
                              mtype='groupchat')

class LedBot(BaseBot):
    def __init__(self, jid, password, nick, room):
        BaseBot.__init__(self, jid, password, nick, room)
        self.led_path = '/sys/class/leds/led0/brightness'
        led_file = open(self.led_path, 'r')
        self.led_state = int(led_file.read())
        led_file.close()

    def handle_message(self, msg):
        body = msg['body'].strip()
        if body == '/ledon':
            print('LED ON')
            self.led_state = 1
            self.__update_led()
        elif body == '/ledoff':
            print('LED OFF')
            self.led_state = 0
            self.__update_led()
        elif body == '/ledtoggle':
            print('LED TOGGLE')
            self.led_state = int(not self.led_state)
            self.__update_led()


    def __update_led(self):
        led_file = open(self.led_path, 'w')
        led_file.write(str(self.led_state))
        led_file.close()
