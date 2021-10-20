def trap(height):
    if not height:
        return 0

    volume = 0
    left, right = 0, len(height) - 1 # 투포인터 시작 인덱스
    left_max, right_max = height[left], height[right] # 투포인터 시작 높이

    while left < right: # left 인덱스가 right 인덱스보다 왼쪽일때
        left_max, right_max = max(height[left], left_max), max(height[right], right_max) # 현재 높이와 이동한 높이 중 최대를 저장
        if left_max <= right_max: # 왼쪽의 높이가 오른쪽 높이보다 작거나 같을 때
            volume += left_max - height[left]
            left += 1
        else:                     # 오른쪽의 높이가 왼쪽의 높이보다 작을때
            volume += right_max - height[right]
            right -= 1

        # 최대 높이 지점에서 두 포인터가 만난다.
    return volume



arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] # -> 6
arr2 = [10, 0, 0, 0, 0, 10] # -> 40
answer = trap(arr)
print(answer)