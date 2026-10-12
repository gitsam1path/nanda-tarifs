"""Calcul des tarifs de trajets Nanda."""

PRIX_KM = 50
FRAIS_SERVICE = 200


def calcul_prix(distance, prix_km=PRIX_KM, frais=FRAIS_SERVICE):
    """Prix d'un trajet en FCFA."""
    if distance <= 0:
        raise ValueError("La distance doit être positive")
    return distance * prix_km + frais


def prix_par_passager(distance, passagers):
    """Prix partagé entre plusieurs passagers, arrondi à l'unité."""
    if passagers < 1:
        raise ValueError("Il faut au moins un passager")
    return round(calcul_prix(distance) / passagers)
