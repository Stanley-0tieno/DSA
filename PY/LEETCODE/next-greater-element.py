def nextGreaterElement( nums1, nums2):
    stack = []
    next_greater = {}

    for num in nums2:
        while stack and num  > stack[-1]:
            top = stack.pop()
            next_greater[top] = num
        stack.append(num)

    while stack:
        top = stack.pop()
        next_greater[top] = -1

    result = []
    for num in nums1:
        result.append(next_greater[num])
        print(result)


first = [4, 1, 2]
second = [1,2,3,4,5]
nextGreaterElement(first, second)