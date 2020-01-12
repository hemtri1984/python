###########################
# Author: Hemant Tripathi #
###########################


def main():
    print('Starting program of Merge Sort')
    dataArray = [25, 57, 48, 37, 12, 92, 86, 33]
    mergeSort(dataArray, 0, len(dataArray)-1)

def mergeSort(arr, lb, ub):
    if arr[lb] == arr[ub]:
        return

    low1 = lb
    high1 = int((lb+ub)/2)
    low2 = high1+1
    high2 = ub
    print('Low1 : '+str(low1)+'; High1: '+str(high1)+'; low2: '+str(low2)+'; high2: ', high2)
    mergeSort(arr, low1, high1)
    mergeSort(arr, low2, high2)

    totalLength = high2 - low1 + 1
    print('Total Length = ', totalLength)
    tempArr = [None]*totalLength
    i = low1
    j = low2
    count = 0
    print('High1 = '+str(high1)+'; high2 = ', high2)
    while i <= high1 and j <= high2:
        print('i = '+str(i)+'; j = ',j)
        if arr[i] > arr[j]:
            print('IF Case >>>>>>>>>>> tempArr['+str(count)+'] = arr['+str(j)+']')
            tempArr[count] = arr[j]
            count = count+1
            j = j+1
        else:
            print('Else Case >>>>>>>>>> tempArr['+str(count)+'] = arr['+str(i)+']')
            tempArr[count] = arr[i]
            count = count+1
            i = i+1

    print('i = '+str(i)+'; high1 = ',high1)
    while i <= high1:
        print('>tempArr['+str(count)+'] = arr['+str(i)+']')
        tempArr[count] = arr[i]
        count = count+1
        i = i+1
    while j <= high2:
        print('>>tempArr['+str(count)+'] = arr['+str(j)+']')
        tempArr[count] = arr[j]
        count = count+1
        j = j+1

    #Now move all the sorted elements into the main array list
    for i in range(totalLength):
        arr[low1] = tempArr[i]
        low1 = low1+1
    print('After next iteration, Array = ', arr)


if __name__ == "__main__":
    main()
