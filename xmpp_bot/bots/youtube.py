from ..base import BaseBot
import subprocess
import youtube_dl

class YouTubeBot(BaseBot):
    def __init__(self, jid, password, nick, room):
        BaseBot.__init__(self, jid, password, nick, room)
        self.player = MPV()

    def handle_message(self, msg):
        if msg['body'].startswith('/play '):
            try:
                url = msg['body'].split(' ')[1]
                (result, desc) = self.player.start(url)
                if result == 'ok':
                    msg = 'Started playing'
                    self.send_msg(msg)
                elif desc == 'already started':
                    msg = 'Song has been already started'
                    self.send_msg(msg)
            except ValueError:
                self.send_msg('error')

        elif msg['body'].strip() == '/cancel':
                (result, desc) = self.player.stop()
                if result == 'ok':
                    msg = 'Stopped playing'
                    self.send_msg(msg)
                elif desc == 'noproc':
                    msg = 'Nothing is playing now'
                    self.send_msg(msg)

        elif msg['body'].strip() == '/ping':
            msg = 'pong'
            self.send_msg(msg)

    def send_msg(self, msg):
        self.send_message(mto=self.room,
                          mbody=msg,
                          mtype='groupchat')

class MPV():
    def __init__(self):
        self.process = None
        self.volume = 100
        self.youtube_dl = youtube_dl.YoutubeDL({'format': 'bestaudio/best'})

    def start(self, url):
        if self.__is_started():
            return ('error', 'already started')
        play_url = self.youtube_dl.extract_info(url, download=False)['url']
        args = ["mpv", "--no-video", play_url]
        self.process = subprocess.Popen(args,
                                        stdin = subprocess.PIPE,
                                        stdout = subprocess.PIPE)
        return ('ok', 'started')

    def stop(self):
        if self.__is_started():
            self.process.kill()
            return  ('ok', 'stopped')
        else:
            return ('error', 'noproc')

    def __is_started(self):
        if self.process is not None:
            if self.process.poll() is None:
                return True
        return False
