from collections import Counter
import random


def custom_counter():
    print("Build a custom counter")
    dict = {}
    letters = ["A", "B", "C", "D", "E", "F"]
    for _ in range(100):
        letter = random.choice(letters)
        dict[letter] = dict.get(letter, 0) + 1
    print(dict, sum(dict.values()))


def built_in_counter():
    print("Use the built in counter")
    counter = Counter()
    letters = ["A", "B", "C", "D", "E", "F"]
    for _ in range(100):
        letter = random.choice(letters)
        counter[letter] = counter[letter] + 1
    print(counter, sum(counter.values()))


def short_built_in_counter():
    print("Use the built in counter")
    names = ["John", "Smith", "Ramu", "Samu", "Babu", "Babar"]
    hun_names = random.choices(names, k=100)
    occurences_counter = Counter(hun_names)
    print(
        occurences_counter,
        sum(occurences_counter.values()),
        occurences_counter.most_common(2),
    )


def counter_operations():
    c1 = Counter({"a": 11, "b": 22, "c": 33})
    c2 = Counter({"a": 1, "b": 2, "c": 3})
    print(c1 - c2)
    print(c1 + c2)


custom_counter()
built_in_counter()
short_built_in_counter()
counter_operations()
