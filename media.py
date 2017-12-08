import webbrowser


class Movie():

    """constructor"""
    def __init__(self, movie_title, movie_storyline, postr_image, trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = postr_image
        self.trailer_youtube_url = trailer

    """show trailer method"""
    def show_trailer(self):
        webbrowser.open(self.trailer_url)
