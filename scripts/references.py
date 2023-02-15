# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 14:49:31 2023

@author: bchicot
"""
import datetime

year = datetime.date.today().year

annees = list(range(2001,year+1))

calcul = {
    "somme":["total","somm"],
    "moyenne":["moyen"],
    "compte":["decompt","compt"],
    "groupe":["group","par","regroup","fonction"]
    }

retour = {
    "texte" :["combien","quel","quantit"],
    "graphique":["evolu","graphiqu","histogramm","barr","represent"],
    "dataframe":["tableau","tabl","datafram","bas"]
    }

variable = {
    "marque" : ["marqu","firm","entrepris"],
    "modele_utac" : ["voitur","model","typ","vehicul"],
    "designation_commerciale":["nom","design","commercial"],
    "carburant":["carbur","energ"],
    "hybride": ["hybrid","elec"],
    "puissance_maximale":["cheval","puissanc","dynam"],
    "consommation_mixte_l_100km":["consomm","essenc"],
    "annee":["anne","temp","period","dat","inform","2009","2010","2011","2012","2013","2014","2015"],
    "co2_g_km":["co2","carbon","emmiss","pollut","pollu"],
    "gamme":["typ","gamm","form","categor"]
    }

liste_dict = {
    "calcul":calcul,
    "retour":retour,
    "variable":variable    
    }

type_graph = {
    "lines" : ["evolu","lign"],
    "histogram" : ["histogramm","barr","baton"],
    "boxplot" : ["boit","moustach"],
    "nuage" : ["nuag","point"]
    }

type_datast= {
    "vehicules-commercialises":["voitur", "vehicul" ,"essenc" ,"diesel" ,
                                "pollu" ,"hybrid" ,"berlin" ,"cabriolet" ,
                                "coup" ,"terrains" ,"break" ,"combispac" ,
                                "minispac" ,"monospace" ,"minibus" , "monospac" ,
                                "alfa-romeo" ,"aston", " martin" ,"audi" ,
                                "bmw" ,"chevrolet" ,"citroen" ,"daci" ,"ferrar" ,
                                "fiat" ,"ford" "hond" ,"hyund" ,"jeep" ,"ki" ,
                                "lamborghin" ,"lanci" ,"land rov" ,"lexus" ,
                                "lotus" ,"maserat" ,"mazd" ,"merced" ,"mercedes amg" ,
                                "mitsubish" ,"nissan" ,"opel" ,"peugeot" ,"dangel" ,
                                "porsch" ,"renault" ,"seat" ,"skod" ,"alfa" ,
                                "bentley" ,"infinit" ,"jaguar" ,"suzuk" ,"tesl" ,
                                "toyot" ,"volkswagen" ,"volvo" ,"chrysl" ,"mg" ,
                                "quattro" ,"rov" ,"saab" ,"smart" ,"subaru" ,
                                "carbod" ,"daewoo" ,"daihatsu" ,"lada" ,"morgan" ,
                                "rolls-royc" ,"isuzu" ,"iveco" ,"lti" ,"pgo" ,
                                "cadillac" ,"dodg" ,"lad" ,"dijeau" ,"lti " ,
                                "ssangyong" ,"maybach" ,"renault",
                                "chevaux","puissance","conso","carb","marque","marqu",
                                "model"]
    }

marques = ["ALFA-ROMEO" ,"ASTON" ,"AUDI" ,"BMW", "CHEVROLET" ,"CITROEN" ,"DACIA" ,
           "FERRARI" ,"FIAT" ,"FORD" ,"HONDA" ,"HYUNDAI" ,"JEEP" ,"KIA" ,"LAMBORGHINI" ,
           "LANCIA" ,"LAND ROVER" ,"LEXUS" ,"LOTUS" ,"MASERATI" ,"MAZDA" ,"MERCEDES" ,
           "MERCEDES AMG" ,"MINI" ,"MITSUBISHI" ,"NISSAN" ,"OPEL" ,"PEUGEOT" ,
           "DANGEL" ,"PORSCHE" ,"RENAULT" ,"SEAT" ,"SKODA" ,"ALFA ROMEO" ,"BENTLEY" ,
           "INFINITI" ,"JAGUAR LAND ROVER LIMITED" ,"SUZUKI" ,"TESLA" ,"TOYOTA" ,
           "VOLKSWAGEN" ,"VOLVO" ,"CHRYSLER" ,"MG" ,"QUATTRO" ,"ROVER" ,"SAAB" ,
           "SMART" ,"SUBARU" ,"CARBODIES" ,"DAEWOO" ,"DAIHATSU" ,"JAGUAR" ,"LADA-VAZ" ,
           "MORGAN" ,"ROLLS-ROYCE" ,"ISUZU" ,"IVECO" ,"LTI" ,"PGO" ,"CADILLAC" ,
           "DODGE" ,"LADA" ,"DIJEAU CARROSSIER" ,"LTI VEHICLES" ,"SSANGYONG" ,"MAYBACH" ,
           "MIA" ,"RENAULT TECH"
    ]



# test = ["voiture","véhicule","essence","diesel","polluant",
#         "hybride",'BERLINE', 'CABRIOLET', 'COUPE', 'TS TERRAINS/CHEMINS',
#         'BREAK', 'COMBISPACE', 'MINISPACE', 'MONOSPACE COMPACT', 'MINIBUS', 
#         'MONOSPACE','ALFA-ROMEO', 'ASTON MARTIN', 'AUDI', 'BMW', 'CHEVROLET',
#         'CITROEN', 'DACIA', 'FERRARI', 'FIAT', 'FORD', 'HONDA', 'HYUNDAI', 
#         'JEEP', 'KIA', 'LAMBORGHINI', 'LANCIA', 'LAND ROVER', 'LEXUS',
#         'LOTUS', 'MASERATI', 'MAZDA', 'MERCEDES', 'MERCEDES AMG',
#         'MINI', 'MITSUBISHI', 'NISSAN', 'OPEL', 'PEUGEOT', 'DANGEL', 'PORSCHE',
#         'RENAULT', 'SEAT', 'SKODA', 'ALFA ROMEO', 'BENTLEY', 'INFINITI',
#         'JAGUAR LAND ROVER LIMITED', 'SUZUKI', 'TESLA', 'TOYOTA', 'VOLKSWAGEN',
#         'VOLVO', 'CHRYSLER', 'MG', 'QUATTRO', 'ROVER', 'SAAB', 'SMART', 
#         'SUBARU', 'CARBODIES', 'DAEWOO', 'DAIHATSU', 'JAGUAR', 'LADA-VAZ',
#         'MORGAN', 'ROLLS-ROYCE', 'ISUZU', 'IVECO', 'LTI', 'PGO', 'CADILLAC',
#         'DODGE', 'LADA', 'DIJEAU CARROSSIER', 'LTI VEHICLES', 'SSANGYONG',
#         'MAYBACH', 'MIA', 'RENAULT TECH']

# for i in test:
#     j = i.lower()
#     print('"' + str(stemmer.stem(j))+'" ,')
    
    
