import sys
import logging

if sys.version_info < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf8')

sys.path.append("../xmpp_bot")

from xmpp_bot.bots.led import LedBot

logging.basicConfig(level=logging.DEBUG)

server = 'localhost'
port = 5222

if __name__ == '__main__':
    if len(sys.argv) >= 4:
        jid = sys.argv[1]           # led@localhost
        password = sys.argv[2]      # 1234
        room = sys.argv[3]          # test_room@muc.localhost
        if len(sys.argv) >= 5:
            server = sys.argv[4]    # localhost
        if len(sys.argv) >= 6:
            port = sys.argv[5]      # 5222

        xmpp = LedBot(jid, password, "led_bot", room)

        xmpp.connect(address=(server, port))
        xmpp.process(threaded=False)
    else:
        print("Invalid number of arguments.\n" +
              "Usage: python %s <jid> <pass> <room> [host] [port]" % sys.argv[0])
