/**
* Author: Hemant Tripathi
*/

class Stack:
    def __init__(self):
        self.mystack = []

    def isEmpty(self):
        print('Is Stack Empty: ', self.mystack == [])

    def push(self, element):
        self.mystack.append(element);
        print('Element added to stack: ',element)

    def pop(self):
        if(len(self.mystack) <= 0):
            print(('Stack is Empty. Cannot pop element'))
        else:
            print('Popping element: ', self.mystack[len(self.mystack)-1])
            self.mystack.pop();

    def show(self):
        print('Current stack is: ', self.mystack)

    def showPeek(self):
        print('Current Peek element is : ', self.mystack[len(self.mystack)-1])

    def stackSize(self):
        print('Size of Stack: ', len(self.mystack))


def main():
    stack = Stack()
    while(1):
        print('\n\nSelect an Option:\n')
        print('1. Push an Element')
        print('2. Pop an Element')
        print('3. Show Stack Elements')
        print('4. Check if Stack is Empty')
        print('5. Show Peek Element')
        print('6. Stack  Size')
        print('7. Exit')

        val = int(input()) # by default it input as a string, you need to cast it to integer
        if(val == 1):
            element = input('Enter the element to push: ')
            stack.push(element)
            continue
        elif(val == 2):
            print('Popping an element from stack')
            stack.pop()
        elif (val == 3):
            print('stack elements are:')
            stack.show()
        elif (val == 4):
            stack.isEmpty()
        elif (val == 5):
            print('Peek Element is:')
            stack.showPeek()
        elif (val == 6):
            print('size of stack is:')
            stack.stackSize()
        elif(val == 7):
            del stack
            del val;
            break
        else:
            print('Invalid input. Please enter a number between 1 to 7')


if __name__ == "__main__":
    main()
