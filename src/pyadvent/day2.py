
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


onetest = one('day2-example.txt')

one = one('day2-input.txt')
# should be lower tahn 394 and 279

# 230 is also wrong
