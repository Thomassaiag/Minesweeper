import random

tableWithXGrid=[]

#affichage de n'importe quelle grille prenant en paramètre n'importe quel tableau
def displayGrid(genericTable):
    tableHeight = len(genericTable)
    for row in range(0, tableHeight):
        #initialisation des 1ères valeurs de colonne et de ligne (avec le numéro de ligne pour cette dernière)
        lines = " "
        content = str(int(row)+1)
        tableWidth = len(genericTable[row])
        for column in range(0, tableWidth+1):
            #remplissage de la grille avec le contenu du tableau donné en paramètre
            #forçage des dernières valeurs des lignes et de colonne
            if column == tableWidth:
                content += "|"
                lines += "-"
            else:
                content += "|"+genericTable[row][column]
                lines += "--"
        print(lines)
        print(content)
    print(lines)
    content = ""
    #affichage des index de colonne pour mieux se repérer
    for column in range(0, tableWidth+1):
        content += str(column)+"|"
    print(content)


#création d'un tableau de dimensions m,n, rempli de "filler" donné en paramètre
def createGridTable(m, n, filler):
    globalArray = []
    for _ in range(0, m):
        lineArray = []
        for _ in range(0, n):
            lineArray.append(filler)
        globalArray.append(lineArray)
    return globalArray



#remplissage du tableau généré dans createGridTable avec k bombes, réparties de manière aléatoire
def fillGridTableWithX(tableToFill, k):
    gridHeight = len(tableToFill)
    #intialisation d'un tableau contenant les bombes à placer
    kArray = []
    for _ in range(k):
        kArray.append("X")
    #tant que le tableau des bombes en contient, on essaye de placer des bombes de manière aléatoire, si la case n'en contient pas déjà une
    #on vide le tableau de la bombe qu'on a placée.
    while len(kArray) > 0:
        for i in range(0, gridHeight):
            gridWidth = len(tableToFill[i])
            for j in range(0, gridWidth):
                randInt = random.randint(1, gridHeight)
                if randInt == 1 and tableToFill[i][j] != "X" and len(kArray) != 0:
                    tableToFill[i][j] = "X"
                    kArray.pop()
                    # print(f"longueur karray={len(kArray)}")
    global tableWithXGrid
    tableWithXGrid=tableToFill# print(tableToFill)
    return tableWithXGrid


def revealTable(tableToReveal,hCoord,wCoord):
    global tableWithXGrid
    tableToReveal[int(hCoord)-1][int(wCoord)-1]=tableWithXGrid[int(hCoord)-1][int(wCoord)-1]
    return tableToReveal


gridHeight=9
gridWidth=9
minesNumber = 10
hCoordinate=0
wCoordinate=0


emptyGridTable = createGridTable(gridHeight, gridWidth,"O")
fillGridTableWithX(emptyGridTable, minesNumber)
gridToGuess=displayGrid(tableWithXGrid)

neutralGridTable = createGridTable(gridHeight, gridWidth,"_")
neutralGrid=displayGrid(neutralGridTable)


gridSize=gridHeight*gridWidth
i=1
while i<gridSize:
    hCoordinate = input(f"Choisissez la coordonnée Verticale (entre 1 et {gridHeight}) : ")
    wCoordinate = input(f"Choisissez la coordonnée horizontale (entre 1 et {gridWidth}) : ")
    table=revealTable(neutralGridTable,hCoordinate,wCoordinate)
    displayGrid(table)
    




#affiche la table neutre, sans les cases vides ou les bombes, appelée une seule fois au début du jeu
# def displayEmptyGrid(table):
#     tableHeight = len(table)
#     for row in range(0, tableHeight):
#         lines = " "
#         content = str(int(row)+1)
#         tableWidth = len(table[row])
#         for column in range(0, tableWidth+1):
#             if column == tableWidth:
#                 content += "|"
#                 lines += "-"
#             else:
#                 content += "|"+"_"
#                 lines += "--"
#         print(lines)
#         print(content)
#     print(lines)
#     content = ""
#     for column in range(0, tableWidth+1):
#         content += str(column)+"|"
#     print(content)




#affiche la table à révéler, pour les tests au début
# def displayTrueGrid(arrayWithBombs):
#     tableHeight = len(arrayWithBombs)
#     for row in range(0, tableHeight):
#         lines = " "
#         content = str(int(row)+1)
#         tableWidth = len(arrayWithBombs[row])
#         for column in range(0, tableWidth+1):
#             if column == tableWidth:
#                 content += "|"
#                 lines += "-"
#             else:
#                 content += "|"+arrayWithBombs[row][column]
#                 lines += "--"
#         print(lines)
#         print(content)
#     print(lines)
#     content = ""
#     for column in range(0, tableWidth+1):
#         content += str(column)+"|"
#     print(content)


# def displayRevealedGrid(table):
#     tableHeight = len(table)
#     for row in range(0, tableHeight):
#         lines = " "
#         content = str(int(row)+1)
#         tableWidth = len(table[row])
#         for column in range(0, tableWidth+1):
#             if column == tableWidth:
#                 content += "|"
#                 lines += "-"
#             else:
#                 if row== int(hCoordinate)-1 and column== int(wCoordinate)-1:
#                     content+= "|"+table[row][column]
#                 else:
#                     content += "|"+"_"
#                     lines += "--"
#         print(lines)
#         print(content)
#     print(lines)
#     content = ""
#     for column in range(0, tableWidth+1):
#         content += str(column)+"|"
#     print(content)
