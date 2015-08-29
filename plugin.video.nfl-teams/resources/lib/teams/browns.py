import resources.lib.nflcs


class Team(resources.lib.nflcs.NFLCS):
    _short = "browns"
    _cdaweb_url = "http://www.clevelandbrowns.com/cda-web/"
    _categories = [
        "Video - 2 Minute Drill",
        "Video - Draft",
        "Video - Features",
        "Video - Game Highlights",
        "Video - History",
        "Video - Interviews",
        "Video - NFL Network",
        "Video - Off the Field",
        "Video - Press Conferences",
        "Video - Pro Bowl",
        "Video - Senior Bowl",
        "Video - Training Camp",
    ]

    def __init__(self, parameters):
        self._parameters = parameters
        self.go()
