import pytest

from nanda.tarifs import calcul_prix, prix_par_passager


def test_prix_standard():
    assert calcul_prix(10) == 700


def test_distance_invalide():
    with pytest.raises(ValueError):
        calcul_prix(0)


def test_prix_partage():
    assert prix_par_passager(10, 2) == 350


def test_passagers_invalides():
    with pytest.raises(ValueError):
        prix_par_passager(10, 0)
