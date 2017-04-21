from ..base import BaseBot

class LedBot(BaseBot):
    def __init__(self, jid, password, nick, room):
        BaseBot.__init__(self, jid, password, nick, room)

        trigger_file = open('/sys/class/leds/led0/trigger', 'w')
        trigger_file.write('none')
        trigger_file.close()

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
