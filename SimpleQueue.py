###########################
# Author: Hemant Tripathi #
###########################

class Queue:
    def __init__(self):
        self.MAXQUEUESIZE = 10
        self.myQueue = []
        self.rear = -1
        self.front = 0

    def insertIntoQueue(self, element):
        if self.rear < self.MAXQUEUESIZE-1:
            self.rear = self.rear + 1
            self.myQueue.append(element)
            print('Element '+element+' is inserted into position ', self.rear)
        else:
            print('Queue is overflow')

    def removeFromQueue(self):
        if self.isEmpty() == True:
            print('Empty Queue')
        else:
            removedElement = self.myQueue[self.front]
            self.front = self.front + 1;
            return removedElement;

    def isEmpty(self):
        if self.rear < self.front:
            return True
        else:
            return False;

    def getTotalElements(self):
        return self.rear - self.front + 1;

    def showAllElements(self):
        for count in range(self.getTotalElements()):
            print('Element ' + self.myQueue[self.front + count] + ' at position: ', self.front + count)


def main():
    print('************ Starting Simple Queue operation *****************')
    queue = Queue()
    while(1):
        print('\n\nSelect an Option:\n')
        print('1. Insert an Element')
        print('2. Remove an Element')
        print('3. Get First Element of Queue')
        print('4. Get Last Element of Queue')
        print('5. Show all elements of queue')
        print('6. Queue Size')
        print('7. Exit')

        val = int(input()) # by default it input as a string, you need to cast it to integer
        if(val == 1):
            element = input('Enter the element to insert: ')
            queue.insertIntoQueue(element)
        elif(val == 2):
            print('Removing an element from queue')
            print('Removed element: ', queue.removeFromQueue());
        elif (val == 3):
            if queue.isEmpty() == True:
                print('Queue is Empty.')
            else:
                print('first Element of queue is: ', queue.myQueue[queue.front])
        elif (val == 4):
            if queue.isEmpty() == True:
                print('Queue is Empty.')
            else:
                print('Last Element of queue is: ', queue.myQueue[queue.rear])
        elif (val == 5):
            if queue.isEmpty() == True:
                print('Queue is Empty.')
            else:
                queue.showAllElements();
        elif (val == 6):
            print('size of queue is:', queue.getTotalElements())
        elif(val == 7):
            print('########### Aborting the program  ##############')
            del queue;
            break
        else:
            print('Invalid input. Please enter a number between 1 to 7')


if __name__ == "__main__":
    main()
