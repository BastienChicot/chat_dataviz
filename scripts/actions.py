# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 14:41:54 2023

@author: bchicot
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def get_retour (dde):
        
    def filtrer_table(objt) :
        
        for key,item in objt.filtres.items():
            objt.data = objt.data.loc[objt.data[key].astype(str) == str(objt.filtres[key])]
        
        return(objt.data)

    for i in list(dde.filtres):
        dde.data = filtrer_table(dde)
        
    for elt in dde.liste_var:
        if elt in list(dde.filtres):
            dde.liste_var = dde.liste_var[dde.liste_var != elt]

    def groupe_data (objt):
        if ("somme" in objt.type_calcul) :
            objt.data = objt.data.groupby(list(objt.liste_var)[0]).sum().reset_index()
        elif ("moyenne" in objt.type_calcul) :
            objt.data = objt.data.groupby(list(objt.liste_var)[0]).mean().reset_index()
        elif ("compte" in objt.type_calcul) :
            objt.data = objt.data.groupby(list(objt.liste_var)[0]).nunique().reset_index()
        else:
            if len(list(objt.liste_var)) > 1:
                if objt.data[list(objt.liste_var)[1]].dtypes == "O" or \
                    objt.data[list(objt.liste_var)[1]].dtypes == "str" :
                        objt.data = objt.data.groupby(list(objt.liste_var)[0]).nunique().reset_index()
                else : 
                    objt.data = objt.data.groupby(list(objt.liste_var)[0]).sum().reset_index()
            else :
                if objt.data[list(objt.liste_var)[0]].dtypes == "O" or \
                    objt.data[list(objt.liste_var)[0]].dtypes == "str" :
                        objt.data = objt.data.groupby(list(objt.liste_var)[0]).nunique().reset_index()
                else : 
                    objt.data = objt.data.groupby(list(objt.liste_var)[0]).sum().reset_index()
                   
        return(objt.data)
                
            
    if ("groupe" in dde.type_calcul) :
        dde.type_calcul = dde.type_calcul[dde.type_calcul != "groupe"]  
        if len(dde.type_calcul) != 0 :
            dde.type_calcul = np.array(list(dde.type_calcul)[0])
        
        dde.data = groupe_data(dde)
        
    dde.data = dde.data[list(dde.liste_var)]
        
    representation = str(dde.type_representation)
    
    if representation == "graphique" :
        if len(dde.type_graph) > 0:
            grph = dde.type_graph[0]

            if len(dde.liste_var) > 1:
                
                if grph == "lines" and ("annee" in  dde.data.columns):
                    
                    ix = list(dde.liste_var[dde.liste_var != "annee"])[0]
                    
                    dde.retour = sns.lineplot(data=dde.data, x=dde.data["annee"], y=dde.data[ix])

                elif grph == "lines" and ("annee" not in  dde.data.columns):
                    
                    ix = list(dde.liste_var)[1]
                    igrec = list(dde.liste_var)[0]
                    
                    dde.retour = sns.lineplot(data=dde.data, x=dde.data[igrec], y=dde.data[ix])
                
                elif grph == "histogram" :

                    ix = list(dde.liste_var)[1]
                    igrec = list(dde.liste_var)[0]
                    
                    dde.retour = sns.barplot(data=dde.data, x=dde.data[igrec], y=dde.data[ix])

                elif grph == "nuage" :

                    ix = list(dde.liste_var)[1]
                    igrec = list(dde.liste_var)[0]
                    
                    dde.retour = sns.scatterplot(data=dde.data, x=dde.data[igrec], y=dde.data[ix])
            
            elif len(dde.liste_var) == 1:
                    
                if grph == "lines" and ("annee" in  dde.data.columns):
                    
                    dde.retour = sns.kdeplot(data=dde.data, x=dde.data["annee"])

                elif grph == "lines" and ("annee" not in  dde.data.columns):
                    
                    igrec = list(dde.liste_var)[0]
                    
                    dde.retour = sns.kdeplot(data=dde.data, x=dde.data[igrec])
                
                elif grph == "histogram" :

                    igrec = list(dde.liste_var)[0]
                    
                    dde.retour = sns.histplot(data=dde.data, x=dde.data[igrec])

                elif grph == "nuage" :

                    igrec = list(dde.liste_var)[0]
                    
                    dde.retour = sns.scatterplot(data=dde.data, x=dde.data[igrec])
                    
            else:
                
                dde.retour = str("Pas de résultat possible pour ce type de graphique" +
                                 "variable : " + list(dde.liste_var) + "\n" +
                                 "calcul : " + dde.type_calcul + "\n" )
                                 
        else:
            if len(dde.liste_var) > 1:

                if all(dde.data.dtypes) == "O" or\
                    all(dde.data.dtypes) == "str" :
                        
                        ix = list(dde.liste_var)[1]
                        igrec = list(dde.liste_var)[0]
                        
                        dde.retour = sns.scatterplot(data=dde.data, x=dde.data[igrec], y=dde.data[ix])
                
                if any(dde.data.dtypes) == "int64"or\
                    any(dde.data.dtypes) == "float" and \
                        ("annee" not in dde.data.columns):
                        
                        for i in dde.liste_var :
                            if dde.data[list(i)[0]].dtypes == "int64" :
                                ix = list(i)[0]
                                igrec = list(i)[1]
                            elif dde.data[list(i)[0]].dtypes == "float" :
                                ix = list(i)[0]
                                igrec = list(i)[1]
                            elif dde.data[list(i)[1]].dtypes == "int64" :
                                ix = list(i)[1]
                                igrec = list(i)[0]
                            elif dde.data[list(i)[1]].dtypes == "float" :
                                ix = list(i)[1]
                                igrec = list(i)[0]
                                                
                        dde.retour = sns.scatterplot(data=dde.data, x=dde.data[igrec], y=dde.data[ix])
            
                elif any(dde.data.dtypes) == "int64"or\
                    any(dde.data.dtypes) == "float" and \
                        ("annee" in dde.data.columns):
                    
                    ix = list(dde.liste_var[dde.liste_var != "annee"])[0]
                    
                    dde.retour = sns.lineplot(data=dde.data, x=dde.data["annee"], y=dde.data[ix])

                elif all(dde.data.dtypes) == "int64"or\
                    all(dde.data.dtypes) == "float" and \
                        ("annee" in dde.data.columns):
                    
                    ix = list(dde.liste_var[dde.liste_var != "annee"])[0]
                    
                    dde.retour = sns.lineplot(data=dde.data, x=dde.data["annee"], y=dde.data[ix])
                
                elif any(dde.data.dtypes) == "int64"or\
                    any(dde.data.dtypes) == "float" and \
                        ("annee" not in dde.data.columns):
                    
                    ix = list(dde.liste_var)[1]
                    igrec = list(dde.liste_var)[0]
                    
                    dde.retour = sns.lineplot(data=dde.data, x=dde.data["annee"], y=dde.data[ix])
                    
            else :

                dde.retour = str("Pas de résultat possible pour ce type de graphique" +
                 "variable : " + dde.liste_var + "\n" +
                 "calcul : " + dde.type_calcul + "\n" )

    elif representation == "dataframe" :
        dde.retour = dde.data
    
    elif representation == "texte" :

        if len(dde.data) == 1:
            dde.retour = dde.data
        elif len(dde.data) > 1 :
            if len(dde.data.columns) > 1:
                if all(dde.data.dtypes) == "int64"or\
                        all(dde.data.dtypes) == "float" :
                            dde.retour = dde.data.describe
                            
                elif all(dde.data.dtypes) == "O" or\
                        all(dde.data.dtypes) == "str" :
                            
                            ix = list(dde.liste_var)[1]
                            igrec = list(dde.liste_var)[0]
    
                            dde.retour = dde.data.groupby([ix , igrec]).nunique()
            elif len(dde.data.columns) == 1 :
                
                k = dde.data.columns[0]
                
                if dde.data[k].dtypes == "int64"or\
                        dde.data[k].dtypes == "float" :
                            dde.retour = dde.data.describe
                            
                elif dde.data[k].dtypes == "O" or\
                        dde.data[k].dtypes == "str" :
                                
                            dde.retour = len(dde.data[k].unique())
                
            else :
                dde.retour = dde.data
    
    else :
        
        dde.retour = str("Pas de résultats possibles pour la demande : " +

                         str(dde.dde))
        
    return(dde.retour)    
        