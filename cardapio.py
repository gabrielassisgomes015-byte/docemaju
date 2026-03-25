import streamlit as st
import urllib.parse

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Doce Maju - Cardápio", page_icon="🧁")

# CSS para centralizar as imagens e deixar o layout bonito
st.markdown("""
    <style>
    [data-testid="stImage"] {
        display: flex;
        justify-content: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🧁 Doce Maju")
st.write("---")

# LISTA DE DOCES (Edite os nomes e preços aqui)
# IMPORTANTE: O nome em 'imagem' deve ser IGUAL ao arquivo no seu GitHub
doces = [
    {
        "nome": "Bombom de Uva",
        "preco": "11,00",
        "imagem": "uva.png"
    },
    {
        "nome": "Bombom de Morango",
        "preco": "11,00",
        "imagem": "morango.png"
    },
    {
        "nome": "Bolo de Pote de Brigadeiro",
        "preco": "7,50",
        "imagem": "brigadeiro.png.jpeg"
    }
]

# EXIBIÇÃO EM COLUNAS
col1, col2 = st.columns(2)

for i, doce in enumerate(doces):
    target_col = col1 if i % 2 == 0 else col2
    
    with target_col:
        with st.container(border=True):
            # Link direto para a imagem no seu GitHub
            link_foto = f"https://raw.githubusercontent.com/gabrielassisgomes015-byte/docemaju/main/{doce['imagem']}"
            
            # Mostra a imagem com tamanho fixo de 250 pixels
            st.image(link_foto, width=250)
            
            st.subheader(doce['nome'])
            st.write(f"### R$ {doce['preco']}")
            
            # Botão de Pedido personalizado
            texto_pedido = f"Olá Maju! Quero o doce: {doce['nome']}"
            # Troque os NOVE ZEROS pelo número real da Maju (Ex: 21988887777)
            link_wa = f"https://wa.me/5521967690731?text={urllib.parse.quote(texto_pedido)}"
            
            st.link_button("Pedir no WhatsApp 💬", link_wa, use_container_width=True)

st.write("---")
st.caption("Doce Maju © 2024 - Feito com ❤️")
