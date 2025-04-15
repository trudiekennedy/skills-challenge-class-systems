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

        return ceil(self.count_words()/ wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        if self._entries == []:
            raise Exception("No entries added yet.")
        words_user_can_read = wpm * minutes

        # finds entries where word count is less than or equal to what the use can read
        readable_entries = [entry for entry in self._entries if entry.count_words() <= words_user_can_read]

        if not readable_entries:
            return None
        
        # looks for the entry with the highest word count amongst the readable_entries
        return max(readable_entries, key=lambda entry: entry.count_words())