###########################
# Author: Hemant Tripathi #
###########################

global swapping;
def main():
    print('Starting program for bubble sorting')
    dataArray = [25, 57, 48, 37, 12, 92, 86, 33]
    swapping = True
    for i in range(len(dataArray)):
        if(swapping == True):
            swapping = False
            for j in range((len(dataArray) - i - 1)):
                if dataArray[j] > dataArray[j+1]:
                    dataArray[j] = dataArray[j] + dataArray[j+1];
                    dataArray[j+1] = dataArray[j] - dataArray[j+1];
                    dataArray[j] = dataArray[j] - dataArray[j+1];
                    swapping = True
            print('After ' +str(i+1)+ ' iteration : ', dataArray)
        else:
            break

    print('Bubble Sorting program executed Successfully >>>>>>>>>>>>>>>>')
    print('Sorted Array: ', dataArray)

if __name__ == "__main__":
    main()
