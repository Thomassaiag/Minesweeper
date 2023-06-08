import random


def createGrid(m, n):
    for _ in range(0, m):
        lines = ""
        content = ""
        for i in range(0, n):
            if i == n-1:
                content += "|"
                lines += "-"
            else:
                content += "|O"
                lines += "--"
        print(lines)
        print(content)


# createGrid(10,30)


def createGrid2(m, n):
    globalArray = []
    for _ in range(0, m):
        lineArray = []
        for _ in range(0, n):
            lineArray.append("O")
        globalArray.append(lineArray)
        # print(globalArray)
    print(globalArray)
    return globalArray


# createGrid2(4, 5)


def fillGrigWithX(tableToFill, k):
    kArray = []
    gridHeight = len(tableToFill)
    print(f"hauteur grille={gridHeight}")
    for _ in range(k):
        kArray.append("X")
    for i in range(0, gridHeight):
        print(f"i={i}")
        gridWidth = len(tableToFill[i])
        print(f"largeur grid:{gridWidth}")
        for j in range(0, gridWidth):
            print(f"j={j}")
            randInt = random.randint(1, gridHeight)
            print(f"randInt={randInt}")
            if randInt == 1 and tableToFill[i][j] != "X" and len(kArray)!=0:
                tableToFill[i][j] = "X"
                kArray.pop()
                print(f"longueur karray={len(kArray)}")
            

    print(tableToFill)
    return tableToFill


fillGrigWithX(createGrid2(4, 5), 5)
