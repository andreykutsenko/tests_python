from functools import reduce


some_dict = {"one": 1, "two": 2, "three": 3}
another_dict = {key : value ** 2 for key, value in some_dict.items()}

# print(another_dict)

"""s = 'cafa'
# print(s.split('a')[-1])

sub = ''
res = ''
for i in s:
    if i not in sub:
        sub += i
    else:
        if len(res) < len(sub):
            res = sub
        sub = sub.split(i)[-1] + i
print(max(len(res), len(sub)))"""
nums = [-1,0,1,2,-1,-4]
res = []
nums.sort()

def twoSumII(nums, i, res):
    lo, hi = i + 1, len(nums) - 1
    while (lo < hi):
        sum = nums[i] + nums[lo] + nums[hi]
        if sum < 0:
            lo += 1
        elif sum > 0:
            hi -= 1
        else:
            res.append([nums[i], nums[lo], nums[hi]])
            lo += 1
            hi -= 1
            while lo < hi and nums[lo] == nums[lo - 1]:
                lo += 1


for i in range(len(nums)):
    if nums[i] > 0:
        break
    if i == 0 or nums[i - 1] != nums[i]:
        twoSumII(nums, i, res)
print(res)




# for i in nums:
#     lambda x, y, z: x + y + z
#     while
# volume = reduce((lambda x, y: x * y), map(int, input().strip().split()))
# print(f'{volume=}')

# dicts = {}
# maxlength = start = 0
# for i, value in enumerate(s):
#     if value in dicts:
#         sums = dicts[value] + 1
#         if sums > start:
#             start = sums
#     num = i - start + 1
#     if num > maxlength:
#         maxlength = num
#     dicts[value] = i

# print(maxlength)
# ans = 0
# sub = ''
# for char in s:
#     if char not in sub:
#         sub += char
#         print(sub)
#         ans = max(ans, len(sub))
#     else:
#         cut = sub.index(char)
#         sub = sub[cut+1:] + char
#         print(sub)
# print(max(3, 44444445))





"""

# s_copy = s[:]
# for i, it in enumerate(s):
#     print(f'{i}: {it}')
# for i in s_copy:
#     print(f'{s_copy.index(i)}: {i}')
# for i in range
#     result.append(i)
# print(result)
max_res = 0
indexL = 0
# indexR = 0
for index, item in enumerate(s):
    # print(f'{index} {item}')
    if item not in s_max:
        s_max += item # формируем строку
        max_res = (index - indexL) + 1
    else:
        if max_res < ((index - indexL) + 1):
            max_res = (index - indexL) + 1
        indexL = index
        print(f'{max_res=}\n{indexL=}\n{s_max=}')
        s_max = item
        print(f'{s_max=}')
        # s_copy = s_copy[:index+1] + '-' + s_copy[index+1:]
print(max_res)

# print(f'{s_max}\n{s_copy}')
#
# for i in s:
#     if i in s_new:
#         s_new += ';'+i
#         s_copy = s[s.index(i)::]
#         print(s_copy)
#     else:
#         s_new += i
# try:
#     max_len = len(max(s_new.split(';'), key=len))
# except:
#     max_len = 0

# print(f'{s_new}\n{max_len}')

for i in s:
    if i in s_new:
        # print(s_new)
        result.append(len(s_new))
        s_new = ""
    else:
        s_new = s_new + i
        # print(s_new)
    result.append(len(s_new))
    res = max(result)
    print(s_new)
if len(s) == 0:
    res = 0

print(res)

# names = ["John", "Bob", "Andy", "Tommy", "Alex"]
# names_starts = filter(lambda name: name.startswith('T'), names)
# print(tuple(names_starts))


"""