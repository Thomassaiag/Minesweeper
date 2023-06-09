import random

#initialisation de la variable globale tableWithXGrid
tableWithXGrid=[]

#affichage de n'importe quelle grille prenant en paramètre n'importe quel tableau
def displayGrid(genericTable):
    tableHeight = len(genericTable)
    for row in range(0, tableHeight):
        #initialisation des 1ères valeurs de colonne et de ligne (avec le numéro de ligne pour cette dernière)
        lines = " "
        content = str(row+1)
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
    #on vide le tableau de la bombe qu'on vient de placer
    while len(kArray) > 0:
        for i in range(0, gridHeight):
            gridWidth = len(tableToFill[i])
            for j in range(0, gridWidth):
                randInt = random.randint(1, gridHeight)
                if randInt == 1 and tableToFill[i][j] != "X" and len(kArray) != 0:
                    tableToFill[i][j] = "X"
                    kArray.pop()

    global tableWithXGrid
    tableWithXGrid=tableToFill
    return tableWithXGrid


#fonction d'affichage des indice chiffrés
def revealHintNumber(hCoord,wCoord):
    #initialisation du compteur de mine
    mineCounter=0
    #initialisation des coordonnées de début de recherche (coin supérieur gauche de la case sélectionnée)
    hCoordToStartLoop=hCoord-1
    wCoordToStartLoop=wCoord-1
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
    if tableWithXGrid[hCoord-1][wCoord-1]=="X":
        tableToReveal[hCoord-1][wCoord-1]=tableWithXGrid[hCoord-1][wCoord-1]
        print("Vous avez perdu")
        global game
        game=False
    else:
        tableToReveal[hCoord-1][wCoord-1]=revealHintNumber(hCoord,wCoord)

    return tableToReveal


#On vérifie si les coordonnées rentrées n'ont pas déjà été utilisées
def checkCoordAlreadyProvided(hcoord, wcoord):
    if (neutralGridTable[hcoord-1][wcoord-1])=="_":
        return True
    else:
        print("Vous avez déjà renseigné ces coordonnées")
        return False


#vérification de l'input de l'utilisateur en tant qu'entier
def checkUserInput(input):
    val=0
    try:
        val=int(input)
        return val
    except ValueError:
        print("Vous devez rentrer un entier")
        return "notAnInt"
    

#boucle répétant la demande de coordonnées tant qu'il ne s'agît pas d'un entier
def requestUserCoordinate(dimensionName, dimensionvalue):
    while True:
        coordinate = input(f"Choisissez la coordonnée {dimensionName} (entre 1 et {dimensionvalue}) : ")
        if checkUserInput(coordinate)!="notAnInt":
            break
    return int(coordinate)


#boucle répétant la demande de taille initiale de la grille tant qu'il ne s'agît pas d'un entier
def requestGridSetupDimensionsCoordinat(dimension):
    while True:
        size = input(f"Quelle {dimension} de Grille souhaitez-vous ?")
        if checkUserInput(size)!="notAnInt":
            break
    return int(size)


#________________________________________________________________________________________________________
#Initialisation du jeu

#initialisation de la taille de la grille et du nombre de bombes, en utilisant la validation d'entier
gridHeight=requestGridSetupDimensionsCoordinat("hauteur")
gridWidth=requestGridSetupDimensionsCoordinat("largeur")
while True:
    minesNumber = input("Combien de mines souhaitez-vous ?")
    if checkUserInput(minesNumber)!="notAnInt":
        break

hCoordinate=0
wCoordinate=0

emptyGridTable = createGridTable(gridHeight, gridWidth,"O")
fillGridTableWithX(emptyGridTable, int(minesNumber))
gridToGuess=displayGrid(tableWithXGrid)


#création de la grille neutre
neutralGridTable = createGridTable(gridHeight, gridWidth,"_")
neutralGrid=displayGrid(neutralGridTable)


gridSize=gridHeight*gridWidth
game=True
tourCount=0


#________________________________________________________________________________________________________
#Exécution du jeu

while game:
    print(tableWithXGrid)
    while True:
        hCoordinate=requestUserCoordinate("verticale", gridHeight)
        wCoordinate=requestUserCoordinate("horizontale", gridWidth)
        if checkCoordAlreadyProvided(hCoordinate,wCoordinate):
            break
    neutralGridTable=revealTablewithNumber(neutralGridTable,hCoordinate,wCoordinate)
    displayGrid(neutralGridTable)
    tourCount+=1
    if tourCount==gridSize-int(minesNumber):
        print("Bravo, vous avez gagné !")
        game=False