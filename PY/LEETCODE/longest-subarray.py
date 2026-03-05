def longest_sub_array(num, k):

    window_sum = 0
    max_length = 0
    left = 0

    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum > k:
            window_sum -= nums[left]
            left += 1

        window_length = right - left +1
        max_length = max(window_length, max_length)

    print(max_length)

nums = [2,1,5,1,3,2]
k = 7

longest_sub_array(nums, k)