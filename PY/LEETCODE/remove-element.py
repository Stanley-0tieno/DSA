def Solution(nums,val):
    k = 0

    for i in range(len(nums)):
        if val != nums[i]:
            nums[k] = nums[i]
            k += 1
    print(k)

nums = [1,2,4,6]
val = 4
Solution(nums, val)