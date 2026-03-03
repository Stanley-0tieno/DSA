def Solution(nums):
    left = 0
    right = 1

    k = 1

    for right in range(len(nums)):
        if nums[left] != nums[right]:
            left += 1
            k += 1
            nums[left] = nums[right]

    print(nums[:k], k)
nums = [1, 2, 3, 3, 4]
Solution(nums)
