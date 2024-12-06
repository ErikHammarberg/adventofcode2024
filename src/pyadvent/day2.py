
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
                break
            before = int(nums[i])
            current = int(nums[i+1])
    print(good_lines)

def two(filename):
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
                if not bypassed:
                    if i == len(nums) - 1:
                        good_lines += 1
                        break
                    current = int(nums[i+1])
                    bypassed = True
                    continue

                break

            if i == len(nums) - 1:
                good_lines += 1
                break
            before = int(nums[i])
            current = int(nums[i+1])
    print(good_lines)


onetest = one('day2-example.txt')
# should be 2
one = one('day2-input.txt')
# should be lower tahn 394 and 279
# should be 236
# 230 is also wrong
twotest = two('day2-example.txt')
#Should be 4
two = two('day2-input.txt')

# 283 is too low
