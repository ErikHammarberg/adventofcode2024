import re

def one(filename):
    file = open(filename, 'r')
    line = file.read()

    matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line)
    res = 0
    for match in matches:
        res += int(match[0]) * int(match[1])
    return res

resonetest = one('day3-example.txt')
assert resonetest == 161

resone = one('day3input.txt')
assert resone == 159833790

def two(filename):
    file = open(filename, 'r')
    line = file.read()

    matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', line)
    res = 0
    active = True
    for match in matches:
        if match == 'do()':
            active = True
            continue
        if match == 'don\'t()':
            active = False
            continue

        if active:
            nums = re.findall(r'(\d+),(\d+)', match)
            for num in nums:
                res += int(num[0]) * int(num[1])

    return res
restwotest = two('day3-exampletwo.txt')
assert restwotest == 48
restwo = two('day3input.txt')
print(restwo)
