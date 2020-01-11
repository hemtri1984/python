###########################
# Author: Hemant Tripathi #
###########################


def main():
    print('Starting Sequential Search program!')
    dataArray = [25, 57, 48, 37, 12, 92, 86, 33]

    element = int(input('Enter the element you want to search: '))

    index = -1;
    elementFound = False
    for i in range(len(dataArray)):
        if dataArray[i] == element:
            elementFound = True
            index = i;
            break
    if(elementFound == True):
        print('Element Found at index: ', index)
    else:
        print('Element Not Found!')


if __name__ == "__main__":
    main()
