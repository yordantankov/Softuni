class Music:
    def __init__(self, title, artist, lyrics: str):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics


    def print_info(self) -> str:
        return F'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics

song = Music("Title", "Artist", "Lyrics")
print(song.print_info())
print(song.play())