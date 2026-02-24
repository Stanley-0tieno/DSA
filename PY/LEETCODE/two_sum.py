input = [2, 7, 11, 15 ]
target = 9

def Solution(input, target):
    new_array = sorted(input)
    left = 0
    right = len(new_array) - 1

    while left < right:
        current_sum = new_array[left] + new_array[right]
        if current_sum > target:
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            print(left)
            print(right)
            break


Solution(input, target)