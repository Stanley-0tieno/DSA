def isvalid(s):
    pairs = {
        ')':'(',
        '}': '{',
        ']': '['
    }

    stack = []

    for char in s:
        if char in "{[(":
            stack.append(char)

        elif char in pairs:
            if len(stack) == 0:
                print(f"stack is empty but found {char}")
                return False
            if stack[-1] == pairs[char]:
                print(f"found {char} and top of stack is {stack[-1]} which is a match")
                stack.pop()
            else:
                return False
    
    if len(stack) == 0:
        print("All brackets matched")
    else:
        print("Unmatched brackets letf")
        return False

                
isvalid("{}[]")