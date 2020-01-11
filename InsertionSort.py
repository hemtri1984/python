###########################
# Author: Hemant Tripathi #
###########################


def main():
    print('Starting program for Insertion Sort')

    dataArray = [25, 57, 48, 37, 12, 92, 86, 33]

    for i in range(1, len(dataArray)):
        for j in range(i, 0, -1):
            print('Comparing between : '+str(dataArray[j])+' and ', dataArray[j-1])
            if dataArray[j] < dataArray[j-1]:
                tmp = dataArray[j]
                dataArray[j] = dataArray[j-1]
                dataArray[j-1] = tmp
                del tmp
            else:
                break
        print('After next iteration, dataArray is: ', dataArray)
    print('##################### Result ####################')
    print('After Insertion Sort operation, Sorted array is: ', dataArray)



if __name__ == "__main__":
    main()
