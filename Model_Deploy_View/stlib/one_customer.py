def run():
    import streamlit as st
    from stlib import load_predictions
    import pandas as pd
    st.markdown("""
                # Prevendo seus Clientes 📊
                """)
    st.markdown(""" ### Guia Rápido 📚""")
    st.markdown("""
        - Insira um arquivo em formato <i>csv</i>.
        - Em seguida, verifique se os dados estão corretos através da nossa ferramenta de visualização rápida.
        - Clique no botão de <b>'Executar'</b>, para poder obter nossas previsões.
        - Em caso de dúvidas sobre o formato e quais colunas são esperadas pela ferramenta, clique na opção para baixar um arquivo de amostra.
        - <b> Esperamos que você goste da nossa ferramenta :smile: </b>
        """, unsafe_allow_html=True)
    
    upload_data = st.file_uploader(label = 'Insira um arquivo contendo os dados dos seus clientes: ',
                                   type = ['csv'])

    if upload_data is not None:
        data = pd.read_csv(upload_data, index_col=[0])
        preview_data = data.head(5).copy()
        st.markdown('<i>Preview dos Dados Inseridos:</i>', unsafe_allow_html = True)
        st.dataframe(preview_data)
        st.button('Executar', type = 'primary', on_click = load_predictions.predictions())
    else:
        
        st.markdown("""<div data-testid="stMarkdownContainer" class="st-emotion-cache-q8sbsg e1nzilvr5">
                    <p>Ver estrutura dos dados e/ou baixar amostra:</p></div> <p></p>""", unsafe_allow_html = True)
        with open('sample_data.csv', 'r') as sample_data:

            st.download_button(label = 'Baixar arquivo de amostra',
                            data = sample_data,
                            file_name = 'sample_data.csv',
                            type = 'primary')


if __name__ == '__main__':
    run()