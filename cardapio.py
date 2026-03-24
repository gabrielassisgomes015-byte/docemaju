import streamlit as st
import pandas as pd
import urllib.parse

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Doce Maju - Cardápio", page_icon="🧁")

# LINK DA PLANILHA
URL = "https://docs.google.com/spreadsheets/d/1700n8U96k3eDg_PeN8QM1IzzfCiftx6kheqqLcnD97c/gviz/tq?tqx=out:csv"

st.title("🧁 Doce Maju")
st.write("---")

try:
    # Lendo a planilha
    df = pd.read_csv(URL)
    
    # Limpando espaços extras nos nomes das colunas
    df.columns = [c.strip().lower() for c in df.columns]

    if df.empty:
        st.warning("Cadastre os doces na planilha para eles aparecerem aqui!")
    else:
        col1, col2 = st.columns(2)
        
        for i, row in df.iterrows():
            # Verifica se o doce está disponível (procura por 'sim')
            # Usei .get() para evitar erro caso a coluna tenha acento ou não
            disponibilidade = str(row.get('disponível', row.get('disponivel', ''))).strip().lower()
            
            if disponibilidade == 'sim':
                target_col = col1 if i % 2 == 0 else col2
                with target_col:
                    with st.container(border=True):
                        # Puxa a foto do GitHub
                        nome_foto = str(row['imagem']).strip()
                        link_foto = f"https://raw.githubusercontent.com/gabrielassisgomes015-byte/docemaju/main/{nome_foto}"
                        
                        st.image(link_foto, use_container_width=True)
                        st.subheader(row['produto'])
                        st.write(f"R$ {row['preço']}")
                        
                        # Botão de Pedido
                        texto_pedido = f"Olá Maju! Quero o doce: {row['produto']}"
                        link_wa = f"https://wa.me/5521999999999?text={urllib.parse.quote(texto_pedido)}"
                        st.link_button("Pedir no WhatsApp", link_wa)

except Exception as e:
    st.error("Erro de conexão. Verifique se a planilha está 'Publicada na Web'!")
