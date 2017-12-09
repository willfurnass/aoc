import os
from functools import reduce

from aoc import get_raw_input


""""Day 4 - part 1

A new system policy has been put in place that requires all accounts to use a
passphrase instead of simply a password. A passphrase consists of a series of
words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

The system's full passphrase list is available as your puzzle input.
How many passphrases are valid?

Day 4 - part 2

For added security, yet another system policy has been put in place. Now, a
valid passphrase must contain no two words that are anagrams of each other -
that is, a passphrase is invalid if any word's letters can be rearranged to
form any other word in the passphrase.

Under this new system policy, how many passphrases are valid?

"""


def test_part_1():

    assert is_valid_pass('aa bb cc dd ee')

    assert not is_valid_pass('aa bb cc dd aa')
    # as the word 'aa' appears more than once.

    assert is_valid_pass('aa bb cc dd aaa')
    # as 'aa' and 'aaa' count as different words.


def test_part_2():

    assert is_valid_pass('abcde fghij', part_2=True)

    assert not is_valid_pass('abcde xyz ecdab', part_2=True)
    # as the letters from the third word can be rearranged to form the first
    # word.

    assert is_valid_pass('a ab abc abd abf abj', part_2=True) 
    # as all letters need to be used when forming another word.

    assert is_valid_pass('iiii oiii ooii oooi oooo', part_2=True)

    assert not is_valid_pass('oiii ioii iioi iiio', part_2=True)
    # as any of these words can be rearranged to form any other word.


def is_valid_pass(password, part_2=False):
    words = password.split()
    if part_2:
        words = [tuple(sorted(word)) for word in words]
    return len(words) == len(set(words))


if __name__ == '__main__':
    passwords = get_raw_input().split(os.linesep)

    print("Part 1: {} passwords are valid".format(
        sum(1 for pw in passwords if is_valid_pass(pw))))

    print("Part 2: {} passwords are valid".format(
        sum(1 for pw in passwords if is_valid_pass(pw, part_2=True))))
