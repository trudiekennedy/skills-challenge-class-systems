from math import ceil

class DiaryEntry:
    def __init__(self, title, contents): # title, contents are strings
        self.title = title
        self.contents = contents
        self._stop_off_point = 0

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        return ceil(self.count_words() / wpm)

    def reading_chunk(self, wpm, minutes):
        words = self.contents.split()
        if self._stop_off_point >= len(words): 
            self._stop_off_point = 0

        readable_chunk_length = wpm * minutes

        start_point = self._stop_off_point
        end_point = self._stop_off_point + readable_chunk_length
        readable_chunk = " ".join(words[start_point:end_point])
        self._stop_off_point += readable_chunk_length
        return readable_chunk