class Song:
    # Class Attributes
    count = 0                    # Total number of songs created
    genres = []                  # List of all unique genres
    artists = []                 # List of all unique artists
    genre_count = {}             # {"Rap": 5, "Rock": 3, ...}
    artist_count = {}            # {"Beyonce": 17, "Jay-Z": 40, ...}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update all statistics when a new song is created
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """Increments total song count"""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Adds genre to list if not already present"""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Adds artist to list if not already present"""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Updates count for each genre"""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """Updates count for each artist"""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1