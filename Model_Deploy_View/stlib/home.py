def run():
    import streamlit as st
    st.markdown('<h1>Seja muito bem vindo ao TeleChurn Insights 👋</h1>', unsafe_allow_html=True)
    st.markdown( """

        Este é um projeto que utiliza Ciencia de Dados e Aprendizado de Máquina para prever se seus clientes de telefonia vão ou não abandonar o seu negócio. 


        ### Como funciona?

        - 👈 Selecione uma das opções no menu à esquerda
        - Insira os seus dados ou envie um arquivo no formato apropriado 
        - :loudspeaker: Antes de clicar no botão de Executar, verifique se todas as informações foram preenchidas ou enviadas corretamente

        ### Quer saber mais como o modelo foi treinado?

        - :computer: [Customer Churn Prediction](https://github.com/GabrielBueno21/Churn_Prediction)
    """)



if __name__ == "__main__":
    run()