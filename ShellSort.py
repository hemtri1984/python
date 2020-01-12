###########################
# Author: Hemant Tripathi #
###########################


def main():
    print('Starting Shell Sort program')

    dataArray = [25, 57, 48, 37, 12, 92, 86, 33]

    gap = int(len(dataArray)/2)
    while gap > 0:
        print('Gap = ', gap)

        for i in range(gap, len(dataArray)):
            tmp = dataArray[i]
            print('i = '+str(i)+'; Temp Value : ', tmp)

            j = i
            while j >= gap and dataArray[j-gap] > tmp:
                dataArray[j] = dataArray[j-gap]
                j = j - gap
            dataArray[j] = tmp

        print('After iteration data array is : ', dataArray)
        gap = int(gap/2)

    print('################ Result #######################')
    print('Shell Sorting completed. Result: ', dataArray)


if __name__ == "__main__":
    main()
