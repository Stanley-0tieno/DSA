x = 121

def isPalindrome(x):
    s = str(x)
    left = 0
    right = len(s)- 1

    while left <= right:
        if s[left] != s[right]:
            print("False")
            return
        left += 1
        right -= 1
    print("True")
        
isPalindrome(x)