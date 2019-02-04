if __name__ == '__main__':
    testAmount = int(input())
    while testAmount > 0:
        firstSetSize = int(input())
        firstSet = list(map(int, input().split()))
        secondSetSize = int(input())
        secondSet = list(map(int, input().split()))

        yay = True

        for number in firstSet:
            if secondSet.count(number) == 0:
                print ("False")
                yay = False
                break
        if yay:
            print ("True")
    testAmount -= 1
