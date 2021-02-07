food_times = [3, 1, 2]
k = 5
i = 0
count = 0

while True:
    if k != 0:
        if i != len(food_times):
            print(i)
            if food_times[i] != 0:
                food_times[i] -= 1
                i += 1
                k -= 1
            else:
                i += 1
                count += 1
                if count == len(food_times):
                    print(-1)
        else:
            i = 0
    else :
        print("r", i+1)
        break
