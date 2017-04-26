import sys
import logging

if sys.version_info < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf8')

sys.path.append("../xmpp_bot")

logging.basicConfig(level=logging.DEBUG)

from xmpp_bot.bots.copernicus import DashboardBot

server = 'localhost'
port = 5222

if __name__ == '__main__':
    if len(sys.argv) >= 5:
        jid = sys.argv[1]           # dashboard@localhost
        password = sys.argv[2]      # 1234
        room = sys.argv[3]          # test_room@muc.localhost
        pubsub_server = sys.argv[4] # pubsub.localhost
        if len(sys.argv) >= 6:
            server = sys.argv[5]    # localhost
        if len(sys.argv) >= 7:
            port = sys.argv[6]      # 5222

        xmpp = DashboardBot(jid, password, "dashboard_bot", room, pubsub_server)

        xmpp.connect(address=(server, port), use_tls=False)
        xmpp.process(threaded=False)
    else:
        print("Invalid number of arguments.\n" +
              "Usage: python %s " +
              "<jid> <pass> <room> <pubsub> [host] [port]" % sys.argv[0])
