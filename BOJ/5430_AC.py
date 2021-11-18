"""
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
"""
round = int(input())
commands = []
nums = []
temp_arrs = []
for _ in range(round):
    command = input()
    commands.append(input())
    nums.append(int(input()))
    str = input().lstrip("[").rstrip("]").split(",")
    temp_arrs.append(str)
print(commands, nums, temp_arrs)
l = len(temp_arrs)

for command in commands:
    pass
