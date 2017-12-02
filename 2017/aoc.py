import sys


def get_raw_input(puzzle=None):
    if not puzzle:
        puzzle = sys.argv[0].split('.')[0]
    with open("{}.input".format(puzzle), 'r') as f:
        txt = f.read()
    return txt
