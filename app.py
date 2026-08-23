import streamlit as st

# ============================================================
# TELA INICIAL
# ============================================================
# Configuração da página
st.set_page_config(
    page_title="TMO HUB",
    page_icon="🧩",
    layout="wide"
)


# Define as páginas que aparecerão na barra lateral
pages = {

    # Grupo "Seções" da barra lateral
    "Seções": [
        # Tela inicial/apresentação
        st.Page("pages/inicio.py", title="Home", icon="🏠"),

        # Página principal do copiloto TMO
        st.Page("pages/copiloto_tmo.py", icon="🤖", title="TMO Copilot"),

        # Página para inserção de dados de mobilização
        st.Page("pages/insercao_mobilizacao.py", icon="📋", title="Mobilização"),

        # Página para inserção de dados de sobrevida
        st.Page("pages/insercao_sobrevida.py", icon="📊", title="Sobrevida")
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