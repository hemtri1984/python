###########################
# Author: Hemant Tripathi #
###########################

class PrefixToPostfix:
    def __init__(self):
        self.OpStack = []
        self.postfixexp = ''

    def IsOperator(self, element):
        if element == '+' or element == '-' or element == '*' or element == '/' or element == '$' or element == '^':
            return True
        else:
            return False

    def PushToOpStack(self, element):
        if self.IsOperator(element) == True:
            print('Its and operator. Do evaluation operation');
            #Make its postfix expression with last to element and push it back
            firstElement = self.PopFromOpStack()
            secondElement = self.PopFromOpStack()
            self.PushToOpStack(firstElement + secondElement + element)
        else: #Push the element into Stack
            print('Its an operand. Push to OpStack')
            self.OpStack.append(element)

    def PopFromOpStack(self):
        if(len(self.OpStack) > 0): #Pop and return the last element
            poppedElement =  self.OpStack[len(self.OpStack) - 1]
            print('Popped Element = ', poppedElement)
            self.OpStack.pop()
            return poppedElement;
        else:
            print('Stack is Empty')
            return -1;

    def split(self, expression):
        return list(expression)

    def reverseArray(self, tokens):
        arrLength = len(tokens)
        for count in range(int(arrLength/2)):
            tmp = tokens[count];
            tokens[count] = tokens[arrLength-count-1]
            tokens[arrLength-count-1] = tmp

        return tokens;




def main():
    print('###################  Start of Prefix to Postfix Conversion  ###############')
    preToPostConverter = PrefixToPostfix()
    expression = input("Enter the Prefix Expression:")
    tokens = preToPostConverter.split(expression)
    tokens = preToPostConverter.reverseArray(tokens)
    for token in tokens:
        print('token = ', token)
        preToPostConverter.PushToOpStack(token)

    print('Conversion to Postfix done.')
    print('Final Result: ', preToPostConverter.PopFromOpStack())


if __name__ == "__main__":
    main()
