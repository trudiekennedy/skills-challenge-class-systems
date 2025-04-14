from math import ceil

class Diary:
    def __init__(self):
        self._entries = []

    def add(self, entry):
        self._entries.append(entry)

    def all(self):
        return self._entries

    def count_words(self):
        return sum([entry.count_words() for entry in self._entries])

    def reading_time(self, wpm):
        if self._entries == []:
            raise Exception("No entries added yet.")
        word_count = self.count_words()
        return ceil(word_count / wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        if self._entries == []:
            raise Exception("No entries added yet.")
        words_user_can_read = wpm * minutes
        most_readable = None
        longest_found_so_far = 0

        for entry in self._entries:
            if entry.count_words() <= words_user_can_read:
                if entry.count_words() > longest_found_so_far:
                    most_readable = entry
                    longest_found_so_far = entry.count_words()
        return most_readable