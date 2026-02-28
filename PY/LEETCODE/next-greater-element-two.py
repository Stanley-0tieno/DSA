def Solution(nums):
    n = len(nums)
    result = [-1] * n
    stack = []

    # print(result)
    for i in range (2 * n):
        current = nums[i%n]

        while stack and current > nums[stack[-1]]:
            index = stack.pop()
            result[index] = current

        if i < n :
            stack.append(i)
    print(result)

nums = [1,2,1]
Solution(nums)

    
