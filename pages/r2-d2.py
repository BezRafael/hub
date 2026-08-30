import streamlit as st


#######
# Campo de resposta
#######

# Campo de input do usuário
prompt = st.chat_input("Digite uma mensagem")
if prompt:
    st.write(f"Você enviou: {prompt}")