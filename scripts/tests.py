# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 16:15:56 2023

@author: bchicot
"""
# import os
# os.chdir("scripts")


from trait_dde import *
from actions import get_retour

txt0 = "nombre de modeles par annee filtrer sur mercedes et peugeot"
txt1 = "nombre de véhicules en 2014 pour alfa-romeo"
txt2 = "Donne moi un graphique en barre avec le nombre de chevaux moyen par type de voiture de la marque Peugeot en 2015"
txt3 = "J'ai besoin d'un tableau avec le nombre d'emmission de carbone moyen regroupé par marque"
txt4 = "Combien y-at-il de modèles différents en 2015"
txt5 = "voiture"

dem = demande(txt0)
get_retour(dem)

dem1 = demande(txt1)
get_retour(dem1)

dem2 = demande(txt2)
get_retour(dem2)

dem3 = demande(txt3)
get_retour(dem3)

dem4 = demande(txt4)
get_retour(dem4)

dem5 = demande(txt5)
get_retour(dem5)
