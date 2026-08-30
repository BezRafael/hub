import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="TMO HUB",
    page_icon=":material/settings_suggest:",
    layout="centered"
)

# Define as páginas que aparecerão na barra lateral
pages = {

    # Grupo "Seções" da barra lateral
    "Seções": [
        # Tela inicial/apresentação
        st.Page("pages/inicio.py", icon=":material/home:", title="Home"),

        # Página principal do TMO Insights
        st.Page("pages/r2.py", icon=":material/smart_toy:", title="R2"),

        # Página principal do TMO Scribe
        st.Page("pages/tars.py", icon=":material/smart_toy:", title="TARS"),
    ],

    # Grupo "Problemas?" da barra lateral
    "Problemas?": [
        # Página para abertura de chamados
        st.Page("pages/abrir_chamado.py", title="Abrir Chamado")
    ]
}

# Cria o sistema de navegação usando as páginas definidas acima
pg = st.navigation(pages)

# Executa a página selecionada pelo usuário
pg.run()