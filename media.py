import webbrowser
class Movie():
  '''
  This class is movie class where you define your favourite moive with
    title
    stoty line
    poster image url
    trailer youtube url
  '''
  def __init__(self, movie_title, moive_storyline, poster_image_url, trailer_url):
    self.title = movie_title
    self.storyline = moive_storyline
    self.poster_image_url = poster_image_url
    self.trailer_youtube_url = trailer_url

  def show_trailer(self):
    webbrowser.open(self.trailer_youtube_url)
