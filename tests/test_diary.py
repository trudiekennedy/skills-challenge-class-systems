from lib.diary import Diary
import pytest

"""
Initially, has an empty list of entries
"""

def test_initiall_has_empty_list_of_entries():
    diary = Diary()
    assert diary.all() == []

"""
Initially, word count is zero
"""
def test_word_count_is_zero_at_start():
    diary = Diary()
    diary.count_words() == 0

"""
Intially, reading time should return an error
"""
def test_initially_reading_time_raises_error():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.reading_time(2)
    assert str(e.value) == "No entries added yet."

"""
Initially best entry should return an error 
"""
def test_initially_that_error_raised_for_best_entry():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.find_best_entry_for_reading_time(2,2)
    assert str(e.value) == "No entries added yet."