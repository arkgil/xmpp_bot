import sys
import logging

if sys.version_info < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf8')

sys.path.append("../xmpp_bot")

logging.basicConfig(level=logging.DEBUG)

from xmpp_bot.bots.humidity import HumidityBot

server = 'localhost'
port = 5222

if __name__ == '__main__':
    if len(sys.argv) >= 4:
        jid = sys.argv[1]           # humidity@localhost
        password = sys.argv[2]      # 1234
        room = sys.argv[3]          # test_room@muc.localhost
        if len(sys.argv) >= 5:
            server = sys.argv[4]    # localhost
        if len(sys.argv) >= 6:
            port = sys.argv[5]      # 5222

        xmpp = HumidityBot(jid, password, "humidity_bot", room)

        xmpp.connect(address=(server, port), use_tls=False)
        xmpp.process(threaded=False)
    else:
        print("Invalid number of arguments.\n" +
              "Usage: python %s <jid> <pass> <room> [host] [port]"  % sys.argv[0])
