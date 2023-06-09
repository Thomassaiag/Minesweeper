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
                content += "|"+str(genericTable[row][column])
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

#fonction d'affichage de la case sélectionnée par les coordonnées
def revealTable(tableToReveal,hCoord,wCoord):
    global tableWithXGrid
    tableToReveal[int(hCoord)-1][int(wCoord)-1]=tableWithXGrid[int(hCoord)-1][int(wCoord)-1]
    return tableToReveal

#fonction d'affichage des indice chiffrés
def revealHintNumber(hCoord,wCoord):
    #initialisation du compteur de mine
    mineCounter=0
    #initialisation des coordonnées de début de recherche (coin supérieur gauche de la case sélectionnée)
    hCoordToStartLoop=int(hCoord)-1
    wCoordToStartLoop=int(wCoord)-1
    #parcours des 8 cases adjacentes à la case sélectionnée
    for hCoordCheck in range(hCoordToStartLoop,hCoordToStartLoop+3):
        print(f"hCoordCheck: {hCoordCheck}")
        for wCoordCheck in range(wCoordToStartLoop,wCoordToStartLoop+3):
            print(f"wCoordCheck: {wCoordCheck}")
            if(hCoordCheck!=0 and wCoordCheck!=0 and hCoordCheck!=gridHeight+1 and wCoordCheck!=gridWidth+1):
                print(f"contenu tableau bombe: {tableWithXGrid[hCoordCheck-1][wCoordCheck-1]}")
            if(hCoordCheck!=0 and wCoordCheck!=0 and hCoordCheck!=gridHeight+1 and wCoordCheck!=gridWidth+1 and tableWithXGrid[hCoordCheck-1][wCoordCheck-1]=="X"):
                mineCounter+=1
    return mineCounter



#fonction d'affichage de la case sélectionnée par les coordonnées
def revealTablewithNumber(tableToReveal,hCoord,wCoord):
    global tableWithXGrid
    if tableWithXGrid[int(hCoord)-1][int(wCoord)-1]=="X":
        tableToReveal[int(hCoord)-1][int(wCoord)-1]=tableWithXGrid[int(hCoord)-1][int(wCoord)-1]
        print("Vous avez perdu")
        global game
        game=False
    else:
        tableToReveal[int(hCoord)-1][int(wCoord)-1]=revealHintNumber(hCoord,wCoord)

    return tableToReveal


#initialisation de la taille de la grille et du nombre de bombes



gridHeight=int(input("Quelle hauteur de Grille souhaitez-vous ?"))
gridWidth=int(input("Quelle largeur de Grille souhaitez-vous ?"))
minesNumber = int(input("Combien de mines souhaitez-vous ?"))
hCoordinate=0
wCoordinate=0


emptyGridTable = createGridTable(gridHeight, gridWidth,"O")
fillGridTableWithX(emptyGridTable, minesNumber)
gridToGuess=displayGrid(tableWithXGrid)

#création de la grille neutre
neutralGridTable = createGridTable(gridHeight, gridWidth,"_")
neutralGrid=displayGrid(neutralGridTable)


gridSize=gridHeight*gridWidth
game=True
tourCount=0
#exécution du jeu
# i=1
while game:
    print(tableWithXGrid)
    hCoordinate = input(f"Choisissez la coordonnée Verticale (entre 1 et {gridHeight}) : ")
    wCoordinate = input(f"Choisissez la coordonnée horizontale (entre 1 et {gridWidth}) : ")
    table=revealTablewithNumber(neutralGridTable,hCoordinate,wCoordinate)
    displayGrid(table)
    tourCount+=1
    if tourCount==gridSize-minesNumber:
        print("Bravo, vous avez gagné !")
        game=False
    




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
