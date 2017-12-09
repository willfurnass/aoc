""""
Day 4 - part 1

A new system policy has been put in place that requires all accounts to use a
passphrase instead of simply a password. A passphrase consists of a series of
words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

The system's full passphrase list is available as your puzzle input.
How many passphrases are valid?
"""

import os
from functools import reduce

from aoc import get_raw_input


def test_part_1():

    assert is_valid_pass('aa bb cc dd ee')

    assert not is_valid_pass('aa bb cc dd aa')
    # as the word 'aa' appears more than once.

    assert is_valid_pass('aa bb cc dd aaa')
    # as 'aa' and 'aaa' count as different words.


def is_valid_pass(password):
    words = password.split()
    return len(words) == len(set(words))


if __name__ == '__main__':
    txt = get_raw_input()
    cnt = reduce(lambda a, b: a + 1,
                 filter(is_valid_pass,
                        txt.split(os.linesep)),
                 0)
    print(cnt)
