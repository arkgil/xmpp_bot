import sys
import logging

if sys.version_info < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf8')

sys.path.append("../xmpp_bot")

logging.basicConfig(level=logging.DEBUG)

from xmpp_bot.bots.copernicus import DashboardBot

if __name__ == '__main__':
    if len(sys.argv) >= 5:
        jid = sys.argv[1]           # dashboard@localhost
        password = sys.argv[2]      # 1234
        room = sys.argv[3]          # test_room@muc.localhost
        pubsub_server = sys.argv[4] # pubsub.localhost

        xmpp = DashboardBot(jid, password, "dashboard_bot", room, pubsub_server)

        xmpp.connect()
        xmpp.process(threaded=False)
    else:
        print("Invalid number of arguments.\n" +
              "Usage: python %s <jid> <pass> <room> <pubsub>" % sys.argv[0])
