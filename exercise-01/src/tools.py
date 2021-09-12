import json
import re
from typing import List, Set, Dict


def pipe(raw_input: str, *args, **kwargs):

    output = raw_input

    if args:
        for arg in args:
            output = arg(output)

    if kwargs:
        for key, vals in kwargs.items():
            output = eval(key, *vals)

    return output


def word_tokenize(text: str) -> List[str]:
    first_pattern = r'[A-Za-z]{2,}'
    second_pattern = r'W+^[\s+]'
    preprocessed_text = re.sub(second_pattern, '', text)
    return re.findall(first_pattern, preprocessed_text)


def get_raw(filename: str) -> str:
    with open(filename, 'r') as f:
        data = f.read()
    return data


def get_preprocessed(filename: str) -> Dict[str, int]:
    with open(filename, 'r') as f:
        data = json.load(f)
    return data


def export_text(text: str, filename: str = 'sample.json'):
    with open(filename, 'w') as f:
        json.dump(text, f, indent=4)


def count_vowel(string: str) -> int:
    counter = 0
    for s in string:
        if s in ['a', 'e', 'i', 'o', 'u']:
            counter += 1
    return counter


def get_wordList(tokenize_words: List[str]) -> Set[str]:
    return pipe(tokenize_words, set)


def get_vowelCounts(word_list: Set[str]) -> List[int]:
    return [count_vowel(word) for word in word_list]


def preprocess_text(data: str) -> Dict[str, int]:
    word_list = pipe(data, get_wordList)
    vowelCounts = pipe(word_list, get_vowelCounts)
    return dict(zip(word_list, vowelCounts))
