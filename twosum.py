# nums = [0,1,2,3,4,8,7,6,5]
# nums.sort()
# def twoSum(nums, target):
#     low, high = 0, len(nums)-1
#     while low < high:
#         sum = nums[low] + nums[high]
#         if sum == target:
#             return [low, high]
#         elif sum < target:
#             low += 1
#         else:
#             high -= 1
#     return [-1, -1]
#
# # print(twoSum(nums, 15))
# print(range(len(nums)))


s = "aacc"
t = "ccac"
l = sorted(list(t))
q = sorted(list(s))
print("".join(l))
print("".join(q))
print(l == q)
# if len(s) != len(t):
#     print(False)
# else:
#     for i in s:
#         if i in l:
#             res += i
#             p = l.index(i)
#             del(l[p])
#         else:
#             break
#     if res == s:
#         print(True)
#     else:
#         print(False)

#
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         else:
#             res = ""
#             l = list(t)
#             for i in s:
#                 if i in l:
#                     res += i
#                     p = l.index(i)
#                     del(l[p])
#                 else:
#                     break
#             if res == s:
#                 return True
#             else:
#                 return 0==1


