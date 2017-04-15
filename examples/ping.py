import sys
sys.path.append("../xmpp_bot")

from xmpp_bot.bots import PingBot

xmpp = PingBot("ping@localhost", "1234", "ping_bot", "test_room@muc.localhost")

xmpp.connect()
xmpp.process(threaded=False)
