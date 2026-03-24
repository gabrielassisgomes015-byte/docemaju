import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Doce Maju - Loja", page_icon="🧁", layout="wide")

# --- CONEXÃO COM A PLANILHA ---
# Coloque seu link aqui embaixo
URL_PLANILHA = "https://docs.google.com/spreadsheets/d/17OOn8U96k3eDg_PeN0QMlIzzfCiftx6kheqqLcnD97c/edit?gid=0#gid=0"

def carregar_estoque():
    try:
        url_csv = URL_PLANILHA.replace('/edit?usp=sharing', '/export?format=csv').replace('/edit', '/export?format=csv')
        df = pd.read_csv(url_csv)
        return df
    except:
        return pd.DataFrame()

df_estoque = carregar_estoque()

# ESTILO
st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {display: none;}
        .main { background-color: #fffafb; }
        .stButton button { background-color: #ffb7c5; color: white; border-radius: 20px; width: 100%; }
    </style>
""", unsafe_allow_html=True)

LINK_FOTOS = "https://raw.githubusercontent.com/gabrielassisgomes015-byte/docemaju/main/"

st.title("🧁 Doce Maju")
st.write("### Feito com amor para adoçar seu dia!")

if not df_estoque.empty:
    col_loja, col_carrinho = st.columns([2, 1])

    with col_loja:
        itens_selecionados = {}
        c1, c2 = st.columns(2)
        
        # Filtrar disponíveis
        produtos_ativos = df_estoque[df_estoque['Disponível'].astype(str).str.upper() == 'SIM']
        
        for i, (index, row) in enumerate(produtos_ativos.iterrows()):
            target_col = c1 if i % 2 == 0 else c2
            with target_col:
                # O ERRO ESTAVA AQUI: As linhas abaixo precisam desses espaços na frente
                with st.container(border=True):
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
            st.header("🛒 Seu Pedido")
            if not itens_selecionados:
                st.write("Seu carrinho está vazio.")
            else:
                total_itens = 0
                resumo_whatsapp = ""
                for nome, info in itens_selecionados.items():
                    st.write(f"{info['qtd']}x {nome}")
                    total_itens += info['subtotal']
                    resumo_whatsapp += f"{info['qtd']}x {nome}; "
                
                st.divider()
                envio = st.selectbox("Entrega", ["Retirada (Grátis)", "Entrega (+ R$ 3,00)"])
                taxa = 3.0 if "Entrega" in envio else 0.0
                total_final = total_itens + taxa
                
                endereco = st.text_input("Endereço completo:") if taxa > 0 else "Retirada"
                pagamento = st.selectbox("Pagamento", ["Pix", "Cartão", "Dinheiro"])
                nome_cli = st.text_input("Seu Nome:")
                
                st.subheader(f"Total: R$ {total_final:.2f}")

                if st.button("🚀 FINALIZAR PEDIDO"):
                    if nome_cli:
                        msg = f"*NOVO PEDIDO*\n*Cliente:* {nome_cli}\n*Itens:* {resumo_whatsapp}\n*Total:* R$ {total_final:.2f}"
                        link_wa = f"https://wa.me/5521999999999?text={urllib.parse.quote(msg)}"
                        st.link_button("ENVIAR NO WHATSAPP", link_wa)
                        st.balloons()
                    else:
                        st.error("Digite seu nome!")
else:
    st.error("Coloque o link da planilha no código para os produtos aparecerem!")
