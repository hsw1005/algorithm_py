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
    commands.append(input())
    nums.append(input())
    str = input().lstrip("[").rstrip("]").split(",")
    temp_arrs.append(str)
#print(commands, nums, temp_arrs)
print(temp_arrs)
l = len(temp_arrs)

for idx, command in enumerate(commands):
    comm = list(command)
    while True:
        try:
            if len(comm) != 0:
                com = comm.pop(0)
                if com == "R":
                    temp_arrs[idx] = temp_arrs[idx][::-1]
                if com == "D":
                    if len(temp_arrs[idx]) != 0:
                        temp_arrs[idx].pop(0)
                    else:
                        print("error")
                        continue

                if len(comm) == 0:
                    print(temp_arrs[idx])
                    break

        except:
            print("error")
            break

