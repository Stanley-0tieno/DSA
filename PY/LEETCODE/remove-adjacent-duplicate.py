def removeDuplicate(s):
    stack = []

    for char in s:
        if  len(stack) != 0 and  char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    print("".join(stack))
            
            

removeDuplicate("abbec")

