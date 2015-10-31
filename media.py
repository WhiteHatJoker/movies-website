import webbrowser


class Movie():
    """This class provides a way to store movie related information"""

    # Contstructor to initialize instance variables
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube, year, rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_year = year
        self.rating_star = rating

    # Instance method to open the web tab with the youtube url
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
