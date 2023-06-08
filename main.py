import random


def displayGrid(table):
    tableHeight=len(table)
    for row in range(0, tableHeight):
        lines = ""
        content = str(int(row)+1)
        tableWith=len(table[row])
        for column in range(0, tableWith+1):
            if column == tableWith:
                content += "|"
                lines += "-"
            else:
                content += "|"+table[row][column]
                lines += "--"
        print(lines)
        print(content)
    print(lines)
    print(lines)
    content=""
    for column in range(0, tableWith+1):
        content+=str(column)+"|"
    print(content)


def displayHollowGrid(table):
    tableHeight=len(table)
    for row in range(0, tableHeight):
        lines = ""
        content = str(int(row)+1)
        tableWith=len(table[row])
        for column in range(0, tableWith+1):
            if column == tableWith:
                content += "|"
                lines += "-"
            else:
                content += "|"+"_"
                lines += "--"
        print(lines)
        print(content)
    print(lines)
    print(lines)
    content=""
    for column in range(0, tableWith+1):
        content+=str(column)+"|"
    print(content)

# createGrid(10,30)


def createGrid(m, n):
    globalArray = []
    for _ in range(0, m):
        lineArray = []
        for _ in range(0, n):
            lineArray.append("O")
        globalArray.append(lineArray)
        # print(globalArray)
    return globalArray


def fillGrigWithX(tableToFill, k):
    kArray = []
    gridHeight = len(tableToFill)
    for _ in range(k):
        kArray.append("X")
    while len(kArray)>0:
        for i in range(0, gridHeight):
            gridWidth = len(tableToFill[i])
            for j in range(0, gridWidth):
                randInt = random.randint(1, gridHeight)
                if randInt == 1 and tableToFill[i][j] != "X" and len(kArray)!=0:
                    tableToFill[i][j] = "X"
                    kArray.pop()
                    print(f"longueur karray={len(kArray)}")
    print(tableToFill)
    return tableToFill


displayGrid(fillGrigWithX(createGrid(9, 9), 10))

displayHollowGrid(fillGrigWithX(createGrid(9, 9), 10))
