import streamlit as st
import urllib.parse

# 1. CONFIGURAÇÃO DA ABA (Onde ficava o cupcake)
# Substitua 'logo.png.jpeg' pelo nome da outra foto se for diferente
st.set_page_config(
    page_title="Doce Maju",
    page_icon="https://raw.githubusercontent.com/gabrielassisgomes015-byte/docemaju/main/logo.png.jpeg",
    layout="wide"
)

# Inicializando a memória do site (Carrinho, PIX e Estoque)
if 'carrinho' not in st.session_state:
    st.session_state.carrinho = {}
if 'pix' not in st.session_state:
    st.session_state.pix = "Chave não cadastrada"
if 'esgotados' not in st.session_state:
    st.session_state.esgotados = []

# CSS para deixar o visual limpo
st.markdown("""
    <style>
    [data-testid="stImage"] { display: flex; justify-content: center; }
    .stButton button { width: 100%; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 2. CABEÇALHO (LOGO E TÍTULO)
col_l, col_t = st.columns([1, 5])
with col_l:
    st.image("https://raw.githubusercontent.com/gabrielassisgomes015-byte/docemaju/main/logo.png.jpeg", width=120)
with col_t:
    st.title("Doce Maju")
    st.markdown("### O sabor que adoça sua vida 🧁")

st.write("---")

# 3. LISTA DE PRODUTOS
doces = [
    {"nome": "Bombom de Uva", "preco": 11.00, "imagem": "uva.png"},
    {"nome": "Bombom de Morango", "preco": 11.00, "imagem": "morango.png"},
    {"nome": "Bolo de Pote", "preco": 7.50, "imagem": "brigadeiro.png.jpeg"}
]

# 4. EXIBIÇÃO DOS PRODUTOS EM COLUNAS
cols = st.columns(4)
for i, doce in enumerate(doces):
    with cols[i % 4]:
        with st.container(border=True):
            link_foto = f"https://raw.githubusercontent.com/gabrielassisgomes015-byte/docemaju/main/{doce['imagem']}"
            st.image(link_foto, width=150)
            st.subheader(doce['nome'])
            
            if doce['nome'] in st.session_state.esgotados:
                st.error("🚫 ESGOTADO")
            else:
                st.write(f"**R$ {doce['preco']:.2f}**")
                if st.button(f"Adicionar +", key=f"add_{doce['nome']}"):
                    st.session_state.carrinho[doce['nome']] = st.session_state.c
