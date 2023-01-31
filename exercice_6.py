debut = [8,12,9,14,11]
fin = [13,17,11,16,12]

horaire = {'A':(8,13), 'B':(12,17), 'C':(9,11), 'D':(14,16), 'E':(11,12)}

def prochaine(debut, fin, h):
    opti = None
    for i in range(len(debut)):
        if debut[i] >= h:
            if opti == None:
                opti = [debut[i],fin[i]]
            elif opti[1] - opti[0] > fin[i] - debut[i] and fin[i] < opti[1]:
                opti = [debut[i],fin[i]]
        else:
            pass

    return opti


def selection(debut, fin):

    h = 8

    max_debut = 0
    lst_act = []

    for i in range(len(debut)-1):
        if debut[i] > max_debut:
            max_debut = debut[i]

    while h < max_debut:
        lst_act.append(prochaine(debut,fin,h))
        h = prochaine(debut,fin,h)[1]
 
    return lst_act

print(prochaine(debut, fin, 8))
