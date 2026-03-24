import streamlit as st
import urllib.parse

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Doce Maju", page_icon="🧁", layout="wide")

# LINK DIRETO PARA AS FOTOS NO SEU GITHUB
# (Ajustado para a pasta principal onde as fotos estão)
LINK_FOTOS = "https://raw.githubusercontent.com/gabrielassisgomes015-byte/docemaju/main/"

# 2. ESTOQUE (Organizado com os nomes das fotos que você subiu)
if 'estoque' not in st.session_state:
    st.session_state.estoque = {
        "Bombom Uva com ninho": {
            "preco": 11.0, 
            "desc": "Uvas frescas e creme Ninho", 
            "disponivel": True, 
            "imagem": "g.jpeg" # Nome exato no seu GitHub
        },
        "Bombom Morango com ninho": {
            "preco": 11.0, 
            "desc": "Morango e o verdadeiro Ninho", 
            "disponivel": True, 
            "imagem": "p.jpeg" # Nome exato no seu GitHub
        },
        "Bolo de Pote brigadeiro": {
            "preco": 8.0, 
            "desc": "Chocolate com morango", 
            "disponivel": True, 
            "imagem": "rango.png.jpeg" # Nome exato no seu GitHub
        }
    }

# 3. MENU LATERAL (Navegação)
st.sidebar.title("Menu Doce Maju")
aba = st.sidebar.radio("Escolha a página:", ["🛒 Loja", "⚙️ Administração"])

# ---------------- PÁGINA DA LOJA (CLIENTE) ----------------
if aba == "🛒 Loja":
    st.markdown("<h1 style='text-align: center; color: #d4a5b9;'>Doce Maju</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'><b>🧁 FEITO COM AMOR 🧁</b></p>", unsafe_allow_html=True)
    st.divider()

    col_menu, col_linha, col_carrinho = st.columns([1.5, 0.1, 1])

    with col_menu:
        st.subheader("🌸 Nosso Cardápio")
        itens_escolhidos = {}
        
        c1, c2 = st.columns(2)
        for i, (nome, info) in enumerate(st.session_state.estoque.items()):
            if info["disponivel"]:
                lado = c1 if i % 2 == 0 else c2
                with lado:
                    with st.container(border=True):
                        # Tenta carregar a imagem. Se o link estiver errado, ele mostra um aviso.
                        try:
                            st.image(LINK_FOTOS + info["imagem"], use_container_width=True)
