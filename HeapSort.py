###########################
# Author: Hemant Tripathi #
###########################


def main():
    print('Starting Heap Sort program')
    dataArray = [25, 57, 48, 37, 12, 92, 86, 33, 40]

    for i in range(int(len(dataArray)/2)-1, 0, -1):
        heapify(dataArray, len(dataArray), i)

    #Now extract one by one element from the top of heap
    for i in range(len(dataArray)-1, 0, -1):
        tmp = dataArray[0]
        dataArray[0] = dataArray[i]
        dataArray[1] = tmp

        #Heapify the array again
        heapify(dataArray, i, 0)

    print('################### Result #########################')
    print('After Heap Sort operation. Sorted array is: ', dataArray)


def heapify(dataArray, totalNodes, fatherNode):
    largestNode = fatherNode;
    leftChild = largestNode*2 + 1
    rightChild = largestNode*2 + 2

    print('Largest Node Position: '+str(largestNode)+'; Left Child Position: '+str(leftChild)+'; Right Child Position: '+str(rightChild)+'; fatherNode: ', fatherNode)

    if leftChild < totalNodes and dataArray[leftChild] > dataArray[largestNode]:
        print('Left child is greater than father')
        largestNode = leftChild

    if rightChild < totalNodes and dataArray[rightChild] > dataArray[largestNode]:
        print('Right child is greater than father')
        largestNode = rightChild

    if largestNode != fatherNode: #Swap largest node and father nodes elements
        print('Swapping largest node and father node elements')
        temp = dataArray[largestNode]
        dataArray[largestNode] = dataArray[fatherNode]
        dataArray[fatherNode] = temp

        print('Heapify total node: '+str(totalNodes)+'; and largest node position: '+str(largestNode)+'; largest node is : ', dataArray[largestNode])
        heapify(dataArray, totalNodes, largestNode)

if __name__ == "__main__":
    main()
