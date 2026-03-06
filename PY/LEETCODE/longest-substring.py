class Solution(object):
    def lengthOfLongestSubstring(s):
        window_length = 0
        left = 0
        right = 1
        max_length = 0

        char_set = set()

        for right in range(len(s)):

            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])

            window_length = right - left + 1
            max_length = max(max_length, window_length)
        print(max_length)

    s = "abcabcbb"
    lengthOfLongestSubstring(s)