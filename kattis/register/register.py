import sys

vals = [2,3,5,7,11,13,17,19]
# 2, 2*3, 2*3*5, ...
needed = [1, 2, 1, 1, 1, 1, 1, 1]
for i in range(2, len(needed)):
    needed[i] = needed[i-1] * vals[i-1]
registers = list(map(int, sys.stdin.readline().split()))

diff = 0
for i in range(0 ,len(registers)):
    want = vals[i]-1-registers[i]
    diff += want * needed[i]
print(diff)

# brute force
# data = {}
# diff = 0
# done = False
# while True:
#     done = True
#     for i in range(0, len(vals)):
#         if vals[i]-1 != registers[i]:
#             done = False
#             break
#     if done:
#         break
#
#     for i in range(0, len(registers)):
#         if registers[i] == vals[i]:
#             continue
#         else:
#             registers[i] += 1
#             diff += 1
#             break
#     for i in range(0, len(registers)):
#         if registers[i] == vals[i]:
#             registers[i] = 0
#             registers[i+1] += 1
#             if i not in data:
#                 data[i] = diff
# print(diff)
# print(data)
