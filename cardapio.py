import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Doce Maju - Loja", page_icon="🧁", layout="wide")

# --- CONEXÃO COM A PLANILHA (O CÉREBRO DA LOJA) ---
# Coloque aqui o link que você pegou na barra de endereços da planilha
URL_PLANILHA = "https://docs.google.com/spreadsheets/d/17OOn8U96k3eDg_PeN0QMlIzzfCiftx6kheqqLcnD97c/edit?gid=0#gid=0"

def carregar_estoque():
    try:
        # Converte o link da planilha para formato de leitura automática (CSV)
        url_csv = URL_PLANILHA.replace('/edit?usp=sharing', '/export?format=csv').replace('/edit', '/export?format=csv')
        df = pd.read_csv(url_csv)
        return df
    except:
        st.error("Erro ao carregar os doces. Verifique o link da planilha!")
        return pd.DataFrame()

df_estoque = carregar_estoque()

# ESTILO PARA FICAR BONITO
st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {display: none;}
        .main { background-color: #fffafb; }
        .stButton button { background-color: #ffb7c5; color: white; border-radius: 20px; width: 100%; }
    </style>
""", unsafe_allow_html=True)

# Link das fotos no seu GitHub
LINK_FOTOS = "https://raw.githubusercontent.com/gabrielassisgomes015-byte/docemaju/main/"

# --- INTERFACE DA LOJA ---
st.title("🧁 Doce Maju")
st.write("### Feito com amor para adoçar seu dia!")

if not df_estoque.empty:
    col_loja, col_carrinho = st.columns([2, 1])

    with col_loja:
        itens_selecionados = {}
        c1, c2 = st.columns(2)
        
        # Filtra apenas o que sua irmã marcou como disponível (Sim)
        produtos_ativos = df_estoque[df_estoque['Disponível'].astype(str).str.upper() == 'SIM']
        
        for i, (index, row) in enumerate(produtos_ativos.iterrows()):
            target_col = c1 if i % 2 == 0 else c2
            with target_col:
                with st.container(border=True):
                    # Puxa a imagem usando o nome que está na planilha
                    st.image(LINK_FOTOS + str(row['Imagem']), use_container_width=True)
                    st.subheader(row['Produto'])
                    st.write(f"R$ {row['Preço']:.2f}")
                    
                    qtd = st.number_input(f"Quantidade", 0, 20, key=f"venda_{row['Produto']}")
                    if qtd > 0:
                        itens_selecionados[row['Produto']] = {
                            "qtd": qtd, 
                            "preco": row['Preço'], 
                            "subtotal": qtd * row['Preço']
                        }

    with col_carrinho:
        with st.container(border=True):
