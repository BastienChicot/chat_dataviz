# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 14:42:25 2023

@author: bchicot
"""

import requests
import json
import pandas as pd

def listing(liste_element,categorie):
    temp = []

    for elt in liste_element:
        temp.append("%27"+str(elt)+"%27")
    
    retour = categorie + "%2C".join(temp)
    
    return(retour)

def build_url(dde):
    
    base = "https://public.opendatasoft.com/api/v2/catalog/datasets/"
    
    liste_retour = []
    
    dataset = str(dde.type_dataset)+"/exports/json?limit=-1"
    # res = listing(dde.liste_var,"facet")
    # var = "".join(res)
    for key,item in dde.filtres.items():
        if len(dde.filtres[key]) > 1:
            retour = listing(dde.filtres[key], str("&where="+key+"%20in%20("))
            retour = retour + ")"
            liste_retour.append(retour)        
        else:
            retour = "&refine."+str(key)+"="+str(list(dde.filtres[key])[0])
            liste_retour.append(retour)
        # if str(key) not in dde.liste_var.values:
        #     var = var + ("&facet="+key)
    
    filtres = "".join(liste_retour)
    
    url = str(base+dataset+filtres)
    
    return(url)

def call_api(url):

    response = requests.get(url)
    
    if response.status_code == 200 :
            
        df = pd.json_normalize(response.json())
        df.drop_duplicates()
        
    else :
        
        df = pd.DataFrame()
    
    return(df)

