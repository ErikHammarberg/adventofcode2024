
first_lines = []
second_lines = []
def one(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    good_lines = 0

    for line in lines:
        nums = line.split()
        increasing = int(nums[1]) > int(nums[0])

        before = int(nums[0])
        current = int(nums[1])
        bypassed = False
        for i in range(1, len(nums)):

            if (current < before) == increasing or current == before or abs(current - before) > 3:
                break


            if i == len(nums) - 1:
                good_lines += 1
                first_lines.append(line)
                break
            before = int(nums[i])
            current = int(nums[i+1])
    print(good_lines)


def not_valid(before, current, increasing):
    return (current < before) == increasing or current == before or abs(current - before) > 3

def two(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    good_lines = 0
    the_good_lines = []
    for line in lines:
        nums = line.split()
        increasing = int(nums[1]) > int(nums[0])

        before = int(nums[0])
        current = int(nums[1])
        bypassed = False
        for i in range(1, len(nums)):

            if  not_valid(before, current, increasing):
                if not bypassed:
                    bypassed = True
                    if i == len(nums) - 1:
                        good_lines += 1
                        second_lines.append(line)
                        break
                    if i == 1:
                        if not not_valid(before, int(nums[i+1]), increasing):
                            current = int(nums[i+1])
                            continue

                        if not not_valid(before, int(nums[i+1]), not increasing):
                            current = int(nums[i+1])
                            increasing = not increasing
                            continue

                        if not not_valid(current, int(nums[i+1]), increasing):
                            before = int(nums[i])
                            current = int(nums[i+1])
                            continue

                        if not not_valid(current, int(nums[i+1]), not increasing):
                            before = int(nums[i])
                            current = int(nums[i+1])
                            increasing = not increasing
                            continue

                    if i == 2:
                        # if not not_valid(before, int(nums[i+1]), not increasing):
                        #     current = int(nums[i+1])
                        #     increasing = not increasing
                        #     continue
                        if not not_valid(current, int(nums[i+1]), not increasing) and not not_valid(int(nums[i-2]), current, not increasing):
                            before = int(nums[i])
                            current = int(nums[i+1])
                            increasing = not increasing
                            continue
                        # if the fault is between the first and second one, we don't know which to kick out
                    current = int(nums[i+1])
                    bypassed = True
                    continue
                break
            if i == len(nums) - 1:
                good_lines += 1
                second_lines.append(line)
                break
            before = int(nums[i])
            current = int(nums[i+1])
    print(good_lines)
    for l in the_good_lines:
        print(l)


onetest = one('day2-example.txt')
# should be 2
one = one('day2-input.txt')
# should be lower tahn 394 and 279
# should be 236
# 230 is also wrong
twotest = two('day2-example.txt')
#Should be 4
two = two('day2-input.txt')

# 283 and 298 is too low
# 302 is also wrong

# 311 to high
print('***************************')
for l in second_lines:
    if l not in first_lines:
        print(l)