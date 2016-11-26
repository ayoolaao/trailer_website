import webbrowser
import Video


class Tv_Show(Video):
    def __init__(self, title, duration, season, episode, tv_station):
        Video.__init__(self, title, duration)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station

    def get_local_listing(self):
        webbrowser.open(self.tv_station)