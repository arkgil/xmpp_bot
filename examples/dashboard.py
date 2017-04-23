import sys
import logging

if sys.version_info < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf8')

sys.path.append("../xmpp_bot")

logging.basicConfig(level=logging.DEBUG)

from xmpp_bot.bots.copernicus import DashboardBot

xmpp = DashboardBot("dashboard@localhost", "1234", "dashboard_bot", "test_room@muc.localhost", "pubsub.localhost")

xmpp.connect()
xmpp.process(threaded=False)
