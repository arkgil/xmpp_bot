import sys

if sys.version_info < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf8')

sys.path.append("../xmpp_bot")

from xmpp_bot.bots.humidity import HumidityBot

xmpp = HumidityBot("humidity@localhost", "1234", "humidity_bot", "test_room@muc.localhost")

xmpp.connect()
xmpp.process(threaded=False)
