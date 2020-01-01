############################
# Author: Hemant Tripathi  #
###########################

class InfixToPostfix:
    def __init__(self):
        self.opstack = []
        self.postfixexp = '';

    def PushToOpStack(self, operator):
        print('Pushing Operator '+operator+' into OpStack');
        if operator == ')':#push all operators to postfix expression until ( will not found
            print('Add to Postfix expression until ( will not meet.')
            operator = self.PopFromOpStack();
            while operator != '(':
                print('Operator pushing into OpStack: ', operator)
                self.AddToPostfixExp(operator)
                operator = self.PopFromOpStack();
        else:
            print('Appending operator to opstack and check precedence.')
            self.opstack.append(operator)
            if(len(self.opstack) > 1):
                precedence = self.CheckPrecedence(self.opstack[len(self.opstack)-1], self.opstack[len(self.opstack)-2])
                if precedence == True:
                    poppedElement = self.PopFromOpStack()
                    self.AddToPostfixExp(self.PopFromOpStack())
                    self.PushToOpStack(poppedElement)


    def AddToPostfixExp(self, element):
        print('Adding element '+element+' to Postfix Expression')
        self.postfixexp = self.postfixexp + element;

    def PopFromOpStack(self):
        poppedElement = self.opstack[len(self.opstack)-1]
        print('Popping top element '+poppedElement+' from OpStack')
        self.opstack.pop()
        return poppedElement

    def CheckPrecedence(self, optop, nextop): #check if precedence of op1 is greater then nexttop element, return false.
        if optop == '(' or optop == '$' or optop == '^':
            return False #false means, don't do any operation. Its a normal case.
        elif (optop == '*' or optop == '/') and (nextop == "*" or nextop == '/' or nextop == '$' or nextop == '^'):
            return True #true means, top precedence is lower or equal to next top element. Now pop it and append to postfix expression
        elif (optop == '+' or optop == '-') and (nextop == '+' or nextop == '-' or nextop == '*' or nextop == '/' or nextop == '$'):
            return True
        else:
            return False

    def split(self, expression):
        return list(expression)

    def isOpStackEmpty(self):
        if len(self.opstack) > 0:
            return False
        else:
            return True


def main():
    infixToPostfixConverter = InfixToPostfix()
    print('----------------Infix to Post Conversion start -------------------')
    expression = input("Enter an Infix expression:  ")
    tokens = infixToPostfixConverter.split(expression)
    result = True;
    for token in tokens:
        print('next token: ', token)
        if token.isalpha() or token.isdigit():
            print(token + ' is operand. Pushing to PostfixExpression')
            infixToPostfixConverter.AddToPostfixExp(token)
        else:
            print(token + ' is operator. Pushing to OpStack')
            infixToPostfixConverter.PushToOpStack(token)

    print('Now pop all the OpStack operators into the postfix expression')
    while (infixToPostfixConverter.isOpStackEmpty() == False):
        infixToPostfixConverter.AddToPostfixExp(infixToPostfixConverter.PopFromOpStack())

    print('===================Final Postfix Expression=======================')
    print('Postfix Expression = ', infixToPostfixConverter.postfixexp)


if __name__ == "__main__":
        main()
