# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 10:43:48 2023

@author: bchicot
"""
import streamlit as st
import pandas as pd
import numpy as np

from scripts.trait_dde import *
from scripts.actions import get_retour

data = pd.read_csv("data/data_voit.csv", sep=";", encoding = "ISO-8859-1")

st.title("Chat dataviz")

dem = st.text_area('Entrez votre demande ci-dessous : ')

if st.button('Envoyer la demande'):
    dde = demande(dem, data)
    retour = get_retour(dde)
    if isinstance(retour, str) or isinstance(retour, int) :
        st.text(retour)
    elif type(retour) == "DataFrame":
        st.table(retour)
    else :
        st.pyplot(retour.figure)

