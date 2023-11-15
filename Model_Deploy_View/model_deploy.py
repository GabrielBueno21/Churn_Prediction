

import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
from stlib import home, one_customer

st.markdown(
    """
    <style>
        [data-testid=stSidebar] [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
)


with st.sidebar:
    st.image('static/churn-rate.png',  width=100)
    st.markdown("<h1 style='text-align: center; color: #E3371F'><b>TeleChurn Insights</b></h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'><i>Seu Parceiro na Retenção de Clientes</i></h5>", unsafe_allow_html=True)
    st.divider()

    menu_selected = option_menu(
        None, ['Início', 'Analisar Clientes'],
        icons = ['house', 'people-fill'],
         styles={
        "container": {"padding": "0!important", "background-color": "black"},
        "nav-link": {"font-size": "14px", "text-align": "left", "margin":"8px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "red","font-size": "12px"}
         }
    )

    st.divider()

    st.markdown("<h5 style='text-align: center; color: #E3371F'><b>Entre em Contato com o Autor</b></h5>", unsafe_allow_html=True)
  

    # Adiciona o link para o Streamlit
    st.markdown(f'<div style="width: 150px; margin: auto;"><a href="https://www.linkedin.com/in/gabriel-bueno-guimaraes/" target="_blank"><img src="./app/static/linkedin.png" alt="Click me" width="150px"></a></div>', unsafe_allow_html=True)

match menu_selected:
    case 'Início': home.run()
    case 'Analisar Clientes': one_customer.run()
