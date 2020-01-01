###########################
# Author: Hemant Tripathi #
###########################

def htower(disks, fromTower, toTower, auxTower):
    if disks == 1:
        print("Move Disk " + str(disks) + " from Tower" + fromTower + " to Tower" + toTower)
        return
    else:
        htower(disks-1, fromTower, auxTower, toTower)
        print("Move Disk " + str(disks) + " from Tower" + fromTower + " to Tower" + toTower)
        htower(disks-1, auxTower, toTower, fromTower)


def main():
    disks = input("Enter total number of disks less than 10: ");
    if int(disks) < int(1):
        print('Invalid Input')
    elif int(disks) > int(10):
        print('Memory Overflow')
    else:
        htower(int(disks), 'A', 'B', 'C')



if __name__ == "__main__":
    main()
