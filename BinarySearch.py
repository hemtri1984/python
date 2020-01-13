###########################
# Author: Hemant Tripathi #
###########################

def main():
    print('Starting program of binary search')
    print('Considering array is already in sorted ascending order')

    dataArray = [1,2,3,4,5,6,7,8,9,10];
    search = int(input('Enter the data you want to search: '))
    result = binarySearch(dataArray, search, 0, len(dataArray)-1)
    if result < 0:
        print('Data not found!')
    else:
        print('Data found at index: ', result)

def binarySearch(array, data, startIndex, endIndex):
    print('Start Index = '+str(startIndex)+'; endIndex = ', endIndex)
    middle = int((startIndex+endIndex)/2);
    if array[middle] == data:
        return middle
    if middle == startIndex and middle == endIndex:
        return -1
    if data < array[middle]:
        return binarySearch(array, data, startIndex, middle)
    else:
        return binarySearch(array, data, middle+1, endIndex)

if __name__ == "__main__":
    main()
