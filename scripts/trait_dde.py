# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 14:41:05 2023

@author: bchicot
"""
# import os
# os.chdir("scripts")
import pandas as pd
from pandas.api.types import is_numeric_dtype

import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import FrenchStemmer
import unidecode
import spacy

from references import *
from requete import build_url, call_api
nlp = spacy.load('fr_core_news_md')

stemmer = FrenchStemmer()

class mot():
    def __init__(self, mot):
        self.mot = mot
        self.liste_affect = []
        self.liste_tag = []

class demande():
    def __init__(self,texte):
        self.dde = texte
        
        self.filtres = {}
        
        self.type_graph = []
        
        self.retour = ""

        self.data = pd.DataFrame()
        
        self.type_dataset = ""
        
        self.url = ""
        
        if type(self.dde) == str:
            self.txt = self.dde.replace("'", " ")
            self.txt = re.sub(r'[^\w\s]','',self.txt)
            self.txt = self.txt.lower()
            
        
            punct = string.punctuation
            for c in punct:
                self.elt_ss = self.txt.replace(c, "")
            self.elt_ss = unidecode.unidecode(self.elt_ss)
                
            self.tokens = nltk.word_tokenize(self.elt_ss)
            # self.tokens = [word for word in self.tokens if word not in stopwords.words('french')]
##FILTERS
            for elt in self.tokens:
                if elt.upper() in marques:
                    i=elt.upper()
                    if "marque" not in self.filtres:
                        self.filtres.update({"marque":[str(i)]})
                    else :
                        self.filtres["marque"].append(str(i))
                if elt in str(annees):
                    if "annee" not in self.filtres:
                        self.filtres.update({"annee":[str(elt)]})
                    else:
                        self.filtres["annee"].append(str(elt))
                else:
                    pass

##STEMATISATION                                
            for elt in range(0,len(self.tokens)):
                self.tokens[elt] = stemmer.stem(self.tokens[elt])

##TYPE DATASET
            for elt in self.tokens :
                for key in type_datast:
                    if elt in type_datast[str(key)]:
                        self.type_dataset = str(key)
              
##TYPE GRAPH
            for elt in self.tokens :
                for key in type_graph:
                    if elt in type_graph[str(key)]:
                        self.type_graph.append(str(key))

            self.voisins = list(nltk.bigrams(self.tokens))
            
            self.liste_mot = self.tokens.copy()
            
            for elt in range(0,len(self.liste_mot)):
                self.liste_mot[elt] = mot(self.liste_mot[elt])
                
            for elt in self.liste_mot:
                for k,i in liste_dict.items():
                    for cle in i.keys():
                        if elt.mot in i[cle]:
                            elt.liste_affect.append(cle)
                            elt.liste_tag.append(k)                    

###RECUPERATION D INFO                            
            self.process()
            

        else:
            return("Je n'ai pas compris votre question")

    def interpretation(self):

        df_temp = pd.DataFrame(columns = ["affect","tag","n"])
        for elt in self.liste_mot :
            if len(elt.liste_affect) > 0:
                new_row = {'affect':elt.liste_affect[0], 'tag':elt.liste_tag[0], 'n':1}
                df_temp = df_temp.append(new_row, ignore_index=True)
            
            else:
                new_row = {'affect':"empty", 'tag':"empty", 'n':1}
                df_temp = df_temp.append(new_row, ignore_index=True)
        
        self.df_inter = df_temp.groupby(["affect","tag"]).sum().reset_index()
        
            
    def det_var(self):
        self.liste_var = "modele_utac"        
        if any(self.df_inter["tag"] == "variable"):
            variables = self.df_inter.loc[self.df_inter["tag"] == "variable"]
            if len(variables["tag"].unique()) == 1:
                self.liste_var = variables["affect"]
            elif len(variables["tag"].unique()) == 2:
                self.liste_var = [variables["affect"][0],variables["affect"][1]]
            elif len(variables["tag"].unique()) > 2:
                temp = variables.sort_values(by = "n", ascending = False)
                self.liste_var = [variables["affect"][0],variables["affect"][1]]
            else:
                pass

    
    def det_calcul(self):            
        self.type_calcul = "compte"
        if any(self.df_inter["tag"] == "calcul"):
            test2 = self.df_inter.loc[self.df_inter["tag"] == "calcul"]
            if len(test2["tag"].unique()) == 1:
                self.type_calcul = test2["affect"].unique()
    
            else:
                temp = test2.sort_values(by = "n", ascending = False)
                self.type_calcul = [test2["affect"][0],test2["affect"][1]]
    
        else:
            if len(self.liste_var ) == 1:
                i = self.liste_var.index.values[0]
                if is_numeric_dtype(self.data[self.liste_var]) :
                    self.type_calcul = "somme"
    
                else:
                    self.type_calcul = "compte"
    
            elif len(self.liste_var ) == 2:
                i = self.liste_var.index.values[0]
                j = self.liste_var.index.values[1]
                if is_numeric_dtype(self.data[self.liste_var[i]]) and \
                is_numeric_dtype(self.data[self.liste_var[j]]):
                    self.type_calcul = "somme"
            
            else:
                self.type_calcul = "compte"
    
    def det_represent(self):
        self.type_representation = "dataframe"
    
        if any (self.df_inter["tag"] == "retour"):
            test = self.df_inter.loc[self.df_inter["tag"]=='retour'].reset_index()
            if len(test["tag"].unique()) == 1:
                self.type_representation = test._get_value(min(test.index), "affect")
    
            else:
                temp = test.sort_values(by = "n", ascending = False).reset_index()
                self.type_representation = test._get_value(min(test.index), "affect")
    
        else:
            if "annee" in self.liste_var:
                self.type_representation = "graphique"
            
            elif len(self.liste_var) == 2 and "groupe" not in self.type_calcul :
                self.type_representation = "graphique"
    
            elif len(self.liste_var) == 2 and "groupe" in self.type_calcul :
                self.type_representation = "dataframe"
    
            elif len(self.liste_var) > 2 :
                self.type_representation = "graphique"
            
            else:
                pass

    def get_table(self) :
###CONSTRUCTION DE LA TABLE
        self.url = build_url(self)
        
        self.data = call_api(self.url)
        
        if len(self.data.columns) == 0:
            print("Pas de données")
                
    def process(self):
        self.interpretation()
        self.det_var()
        self.get_table()

        if not self.data.empty:
            self.det_calcul()
            self.det_represent()
            
        else :
            print("Pas de données disponibles pour cette demande : " + self.dde)
            

        

# txt0 = "annee et marque mercedes"
# txt1 = "Je veux le nombre de véhicule par marque en 2022"
# txt2 = "Donne moi un graphique en barre avec le nombre de chevaux moyen par type de voiture de la marque Peugeot en 2015"
# txt3 = "J'ai besoin d'un tableau avec le nombre d'emmission de carbone regroupées par marque"
# txt4 = "Combien y-at-il de modèles différents en 2021"

# lst_txt = [txt0,txt1,txt2,txt3,txt4]

# for t in lst_txt:
    
#     dde_1 = demande(t)
#     print(dde_1.tokens)
#     va = pd.Series(dde_1.liste_var)
#     ca = pd.Series(dde_1.type_calcul)
#     rp = pd.Series(dde_1.type_representation)
    
#     print("va : " + va.values,"ca : " + ca.values,"rp : " + rp.values)
#     print("filtres : ")
#     for key,item in dde_1.filtres.items():
#         print(key, " : ", dde_1.filtres[key])
