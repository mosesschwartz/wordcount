import pytest

from wordcount import wordcount

test_words = "This is a! test this"


def test_basic():
    r = wordcount.count_words(test_words)
    expected_result = {"this": 2, "is": 1, "a!": 1, "test": 1}
    assert dict(r) == expected_result


def test_case_sensitive():
    r = wordcount.count_words(test_words, make_lower=False)
    expected_result = {"This": 1, "this": 1, "is": 1, "a!": 1, "test": 1}
    assert dict(r) == expected_result


def test_strip_chars():
    r = wordcount.count_words(test_words, strip_chars="!")
    expected_result = {"this": 2, "is": 1, "a": 1, "test": 1}
    assert dict(r) == expected_result


def test_delimiter():
    r = wordcount.count_words(test_words, word_delimiter="s")
    expected_result = {"thi": 1, " i": 1, " a! te": 1, "t thi": 1}
    assert dict(r) == expected_result
