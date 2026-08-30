import streamlit as st

#######
# Campo de resposta
#######

# campo de input do arquivo
with st.form("audio_form"):
    audio_file = st.file_uploader("Envie um arquivo de áudio", type=["wav", "mp3", "ogg", "..."])
    submitted = st.form_submit_button("Enviar")


# Mensagem de status 
if submitted and audio_file:
    st.audio(audio_file)
    st.success("Arquivo enviado com sucesso!")
    st.success("Aguarde o retorno do TARS")
elif submitted and not audio_file:
    st.warning("Por favor, selecione um arquivo de áudio antes de enviar.")
