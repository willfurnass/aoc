# Advent of code 2017
# Day 1: Inverse Captcha
# 
# Will Furnass

from functools import reduce
from aoc import get_raw_input


def test_set():
    assert inv_captcha([]) == 0

    assert inv_captcha([1]) == 0

    assert inv_captcha([1, 1, 2, 2]) == 3
    # because the first digit (1) matches the second digit and
    # the third digit (2) matches the fourth digit.

    assert inv_captcha([4, 4, 4, 4]) == 4
    # because each digit (all 1) matches the next.

    assert inv_captcha([1, 2, 3, 4]) == 0
    # because no digit matches the next.

    assert inv_captcha([9, 1, 2, 1, 2, 1, 2, 9]) == 9
    # because the only digit that matches the next one is the last digit, 9.


def _conjoin_first_last_runs(runs):
    # amalgamate the first and last runs
    # have the same value
    # but are distinct 
    if len(runs) > 1 and runs[0][0] == runs[-1][0] and runs[0][1] != len(runs):
        runs[0][1] += 1
        runs.pop()
    return runs


def _gen_runs(runs, next_val):
    # generate a list of runs, each is a [value, length]
    if runs and runs[-1][0] == next_val:
        runs[-1][1] += 1
    else:
        runs.append([next_val, 1])
    return runs


def inv_captcha(int_seq):
    return sum(
            map(lambda run: run[0],
                filter(lambda run: run[1] > 1,
                       _conjoin_first_last_runs(
                           reduce(_gen_runs, int_seq, [])))))


if __name__ == '__main__':
    txt = get_raw_input().strip()
    long_seq = list(map(int, txt))
    print(inv_captcha(long_seq))
