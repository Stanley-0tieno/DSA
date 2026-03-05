def max_avg_subarray(nums, k):
    window_sum = 0
    max_sum = 0


    for i in range(k):
        window_sum += nums[i]

    max_sum = window_sum
    max_start = 0
    
    for right in range(k, len(nums)):
        window_sum += nums[right]
        window_sum -= nums[right - k]

        if window_sum > max_sum:
            max_sum = window_sum
            max_start = right - (k-1)

    best_window = nums[max_start: max_start + k]

    avarage = max_sum/k

    print(max_sum, best_window, avarage)

nums =[1,12,-5,-6,50,3]
k = 4
max_avg_subarray(nums, k)