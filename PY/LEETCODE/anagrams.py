def find_all_anagrams(s, p):

    result = []
    k = len(p)

     # Step 1: build frequency map of p
    p_count = {}
    for char in p :
        p_count[char] = p_count.get(char, 0) + 1

    # Step 2: build frequency map of first window in s
    window_count = {}
    for char in s[:k]:
        window_count[char] = window_count.get(char, 0) + 1

     # Step 3: check first window
    if window_count == p_count:
        print("anagram found")
        result.append(0)

    # Step 4: slide the window
    for i in range(k, len(s)):
        # character entering the window
        new_char = s[i]
        window_count[new_char] = window_count.get(new_char, 0) + 1
        
        # character leaving the window
        old_char = s[i - k]
        window_count[old_char] -= 1
        if window_count[old_char] == 0:
            del window_count[old_char]  # keep dict clean
        
        # check if current window matches p_count
        if window_count == p_count:
            start_index = i - k + 1
            result.append(start_index)
            print(f"Anagram found at index {start_index}")
    
    print(result) 



s = "cbaebabacd"
p = "abc"

find_all_anagrams(s, p)