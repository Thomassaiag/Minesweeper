def createGrid(m,n):
    for _ in range (0,m):
        lines=""
        content=""
        for i in range(0,n):
            if i==n-1:
                content+="|"
                lines+="-"
            else:
                content+="|O"
                lines+="--"
        print(lines)
        print(content)
    

createGrid(4,5)