# voyageur glouton

def plus_proche(ville, dist, visitees):
    """Renvoie le numéro de la ville non encore visitée la
       plus proche de la ville courante, en supposant qu'il
       en existe au moins une.
    """
    pp = None
    for i in range(len(visitees)):
        if visitees[i]: continue
        if pp == None or dist[ville][i] < dist[ville][pp]:
            pp = i
    return pp

def voyageur(villes, dist, depart):
    """Affiche les étapes du parcours glouton depuis la
       ville de départ.
    """
    n = len(villes)
    visitees = [False] * n
    courante = depart
    for _ in range(n-1):
        visitees[courante] = True
        suivante = plus_proche(courante, dist, visitees)
        print("on va de", villes[courante], \
              "à", villes[suivante], \
              "en", dist[courante][suivante], "km")
        courante = suivante
    print("on revient de", villes[courante], \
          "à", villes[depart], \
          "en", dist[courante][depart], "km")


villes = [0,1,2,3,4]
dist =[[0,55,303,188,183],[55,0,306,176,203],[303,306,0,142,153],[188,176,142,0,123],[183,203,153,123,0]]
print(voyageur(villes, dist, 0))