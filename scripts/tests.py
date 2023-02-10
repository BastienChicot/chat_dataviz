# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 16:15:56 2023

@author: bchicot
"""
# import os
# os.chdir("scripts")


from trait_dde import *
from actions import get_retour

txt0 = "nombre de modeles par annee filtrer sur mercedes"
txt1 = "Je veux le nombre de véhicule par marque en 2014"
txt2 = "Donne moi un graphique en barre avec le nombre de chevaux moyen par type de voiture de la marque Peugeot en 2015"
txt3 = "J'ai besoin d'un tableau avec le nombre d'emmission de carbone regroupées par marque"
txt4 = "Combien y-at-il de modèles différents en 2015"

dem = demande(txt0)
a = get_retour(dem)

type(a) == pd.DataFrame

dem1 = demande(txt1)
get_retour(dem1)

type(b)

dem2 = demande(txt2)
c =get_retour(dem2)

type(c)

dem3 = demande(txt3)
get_retour(dem3)

dem4 = demande(txt4)
d = get_retour(dem4)

type(d)