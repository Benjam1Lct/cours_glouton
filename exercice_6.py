debut = [8,12,9,14,11]
fin = [13,17,11,16,12]

horaire = {'A':(8,13), 'B':(12,17), 'C':(9,11), 'D':(14,16), 'E':(11,12)}

def prochaine(debut, fin, h):
    min = None
    debut_stock = 0
    fin_stock = 0
    for i in range(len(debut)-1):
        if debut[i] >= h:
            if min is None:
                min = (fin[i] - debut[i])
                debut_stock = debut[i]
                fin_stock = fin[i]
            elif (fin[i] - debut[i]) < min:
                min = (fin[i] - debut[i])
                debut_stock = debut[i]
                fin_stock = fin[i]
    return str(debut_stock) + 'h-' + str(fin_stock) + 'h'


def selection(debut, fin):
    prochaine(debut, fin, )
    while

print(prochaine(debut, fin, 8))
