import sys

if sys.version_info < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf8')

sys.path.append("../xmpp_bot")

from xmpp_bot.bots.youtube import YouTubeBot

xmpp = YouTubeBot("youtube@localhost", "1234", "youtube_bot", "youtube_room@muc.localhost")

xmpp.connect()
xmpp.process(threaded=False)
