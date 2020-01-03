###########################
# Author: Hemant Tripathi #
###########################

class CircularQueue:
    def __init__(self):
        self.MAXQSIZE = 5
        self.cQueue = [0]*self.MAXQSIZE
        self.rear = self.MAXQSIZE - 1
        self.front = self.MAXQSIZE - 1

    def insertIntoQueue(self, element):
        print('Inserting element '+element+' into circular queue')
        if self.isOverflow():
            print('Buffer overflow! Cannot insert.')
        else:
            if self.rear == self.MAXQSIZE - 1:
                self.rear = 0
            else:
                self.rear = self.rear + 1
            print('Inserting element into position: ', self.rear)
            self.cQueue[self.rear] = element
            print('Element '+element+' inserted successfully at position: ', self.rear)

    def removeFromQueue(self):
        print('Removing and element from circular queue')
        if(self.isEmpty()) :
            print('Queue is Empty! Pop operation not possible.')
        else:
            if self.front == self.MAXQSIZE-1:
                self.front = 0
            else:
                self.front = self.front+1
            print('Popped Element : ', self.cQueue[self.front])
            print('Element popped successfully from position: ', self.front)

    def getFirstElement(self):
        if(self.isEmpty()):
            print('No element found! Empty Queue.')
            return -1
        else:
            firstElementPosition = 0;
            if self.front == self.MAXQSIZE-1:
                firstElementPosition = 0;
            else:
                firstElementPosition = self.front + 1;
            print('First Element is : ', self.cQueue[firstElementPosition])

    def getFirstElementPosition(self):
        if(self.isEmpty()):
            print('No element found! Empty Queue.')
            return -1
        else:
            firstElementPosition = 0;
            if self.front == self.MAXQSIZE-1:
                firstElementPosition = 0;
            else:
                firstElementPosition = self.front + 1;
            print('First Element position is: ', firstElementPosition)

    def getLastElement(self):
        if(self.isEmpty()):
            print('No element found! Empty Queue.')
            return -1
        else:
            print('Last Element is : ', self.cQueue[self.rear])

    def getLastElementPosition(self):
        if(self.isEmpty()):
            print('No element found! Empty Queue.')
            return -1
        else:
            print('Last element position is: ', self.rear)

    def isEmpty(self):
        print('Check if circular queue is empty')
        if self.rear == self.front:
            return True
        else:
            return False


    def isOverflow(self):
        print('Check if circular queue is overflow')
        if (self.rear == self.MAXQSIZE-1 and self.front == 0) or (self.rear == self.front - 1) :
            return True
        else:
            return False

    def showElements(self):
        print('Show all elements of queue')
        if self.front < self.rear:
            for count in range(self.front+1, self.rear+1):
                print('Element '+self.cQueue[count]+' at position: ', count)
        elif self.rear < self.front:
            for count in range(self.front + 1, self.MAXQSIZE-1):
                print('Element '+self.cQueue[count]+' at position: ', count)
            for count in range(0, self.rear+1):
                print('Element '+self.cQueue[count]+' at position: ', count)
        else:
            print('Its an Empty Queue')

    def totalCount(self):
        print('Show total count of elements in queue')
        totalElements = 0
        if self.front < self.rear:
            print('first if case: front = '+str(self.front)+'; rear = '+str(self.rear))
            totalElements = totalElements + self.rear - self.front
            print('After first total elements : ', totalElements)
        elif self.rear < self.front:
            print('second if case: front = '+str(self.front)+'; rear = '+str(self.rear))
            totalElements = totalElements + self.MAXQSIZE-self.front-1
            totalElements = totalElements + self.rear
            print('After second total elements : ', totalElements)
        else:
            print('Its an Empty Queue')
        print('Total Elements = ',totalElements)


def main():
    print('************ Starting Circular Queue operation *****************')
    cQueue = CircularQueue()
    while(1):
        print('\n\nSelect an Option:\n')
        print('1. Insert element')
        print('2. Remove an element')
        print('3. Get first Element')
        print('4. Get first element position')
        print('5. Get last element')
        print('6. Get last element position')
        print('7. Get total element in queue')
        print('8. Show all element in circular queue')
        print('9. Exit')

        val = int(input()) # by default it input as a string, you need to cast it to integer
        if val == 1:
            element = input('Enter the element to insert: ')
            cQueue.insertIntoQueue(element)
        elif val == 2:
            cQueue.removeFromQueue()
        elif val == 3:
            cQueue.getFirstElement()
        elif val == 4:
            cQueue.getFirstElementPosition()
        elif val == 5:
            cQueue.getLastElement()
        elif val == 6:
            cQueue.getLastElementPosition()
        elif val == 7:
            cQueue.showElements()
        elif val == 8:
            cQueue.totalCount()
        elif val == 9:
            print('########### Aborting the program  ##############')
            del cQueue;
            break
        else:
            print('Invalid input. Please enter a number between 1 to 7')


if __name__ == "__main__":
    main()
