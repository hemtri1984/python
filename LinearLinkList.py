###########################
# Author: Hemant Tripathi #
###########################

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinearLinkList:
    def __init__(self):
        self.header = None


def main():
    linkList = LinearLinkList()
    print('Starting LinearLinkList operations.................')
    while(1):
        print('Please select an option:')
        print('1. Add a node to the beginning of the list')
        print('2. Add a node into the middle of the list')
        print('3. Add a node into the end of the list')
        print('4. Remove a node from the beginning of the list')
        print('5. Remove a node from the middle of the list')
        print('6. Remove a node from the end of the list')
        print('7. Show all nodes of the list')
        print('8. Exit')

        selection = int(input())
        if selection == 1:
            print('Enter the data into new node')
            data = input()
            if(linkList.header == None):
                print('No Linklist found. Creating first node of list')
                linkList.header = Node(data)
                print('Linklist first node created')
            else:
                newNode = Node(data)
                newNode.next = linkList.header
                linkList.header = newNode
                print('Added new node at the beginning of list')

        elif selection == 2:
            print('Enter the data into new node')
            data = input()
            if(linkList.header == None):
                print('No Linklist found. Creating first node of list')
                linkList.header = Node(data)
                print('Linklist first node created')
            else:
                newNode = Node(data)
                print('Enter the position of this node in the list')
                limitException = False
                position = int(input())
                if(position > 0):
                    tmpNode = linkList.header
                    for counter in range(0, position-1):
                        if tmpNode.next is None:
                            limitException = True
                            print('Error: IndexOutOfBound, position must be less than linklist range')
                            break
                        tmpNode = tmpNode.next
                    if limitException == False:
                        newNode.next = tmpNode.next
                        tmpNode.next = newNode
                        print('New Node is inserted into link list')
                else:
                    print('Node position must be greater than zero')

        elif selection == 3:
            print('Enter the data into new node')
            data = input()
            if(linkList.header == None):
                print('No Linklist found. Creating first node of list')
                linkList.header = Node(data)
                print('Linklist first node created')
            else:
                newNode = Node(data)
                tmpNode = linkList.header
                count = 0;
                while tmpNode.next is not None:
                    count = count + 1
                    tmpNode = tmpNode.next
                tmpNode.next = newNode
                print('Added new node at position : ', count)

        elif selection == 4:
            print('Removing the node from the beginning of the list')
            if linkList.header is None:
                print('No linklist found!')
            elif linkList.header.next is None:
                linkList.header = None
            else:
                tmp = linkList.header
                linkList.header = linkList.header.next
                tmp.next = None
                del tmp
            print('Removed the first node from linkList')

        elif selection == 5:
            if linkList.header is None:
                print('No linklist found!')
            else:
                limitException = False
                tmp = linkList.header
                tmp1 = linkList.header.next
                print('Enter the position of the node you want to remove')
                position = int(input())
                for count in range(0, position-1):
                    if tmp1 is None:
                        limitException = True
                        print('Error: IndexOutOfBound, position must be less than linklist range')
                        break
                    tmp = tmp.next
                    tmp1 = tmp1.next
                tmp.next = tmp1.next
                tmp1.next = None
                del tmp1

        elif selection == 6:
            print('Removing the node from the end of the list')
            if linkList.header is None:
                print('No linklist found!')
            else:
                tmp = linkList.header
                tmp1 = linkList.header.next
                while tmp1.next is not None:
                    tmp = tmp.next
                    tmp1 = tmp1.next
                tmp.next = None
                del tmp1

        elif selection == 7:
            print('Calculating all nodes of the link list')
            if linkList.header is None:
                print('No linklist found!')
            else:
                tmpNode = linkList.header
                count = 0;
                while tmpNode is not None:
                    count = count + 1
                    print('Next node Value: '+tmpNode.data+' At position: ', count)
                    tmpNode = tmpNode.next
                print('Total Nodes : ', count)

        elif selection == 8:
            print('########### Terminating the program  ##############')
            del linkList
            break
        else:
            print('Invalid input. Please enter a number between 1 to 8')


if __name__ == "__main__":
    main()
