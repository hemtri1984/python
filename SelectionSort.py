###########################
# Author: Hemant Tripathi #
###########################


def main():
    print('Starting Selection Sort program')
    print('Ascending Selection Sort')
    dataArray = [25, 57, 48, 37, 12, 92, 86, 33]

    for i in range(len(dataArray)-1):
        minIndex = i;
        for j in range(i+1, len(dataArray)):
            if dataArray[minIndex] > dataArray[j]:
                minIndex = j
        #Swap i th and minIndex elements
        tmp = dataArray[minIndex];
        dataArray[minIndex] = dataArray[i]
        dataArray[i] = tmp
        print('After next iteration, Array is: ', dataArray)
    print('################### Result ############################')
    print('After Selection Sort operation, array is: ', dataArray)


if __name__ == "__main__":
    main()
