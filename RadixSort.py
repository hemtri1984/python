###########################
# Author: Hemant Tripathi #
###########################

def main():
    print('Starting program for Radix Sort')
    dataArray = [25, 57, 48, 37, 12, 92, 86, 33]
    maxDigit = getMax(dataArray)
    print('Max Digit in Array: ', maxDigit)
    exp = 1
    count = 0
    while(maxDigit//exp > 0): #double divide (//) will return int value, while single divide (/) will return float value
        count = count+1
        print("Pass : ", count)
        radixSort(dataArray, exp)
        exp = exp*10


def getMax(dataArray):
    maxVal = dataArray[0]
    for val in range(1, len(dataArray)):
        if(maxVal < dataArray[val]):
            maxVal = dataArray[val];
    return maxVal

def radixSort(arr, exp):
    count = [0,0,0,0,0,0,0,0,0,0]
    output = [None]*len(arr)

    for i in range(len(arr)): #calculating frequencies
        count[(arr[i]//exp)%10]+=1
    print('Frequencues of each indexes are : ', count)

    for i in range(1,10): #calculate Cumulative frequencies
        count[i] = count[i]+count[i-1]
    print('Cumulative frequencies of each index are: ', count)

    for i in range(len(arr)-1, -1, -1):
        output[(count[(arr[i]//exp)%10])-1] = arr[i]
        count[(arr[i]//exp)%10]-=1

    for i in range(len(arr)):
        arr[i] = output[i]
    print('After this iteration, sorted array is: ', arr)

if __name__ == "__main__":
    main()
