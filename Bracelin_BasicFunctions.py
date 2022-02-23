def formula(apo,numSide,sideLen):
    perim = numSide * sideLen

    area  =(apo*perim) / 2
    return area


def main():
    numberSides = 5
    sideLength = 10
    apothem = 12.5
    print('the area of your regular polygon with ' + str(numberSides) +  '  sides is ' + str(formula(apothem,numberSides,sideLength)) + ' units squared.')




main()
