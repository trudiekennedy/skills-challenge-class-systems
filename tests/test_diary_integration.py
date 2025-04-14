from lib.diary import Diary
from lib.diary_entry import DiaryEntry

"""
Given I add two diary entries, I see them back in a list
"""
def test_adds_and_lists_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "Contents of entry 1")
    entry_2 = DiaryEntry("Title 2", "Contents of diary entry 2")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]

"""
Given I add two diary entries
And I call count words
I get the sum of all words in the diary entries contents
"""

def test_count_words_all_entry_total():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "Contents of entry one")
    entry_2 = DiaryEntry("Title 2", "Contents of diary entry two")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 9

"""
Given I add two diary entries with a total length of 5
And I call #reading_time with a wpm of 2
Then the total reading time should be 3 (rounded up to whole min)
""" 
def test_reading_time_returns_time_to_read_all_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "un deux trois")
    entry_2 = DiaryEntry("Title 2", "quatre cinq")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.reading_time(2) == 3

"""
Given I have two diary entries with one long content and one short one
And I call #find_best_entry_for_reading_time
With a wpm and minutes that mean I can only read the short one
Then find_best_entry_for_reading_time will return the shorter one.
"""

def test_find_best_entry_for_reading_time_returns_short_entry():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "un deux trois")
    entry_2 = DiaryEntry("Title 2", "quatre cinq six sept huit neuf dix onze douze treiz quatorze")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry_1

"""
Given I have a diary entry
And I call #find_best_entry_for_reading_time 
With a wpm and minutes that mean I can read that entry
Then #find_best_entry_for_reading_time returns that entry
"""
def test_find_best_entry_returns_entry_that_fits_in_time():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "un deux trois")
    diary.add(entry_1)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry_1

"""
Given I have a diary entry
And I call #find_best_entry_for_reading_time 
With a wpm and minutes that mean I cannot read that entry
Then #find_best_entry_for_reading_time returns an empty list
"""
def test_returns_none_if_no_entries_can_be_read_in_time():
    diary = Diary()
    entry_1 = DiaryEntry("Title 2", "quatre cinq six sept huit neuf dix onze douze treiz quatorze")
    diary.add(entry_1)
    assert diary.find_best_entry_for_reading_time(2, 3) == None

"""
Given I have two diary entries
And I call #find_best_entry_for_reading_time
With a wpm minutes that means I can read both entries
Then #find_best_entry_for_reading_time returns the longer entry
"""
def test_find_best_entry_for_reading_time_returns_longer_entry():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "un deux trois")
    entry_2 = DiaryEntry("Title 2", "quatre cinq six sept huit neuf dix onze douze treiz quatorze")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 10) == entry_2