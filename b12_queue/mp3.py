class Mp3Player:
    def __init__(self):
        self.music_queue = []
        self.current_song = None

    def add_song(self, songs):
        self.music_queue.extend(songs)
        for song in songs:
            print(f"Added MP3 file: {song}")

    def play_next_song(self):
        if self.music_queue:
            self.current_song = self.music_queue.pop(0)
            print(f"Playing MP3 file: {self.current_song}")
        else:
            print("No MP3 files in the queue")

    def skip_song(self):
        if self.music_queue:
            print(f"Skipping MP3 file: {self.current_song}")
            self.play_next_song()
        else:
            print("No MP3 files to skip to")

mp3_player = Mp3Player()
mp3_player.add_song(["test.mp3", "test2.mp3"])
mp3_player.play_next_song()
mp3_player.skip_song()
