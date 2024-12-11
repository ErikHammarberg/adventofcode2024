import pprint

from yt_dlp.extractor import funk

word_d = {"X" : "M", "M": "A", "A" : "S"}

# def search(lines, x, y, found):
#     if x < 0 or y < 0 or x >= len(lines[0]) or y >= len(lines):
#         return 0
#     letter = lines[x][y]
#     if letter == 'S':
#         return 1
#     next = word_d[found]
#     if next == letter:
#         return

def common_search(lines, x, y, found, funk):
    letter = lines[y][x]

    next = word_d[found]
    if next == letter:
        if letter == 'S':
            return 1
        return funk(lines, x, y, letter)
    return 0

def left(lines, x, y, found):
    if x == 0:
        return 0
    xx = x-1
    yy = y
    return common_search(lines, xx, yy, found, left)

def right(lines, x, y, found):
    if x == len(lines[0])-1:
        return 0
    xx = x+1
    yy = y
    return common_search(lines, xx, yy, found, right)

def up(lines, x, y, found):
    if y == 0:
        return 0
    xx = x
    yy = y-1
    return common_search(lines, xx, yy, found, up)

def down(lines, x, y, found):
    if y == len(lines)-1:
        return 0
    xx = x
    yy = y+1
    return common_search(lines, xx, yy, found, down)

def downright(lines, x, y, found):
    if x == len(lines[0])-1 or y == len(lines)-1:
        return 0
    xx = x+1
    yy = y+1
    return common_search(lines, xx, yy, found, downright)
def downleft(lines, x, y, found):
    if x == 0 or y == len(lines)-1:
        return 0
    xx = x-1
    yy = y+1
    return common_search(lines, xx, yy, found, downleft)
def upright(lines, x, y, found):
    if x == len(lines[0])-1 or y == 0:
        return 0
    xx = x+1
    yy = y-1
    return common_search(lines, xx, yy, found, upright)
def upleft(lines, x, y, found):
    if x == 0 or y == 0:
        return 0
    xx = x-1
    yy = y-1
    return common_search(lines, xx, yy, found, upleft)




def one(filename):
    file = open(filename, "r")
    lines = file.readlines()

    res = 0
    for y in range(0, len(lines)):
        for x in range(0, len(lines[0])):
            if lines[y][x] == 'X':
                res += left(lines, x, y, 'X')
                res += right(lines, x, y, 'X')
                res += up(lines, x, y, 'X')
                res += down(lines, x, y, 'X')
                res += downright(lines, x, y, 'X')
                res += downleft(lines, x, y, 'X')
                res += upright(lines, x, y, 'X')
                res += upleft(lines, x, y, 'X')
    return res

onetest = one('day4example.txt')
print(onetest)
assert onetest == 18

oneres = one('day4input.txt')
print(oneres)
assert oneres == 2447
