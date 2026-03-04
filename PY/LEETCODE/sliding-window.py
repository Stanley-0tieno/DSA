def max_sum_subarray(arr, k):
    window_sum = 0
    max_sum = 0

    for i in range(k):
        window_sum += arr[i]

    max_sum = window_sum
    max_start = 0

    for right in range(k, len(arr)):
        window_sum += arr[right]
        window_sum -= arr[right-k]

        if window_sum > max_sum:
            max_sum = window_sum
            max_start = right - (k - 1)
        best_window= arr[max_start : max_start + k]


    print(best_window, max_sum)

arr = [2, 1, 5, 1, 3, 2]
k = 3
max_sum_subarray(arr, k)