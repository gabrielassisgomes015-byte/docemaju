import streamlit as st
import urllib.parse

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Doce Maju - Cardápio", 
    page_icon="🧁", 
    layout="wide"
)

# Estilo para deixar os botões bonitos e centralizar as fotos
st.markdown("""
    <style>
    .stButton button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
    }
    [data-testid="stImage"] {
        display: flex;
        justify-content: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. CABEÇALHO (LOGO E TÍTULO)
col_logo1, col_logo2 = st.columns([1, 4])
with col_logo1:
    # Tenta puxar a logo do seu GitHub
    st.image("https://raw.githubusercontent.com/gabrielassisgomes015-byte/docemaju/main/logo.png.jpeg", width=80)
with col_logo2:
    st.title("🧁 Doce Maju - Cardápio")

st.write("---")

# 3. LISTA DE PRODUTOS
# Aqui você pode adicionar as características que sua irmã quiser
doces = [
    {
        "nome": "Bombom de Uva",
        "preco": "11,00",
        "imagem": "uva.png",
        "descricao": "Uva verde fresca e brigadeiro."
    },
    {
        "nome": "Bombom de Morango",
        "preco": "11,00",
        "imagem": "morango.png",
        "descricao": "Morango suculento com chocolate."
    },
    {
        "nome": "Bolo de Pote",
        "preco": "7,50",
        "imagem": "brigadeiro.png.jpeg",
        "descricao": "Brigadeiro gourmet cremoso."
    }
]

# 4. EXIBIÇÃO EM COLUNAS (Fotos menores e botões ativos)
# O número 4 faz com que caibam 4 doces por linha, deixando-os pequenos
cols = st.columns(4) 

for i, doce in enumerate(doces):
    with cols[i % 4]:
        with st.container(border=True):
            # Link da imagem no GitHub
            link_foto = f"https://raw.githubusercontent.com/gabrielassisgomes015-byte/docemaju/main/{doce['imagem']}"
            
            # Foto pequena (150px para caberem várias lado a lado)
            st.image(link_foto, width=150)
            
            st.subheader(doce['nome'])
            st.caption(doce['descricao'])
            st.write(f"**R$ {doce['preco']}**")
            
            # --- O BOTÃO DE PEDIDO (O seu 'carrinho') ---
            texto_pedido = f"Olá Maju! Quero o doce: {doce['nome']}"
            # Lembre de trocar o número abaixo pelo real da Maju
            link_wa = f"https://wa.me/5521999999999?text={urllib.parse.quote(texto_pedido)}"
            
            st.link_button("🛒 Pedir no WhatsApp", link_wa)

st.write("---")
st.caption("Doce Maju - Qualidade e Sabor")
