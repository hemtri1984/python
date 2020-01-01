############################
# Author: Hemant Tripathi  #
###########################

class ExpValidator:
    def __init__(self):
        self.myarray = []
        self.expression = ''

    def push(self, element):
        print('Stack Size: ', len(self.myarray));
        print('Pushed data: ', element)
        if(len(element) > 0):#insert element
            self.myarray.append(element)

    def pop(self, element):
        popElement = self.myarray[len(self.myarray)-1]
        if (element == ')' and popElement == '(') or (element == '}' and popElement == '{') or (element == ']' and popElement == '['):
            print('Popped element: ', popElement)
            self.myarray.pop()
            return True
        else:
            print('Closing brace does not match with open brace. Cannot popped')
            return False

    def peek(self):
        print('Stack peek element: ', self.myarray[len(self.myarray)-1])

    def isEmpty(self):
        if(len(self.myarray) <= 0):
            return True
        else:
            return False

    def stacksize(self):
        return len(self.myarray)

    def split(self, expression):
        return list(expression)


def main():
    print('------------------------------Expression Validator start -------------------------------------')
    expValidator = ExpValidator()
    expression = input('Enter the expression to validate: ')
    tokens = expValidator.split(expression)
    result = True
    for token in tokens:
        print('next token: ', token)
        if token == '(' or token == '{' or token == '[':
            expValidator.push(token)
        if token == ')' or token == '}' or token == ']':
            result = expValidator.pop(token)
            if(result == True):
                continue
            else:
                result = False
                break

    if result == True and expValidator.stacksize() == 0:
        print('Valid Expression')
    else:
        print('Invalid Expression')

    del expValidator
    del expression
    del result
    del token




if __name__ == "__main__":
    main()
