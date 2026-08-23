import streamlit as st
# tela inicial de apresentação



# abas na barra lateral esquerda
pages = {
    "Seções":[
        st.Page("pages/copiloto_tmo.py", title="TMO Copilot"),
        st.Page("pages/insercao_mobilizacao.py", title="Mobilização"),
        st.Page("pages/insercao_sobrevida.py", title="Sobrevida")
    ],
    "Problemas?":[
        st.Page("pages/abrir_chamado.py", title="Abrir Chamado")
    ]
}

pg = st.navigation(pages)
pg.run()