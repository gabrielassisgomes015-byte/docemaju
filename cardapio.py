import streamlit as st
import pandas as pd
import urllib.parse

# CONFIGURAÇÃO DA LOJA (O QUE O CLIENTE VÊ)
st.set_page_config(page_title="Doce Maju - Loja", page_icon="🧁", layout="wide")

# LINK DA SUA PLANILHA (Apontei direto para os seus dados)
URL_PLANILHA = "https://docs.google.com/spreadsheets/d/1700n8U96k3eDg_PeN8QM1IzzfCiftx6kheqqLcnD97c/export?format=csv"

# Escondendo menus desnecessários para o cliente
st.markdown("<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;}</style>", unsafe_allow_html=True)

st.title("🧁 Doce Maju")
st.write("### Escolha suas delícias e peça pelo WhatsApp!")

try:
    # Carregando os produtos da planilha
    df = pd.read_csv(URL_PLANILHA)
    
    col1, col2 = st.columns(2)
    
    # Rodando a lista de produtos
    for i, row in df.iterrows():
        # Só mostra se na coluna 'Disponível' estiver 'Sim'
        if str(row['Disponível']).strip().lower() == 'sim':
            target_col = col1 if i % 2 == 0 else col2
            with target_col:
                with st.container(border=True):
                    # Puxando a foto do seu GitHub
                    link_foto = f"https://raw.githubusercontent.com/gabrielassisgomes015-byte/docemaju/main/{row['Imagem']}"
                    st.image(link_foto, use_container_width=True)
                    st.subheader(row['Produto'])
                    st.write(f"R$ {row['Preço']:.2f}")
                    
                    # Botão para o cliente escolher
                    qtd = st.number_input("Quantidade", 0, 10, key=f"loja_{i}")
                    
                    if qtd > 0:
                        total_item = qtd * row['Preço']
                        msg = f"Olá Maju! Quero {qtd}x {row['Produto']} (Total: R$ {total_item:.2f})"
                        link_wa = f"https://wa.me/5521999999999?text={urllib.parse.quote(msg)}"
                        st.link_button(f"🛒 Pedir {qtd} via WhatsApp", link_wa)

except Exception as e:
    st.error("Carregando o cardápio... Se demorar, verifique o link da planilha!")
