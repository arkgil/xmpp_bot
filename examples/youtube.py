import sys
import logging

if sys.version_info < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf8')

sys.path.append("../xmpp_bot")

from xmpp_bot.bots.youtube import YouTubeBot

logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    if len(sys.argv) >= 4:
        jid = sys.argv[1]           # youtube@localhost
        password = sys.argv[2]      # 1234
        room = sys.argv[3]          # test_room@muc.localhost

        xmpp = YouTubeBot(jid, password, "youtube_bot", room)

        xmpp.connect()
        xmpp.process(threaded=False)
    else:
        print("Invalid number of arguments.\n" +
              "Usage: python %s <jid> <pass> <room>" % sys.argv[0])
