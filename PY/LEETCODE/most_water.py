def Solution(height):
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        width = right - left
        minimum_height = min(height[right], height[left])
        area = width * minimum_height
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1

        max_area = max(max_area, area)
    print(max_area)

height = [1,8,6,2,5,4,8,3,7]       
Solution(height) 

