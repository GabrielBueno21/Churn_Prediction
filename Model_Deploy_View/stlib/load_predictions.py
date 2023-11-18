def predictions(data):
    import streamlit as st
    import numpy as np
    import pandas as pd
    import time
    import pickle

    @st.cache_data
    def import_model():
        return pickle.load(open('trained_model.pkl', 'rb'))

    with  st.spinner(text = 'Prevendo seus Clientes....'):
        time.sleep(2)
        model = import_model()
    
    std_columns = ['state', 'account_length', 'area_code', 'international_plan',
       'voice_mail_plan', 'number_vmail_messages', 'total_day_minutes',
       'total_day_calls', 'total_day_charge', 'total_eve_minutes',
       'total_eve_calls', 'total_eve_charge', 'total_night_minutes',
       'total_night_calls', 'total_night_charge', 'total_intl_minutes',
       'total_intl_calls', 'total_intl_charge',
       'number_customer_service_calls']
    

    if np.size(np.setxor1d(data.columns.to_list(), std_columns)) == 0:
        st.success('Tudo certo! Aqui estão suas previsões :smile:')
        df_results = pd.DataFrame(model.predict_proba(data), 
                           columns=['Proba_Abandono', 'Proba_Permanencia']).reset_index()

        df_results['ClienteID'] = df_results['index'].apply(lambda id: 'Cliente ' + str(id))
        df_results = df_results.drop(columns=['index'])

        df_results['Previsão de Churn'] = df_results['Proba_Abandono'].apply(lambda x: 'Abandono' if x > 0.5 else 'Permanencia')
        df_results = df_results.drop(columns = ['Proba_Abandono', 'Proba_Permanencia'])
        return st.dataframe(df_results, use_container_width  = True)
    else:
        return st.error(f'O arquivo que voce forneceu possui algumas colunas ausentes :sad:. Envie um novo ')
    


    
if __name__ == '__main__':
    predictions()