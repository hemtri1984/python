###########################
# Author: Hemant Tripathi #
###########################


def main():
    print('############### Quick Sort Program ####################')
    dataArray = [25, 57, 48, 37, 12, 92, 86, 33]
    quickSort(dataArray, 0, len(dataArray)-1)

    print('####################### Result ##############################')
    print('After quickSort operation completed, Array : ', dataArray)


def quickSort(dataArray, lowerBound, upperBound):
    print('lowerBound = '+str(lowerBound)+'; upperBound = ', upperBound)
    a = dataArray[lowerBound]
    down = lowerBound
    up = upperBound


    while down < up:
        while dataArray[down] <= a and down < upperBound:
            down = down + 1

        while dataArray[up] > a:
            up = up - 1

        if down < up:
            #swap down and up position elements
            tmp = dataArray[down]
            dataArray[down] = dataArray[up]
            dataArray[up] = tmp

    #now swap a with upperBound eleemnt
    dataArray[lowerBound] = dataArray[up]
    dataArray[up] = a

    print('After next iteration, array is : ', dataArray)

    if down < upperBound:
        quickSort(dataArray, up+1, upperBound)
    if up > lowerBound:
        quickSort(dataArray, lowerBound, up-1)

if __name__ == "__main__":
    main()
