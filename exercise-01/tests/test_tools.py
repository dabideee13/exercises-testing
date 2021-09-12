import sys
from pathlib import Path, PosixPath

import pytest

sys.path.insert(0, '../src')

from tools import (
    pipe,
    get_raw,
    get_preprocessed,
    word_tokenize,
    count_vowel,
    get_wordList,
    get_vowelCounts,
    preprocess_text,
)


def get_dataPath(folder_name: str, filename: str) -> PosixPath:
    return Path.joinpath(Path.cwd().parent, 'data/', folder_name, filename)


RAW = get_dataPath('raw', 'test_data.txt')
PROCESSED = get_dataPath('processed', 'test_data_processed.json')


@pytest.fixture
def preprocessed_data():
    return pipe(PROCESSED, get_preprocessed)


@pytest.fixture
def test_data():
    return pipe(RAW, get_raw)


@pytest.fixture
def tokens():
    return pipe(RAW, get_raw, word_tokenize)


@pytest.fixture
def word_list():
    return pipe(RAW, get_raw, word_tokenize, get_wordList)


def test_word_tokenize(test_data):

    assert isinstance(test_data, str)

    tokenize_words = word_tokenize(test_data)
    assert isinstance(tokenize_words, list)

    for word in tokenize_words:
        assert isinstance(word, str)


def test_count_vowel(preprocessed_data):

    for data, count in preprocessed_data.items():

        assert isinstance(data, str)
        assert isinstance(count, int)

        assert count_vowel(data) == count


def test_get_wordList(tokens):

    assert isinstance(tokens, list)

    word_list = get_wordList(tokens)
    assert len(set(tokens)) == len(word_list)
    assert isinstance(word_list, set)

    for word in word_list:
        assert isinstance(word, str)


def test_get_vowelCounts(word_list):

    assert isinstance(word_list, set)

    vowel_counts = get_vowelCounts(word_list)
    assert isinstance(vowel_counts, list)

    for count in vowel_counts:
        assert isinstance(count, int)


def test_preprocess_text(preprocessed_data):

    assert isinstance(preprocessed_data, dict)

    for key, val in preprocessed_data.items():
        assert isinstance(key, str)
        assert isinstance(val, int)
