import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="TMO HUB",
    page_icon=":material/hub:",
    layout="wide"
)

# Define as páginas que aparecerão na barra lateral
pages = {

    # Grupo "Seções" da barra lateral
    "Seções": [
        # Tela inicial/apresentação
        st.Page("pages/inicio.py", icon=":material/home:", title="Home"),

        # Página principal do TMO Insights
        st.Page("pages/tmo_insights.py", icon=":material/auto_awesome:", title="TMO Insights"),

        # Página principal do TMO Scribe
        st.Page("pages/tmo_scribe.py", icon=":material/record_voice_over:", title="TMO Scribe"),

        # Página para inserção de dados de mobilização
        st.Page("pages/coleta.py", icon=":material/medical_services:", title="Mobilização/Coleta"),

        # Página para inserção de dados de sobrevida
        st.Page("pages/transplantes.py", icon=":material/health_and_safety:", title="Sobrevida/Transplantes")
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