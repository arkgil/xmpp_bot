import sys
import logging

if sys.version_info < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf8')

sys.path.append("../xmpp_bot")

logging.basicConfig(level=logging.DEBUG)

server = 'localhost'
port = 5222

from xmpp_bot.controllers.copernicus import DashboardController

if __name__ == '__main__':
    if len(sys.argv) >= 4:
        jid = sys.argv[1]           # dashboard1@localhost
        password = sys.argv[2]      # 1234
        pubsub_server = sys.argv[3] # pubsub.localhost
        if len(sys.argv) >= 5:
            server = sys.argv[4]    # localhost
        if len(sys.argv) >= 6:
            port = sys.argv[5]      # 5222

        xmpp = DashboardController(jid, password, pubsub_server)

        xmpp.connect(address = (server, port), use_tls=False)
        xmpp.process(threaded=False)
    else:
        print("Invalid number of arguments.\n" +
              "Usage: python %s " +
              "<jid> <pass> <pubsub> [host] [port]" % sys.argv[0])
