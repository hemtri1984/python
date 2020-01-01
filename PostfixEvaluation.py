############################
# Author: Hemant Tripathi  #
###########################


class PostfixEvaluation:
    def __init__(self):
        self.opstack = []
        self.result = 0;

    def PushToOpStack(self, operand):
        self.opstack.append(operand)
        print('Operand '+ str(operand) +' push to opstack at position: ',len(self.opstack))

    def PopFromStack(self):
        poppedElement = self.opstack[len(self.opstack)-1]
        print('Popped Element : ', poppedElement)
        self.opstack.pop()
        return poppedElement

    def IsOpStackEmpty(self):
        if len(self.opstack) > 0:
            return False
        else:
            return True

    def split(self, expression):
        return list(expression)

    def IsOperand(self, element):
        try:
            if int(element) >=0 and int(element) <= 9:
                return True
            else:
                return False
        except ValueError:
            return False

    def IsOperator(self, element):
        if element == '+' or element == '-' or element == '*' or element == '/' or element == '$' or element == '^':
            return True
        else:
            return False


def main():
    postfixEvaluator = PostfixEvaluation()
    expression = raw_input("Enter the Postfix Expression you want to evaluate:")
    tokens = postfixEvaluator.split(expression)
    for token in tokens:
        print ('Token : ', token)
        if postfixEvaluator.IsOperand(token) == True:
            print('Token '+token+' is an Operand.')
            postfixEvaluator.PushToOpStack(token)
        elif postfixEvaluator.IsOperator(token) == True: #Pop top to elements, perform the operation and push the result back to stack
            print('Token '+token+' is an Operator.')
            firstElement = int(postfixEvaluator.PopFromStack())
            secondElement = int(postfixEvaluator.PopFromStack())
            if token == '$' or token == '^':
                count = 0
                result = 1
                while count < firstElement:
                    result = result * secondElement
                    print('result = ', result)
                    count = count + 1
                secondElement = result
            elif token == '*':
                secondElement = firstElement * secondElement
            elif token == '/':
                secondElement = secondElement/firstElement
            elif token == '+':
                secondElement = firstElement + secondElement
            elif token == '-':
                secondElement = secondElement - firstElement

            postfixEvaluator.PushToOpStack(secondElement)
        else: #skip it
            print('Token '+token+' cannot be identified. Hence skipping')
            continue

    print('Postfix evaluation result : ', postfixEvaluator.PopFromStack())

if __name__ == "__main__":
    main()
