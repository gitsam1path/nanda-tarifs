from nanda.tarifs import calcul_prix
def prix_nuit( distance ):
    majoration=1.2
    prix = calcul_prix(distance)*majoration
    return round(prix)
