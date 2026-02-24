class myStack:

    #CONSTRUCTOR
    def __init__(self, cap):
        self.capacity = cap
        self.arr = [0] * self.capacity
        self.top = -1

    #push operation
    def push(self, x):
        if self.top == self.capacity:
            print("Stack overflow")
            return 
        self.top += 1
        self.arr[self.top] = x

    #pop operation
    def pop(self):
        if self.top == -1:
            print("stack underflow")
            return -1
        val = self.arr[self.top]
        self.top -= 1
        return val
    
    #peek operation
    def peek(self):
        if self.top == -1:
            print("stack is empty")
            return -1
        
        return self.arr[self.top]
    
    #check if stack is empty
    def isEmpty(self):
        return self.top == -1
    

    #check if stack is full
    def isFull(self):
        return self.top == self.capacity - 1
    
if __name__ == "__main__":
    st = myStack(4)

    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)

    # popping one element
    print("Popped:", st.pop())

    # checking top element
    print("Top element:", st.peek())

    # checking if stack is empty
    print("Is stack empty: ", "Yes" if st.isEmpty() else "No")

    # checking if stack is full
    print("Is stack full: ", "Yes" if st.isFull() else "No")