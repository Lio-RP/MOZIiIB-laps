def transposition(tabl):
    a = []
    for i in range(4):
        s = ''
        for b in reversed(tabl):
            s += b[ i]
        a.append(s)
    return a

def recall_password(tabl, cod):
    txt = ''
    for k in range(4):
        for i in range(4):
            for j in range(4):
                if tabl[ i][j] == "X":
                    txt = txt + cod[ i][j]
        tabl=transposition(tabl)
    return txt

print ( recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')))