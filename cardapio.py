import streamlit as st
import urllib.parse

# 1. CONFIGURAÇÃO DA PÁGINA (Aqui você muda o ícone da aba do navegador)
# No 'page_icon', você pode colocar um link de uma foto ou um emoji
st.set_page_config(
    page_title="Doce Maju - Cardápio", 
    page_icon="🧁", 
    layout="wide" # Isso faz o site usar a tela toda, espalhando mais os itens
)

# CSS para ajustar o visual e diminuir espaços
st.markdown("""
    <style>
    .stButton button {
        width: 100%;
        border-radius: 20px;
    }
    [data-testid="stImage"] {
        display: flex;
        justify-content: center;
    }
    /* Estilo para as características */
    .descricao {
        font-size: 14px;
        color: #666;
        text-align: center;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. CABEÇALHO COM LOGO (Opcional)
# Se tiver um link de logo, substitua o link abaixo. 
# Se não tiver, ele vai mostrar apenas o texto.
col_logo1, col_logo2 = st.columns([1, 4])
with col_logo1:
    # Substitua esse link pela URL da sua logo no GitHub se quiser
    st.image("https://raw.githubusercontent.com/gabrielassisgomes015-byte/docemaju/main/logo.png.jpeg", width=100)
with col_logo2:
    st.title("Doce Maju - Cardápio")

st.write("---")

# 3. LISTA DE DOCES (Com campo para Características)
doces = [
    {
        "nome": "Bombom de Uva",
        "preco": "11,00",
        "imagem": "uva.png",
        "descricao": "Uva fresca coberta com brigadeiro branco e chocolate."
    },
    {
        "nome": "Bombom de Morango",
        "preco": "11,00",
        "imagem": "morango.png",
        "descricao": "Morango selecionado com camada generosa de chocolate."
    },
    {
        "nome": "Bolo de Pote",
        "preco": "7,50",
        "imagem": "brigadeiro.png.jpeg",
        "descricao": "Massa fofinha com recheio cremoso de brigadeiro gourmet."
    }
]

# 4. EXIBIÇÃO EM COLUNAS (Lado a lado e menores)
# Criamos várias colunas para os doces não ficarem gigantes
cols = st.columns(3) # Aumentei para 3 colunas para ficarem menores ainda

for i, doce in enumerate(doces):
    # Distribui os doces entre as 3 colunas
    with cols[i % 3]:
        with st.container(border=True):
            link_foto = f"https://raw.githubusercontent.com/gabrielassisgomes015-byte/docemaju/main/{doce['imagem']}"
            
            # IMAGEM PEQUENA (180px)
            st.image(link_foto, width=180)
            
            st.subheader(doce['nome'])
            
            # CARACTERÍSTICAS (O que você pediu para adicionar depois)
            st.markdown(f"<p class='descricao'>{doce['descricao']}</p>", unsafe_allow_html=True)
            
            st.write(f"**R$ {doce['preco']}**")
            
            # Botão de Pedido
            texto_pedido = f"Olá Maju! Quero o doce: {doce['nome']}"
            link_wa = f"https://wa.me/5521999999999?text={urllib.parse.quote(texto_pedido)}"
            st.link_button("Pedir", link_wa)

st.write("---")
st.caption("Doce Maju - Qualidade e Sabor")
