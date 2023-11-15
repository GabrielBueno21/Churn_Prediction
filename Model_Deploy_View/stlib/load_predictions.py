def predictions():
    import streamlit as st
    import pandas as pd
    import time
    with  st.spinner(text = 'Executando....'):
        time.sleep(2)
    st.success('Done!')


    
if __name__ == '__main__':
    predictions()