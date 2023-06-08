import random


def displayGrid(table):
    tableHeight = len(table)
    for j in range(0, tableHeight):
        lines = ""
        content = ""
        tableWith = len(table[j])
        for i in range(0, tableWith+1):
            if i == tableWith:
                content += "|"
                lines += "-"
            else:
                content += "|"+table[j][i]
                lines += "--"
        print(lines)
        print(content)
    print(lines)

# createGrid(10,30)


def createGrid(m, n):
    globalArray = []
    for _ in range(0, m):
        lineArray = []
        for _ in range(0, n):
            lineArray.append("O")
        globalArray.append(lineArray)
        # print(globalArray)
    print(globalArray)
    return globalArray


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
            if randInt == 1 and tableToFill[i][j] != "X" and len(kArray) != 0:
                tableToFill[i][j] = "X"
                kArray.pop()
                print(f"longueur karray={len(kArray)}")

    print(tableToFill)
    return tableToFill


displayGrid(fillGrigWithX(createGrid(4, 5), 5))
