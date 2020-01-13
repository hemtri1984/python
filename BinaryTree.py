###########################
# Author: Hemant Tripathi #
###########################


class Node:
    def __init__(self, info = None):
        self.info = info
        self.left = None
        self.right = None

    def printInfo(self):
        print(self.info)

    def isLeft(self):
        if self.left != None:
            return True
        else:
            return False

    def isRight(self):
        if self.right != None:
            return True
        else:
            return False

class BinaryTree:
    def __init__(self):
        self.root = None


def main():
    binaryTree = BinaryTree()
    print('Starting Binary tree operations............................')
    while(1):
        print('Please select an option:')
        print('1. Insert a node into tree')
        print('2. Show all Nodes of tree into Inorder form')
        print('3. Show all Nodes of tree into Preorder form')
        print('4. Show all Nodes of tree into Postorder form')
        print('5. Search and element in BST')
        print('6. Exit')

        selection = int(input())
        if selection == 1:
            print('Enter the data to insert into the tree')
            infoData = int(input())
            if (binaryTree.root == None):
                print('No Tree nodes found! Create the root node')
                binaryTree.root = Node(infoData)
                print('Root node created')
            else:
                if infoData >= binaryTree.root.info:
                    print('Greater than or equal to parent node. Moving to the right of tree')
                    binaryTree.root.right = InsertOp(binaryTree.root.right, infoData)
                else:
                    print('Less than parent node. Moving to the left of tree')
                    binaryTree.root.left = InsertOp(binaryTree.root.left, infoData)

        elif selection == 2:
            print('Traversing the tree into Inorder form')
            showInorder(binaryTree.root)

        elif selection == 3:
            print('Traversing the tree into Preorder form')
            showPreOrder(binaryTree.root)

        elif selection == 4:
            print('Traversing the tree into Postorder form')
            showPostOrder(binaryTree.root)

        elif selection == 5:
            element = int(input('Enter the element you want to search in BST: '))
            searchNode = searchBST(binaryTree.root, element)
            if searchNode == None:
                print('Element not found!')
            else:
                print('Element found!')

        else:
            print('########### Terminating the program  ##############')
            del binaryTree
            break

def InsertOp(parentNode, infoData):
    if parentNode == None:
        print('No node found! Creating new node')
        parentNode = Node(infoData)
    else:
        if infoData >= parentNode.info:
            print('Node found! Inserting to right of this node. currentNode = ', parentNode.info)
            parentNode.right = InsertOp(parentNode.right, infoData)
        else:
            print('Node found! Inserting to left of this node. Current node = ', parentNode.info)
            parentNode.left = InsertOp(parentNode.left, infoData)
    return parentNode

def showInorder(parentNode):
    if(parentNode.isLeft()):
        showInorder(parentNode.left)
    parentNode.printInfo()
    if(parentNode.isRight()):
        showInorder(parentNode.right)

def showPreOrder(parentNode):
    parentNode.printInfo()
    if(parentNode.isLeft()):
        showPreOrder(parentNode.left)
    if(parentNode.isRight()):
        showPreOrder(parentNode.right)

def showPostOrder(parentNode):
    if(parentNode.isLeft()):
        showPostOrder(parentNode.left)
    if(parentNode.isRight()):
        showPostOrder(parentNode.right)
    parentNode.printInfo()

def searchBST(parentNode, data):
    if parentNode == None:
        return parentNode
    else:
        while parentNode != None and data != parentNode.info:
            if data < parentNode.info:
                parentNode = parentNode.left
            else:
                parentNode = parentNode.right
        return parentNode

if __name__ == "__main__":
    main()
