"""
Day 5 - part 1

An urgent interrupt arrives from the CPU: it's trapped in a maze of jump
instructions, and it would like assistance from any programs with spare cycles
to help find the exit.

The message includes a list of the offsets for each jump. Jumps are relative:
-1 moves to the previous instruction, and 2 skips the next one. Start at the
first instruction in the list. The goal is to follow the jumps until one leads
outside the list.

In addition, these instructions are a little strange; after each jump, the
offset of that instruction increases by 1. So, if you come across an offset of
3, you would move three instructions forward, but change it to a 4 for the next
time it is encountered.

For example, consider the following list of jump offsets:

0
3
0
1
-3

Positive jumps ("forward") move downward; negative jumps move upward. For
legibility in this example, these offset values will be written all on one
line, with the current instruction marked in parentheses. The following steps
would be taken before an exit is found:

    (0) 3  0  1  -3  - before we have taken any steps.
    (1) 3  0  1  -3  - jump with offset 0 (that is, don't jump at all). Fortunately, the instruction is then incremented to 1.
     2 (3) 0  1  -3  - step forward because of the instruction we just modified. The first instruction is incremented again, now to 2.
     2  4  0  1 (-3) - jump all the way to the end; leave a 4 behind.
     2 (4) 0  1  -2  - go back to where we just were; increment -3 to -2.
     2  5  0  1  -2  - jump 4 steps forward, escaping the maze.

In this example, the exit is reached in 5 steps.

How many steps does it take to reach the exit?

Day 5 - part 2

Now, the jumps are even stranger: after each jump, if the offset was three or
more, instead decrease it by 1. Otherwise, increase it by 1 as before.

Using this rule with the above example, the process now takes 10 steps, and the
offset values after finding the exit are left as 2 3 2 3 -1.

How many steps does it now take to reach the exit?
"""

from aoc import get_raw_input


def _state_str(instrs, pointer):
    return '\t'.join(('({})' if i == pointer else '{}').format(x)
                     for i, x in enumerate(instrs))


_test_input = [0, 3,  0,  1,  -3]


def test_pt_1():
    wanted = (5, [2, 5, 0, 1, -2])
    got = process_instrs(_test_input)
    print(wanted, got)
    assert wanted == got


def test_pt_2():
    wanted = (10, [2, 3, 2, 3, -1])
    got = process_instrs(_test_input, part_2=True)
    print(wanted, got)
    assert wanted == got


def process_instrs(instrs, pointer=0, part_2=False):
    """Returns a tuple of the number of jumps taken to exit the list of
    instructions and the final list of instructions)"""
    instrs = instrs.copy()
    instrs_done = 0

    while True:
        cur_instr = instrs[pointer]
        if (part_2 and cur_instr > 2):
            instrs[pointer] -= 1
        else:
            instrs[pointer] += 1
        pointer += cur_instr
        instrs_done += 1
        if pointer < 0 or pointer >= len(instrs):
            break
    return (instrs_done, instrs)


if __name__ == '__main__':
    instrs = list(map(int, get_raw_input().split()))
    print(process_instrs(instrs))
    print(process_instrs(instrs, part_2=True))
