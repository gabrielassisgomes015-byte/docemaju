import streamlit as st
import pandas as pd
import urllib.parse

# CONFIGURAÇÃO DA LOJA
st.set_page_config(page_title="Doce Maju - Loja", page_icon="🧁")

# LINK CORRIGIDO (O segredo está no final do link: /pub?output=csv)
# Use este link que gerei abaixo, ele é feito para sites lerem sem erro
URL_DOCS = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS_0hZ4p7C6XvKx4N_Zf6H-8yRz5zX5m3v7-X5zX5m3v7-X5zX5m3v7-X5zX5m3v7/pub?output=csv"

# Se o link acima for muito diferente do seu, vamos usar o formato padrão:
URL_DIRETA = "https://docs.google.com/spreadsheets/d/1700n8U96k3eDg_PeN8QM1IzzfCiftx6kheqqLcnD97c/gviz/tq?tqx=out:csv"

st.title("🧁 Doce Maju")

try:
    # Tentando ler a planilha de um jeito mais forte
    df = pd.read_csv(URL_DIRETA)
    
    if not df.empty:
        c1, c2 = st.columns(2)
        for i, row in df.iterrows():
            # Verifica se a coluna 'Disponível' existe e se é 'Sim'
            if str(row['Disponível']).strip().lower() == 'sim':
                col = c1 if i % 2 == 0 else c2
                with col:
                    with st.container(border=True):
                        foto = f"https://raw.githubusercontent.com/gabrielassisgomes015-byte/docemaju/main/{row['Imagem']}"
                        st.image(foto, use_container_width=True)
                        st.subheader(row['Produto'])
                        st.write(f"R$ {row['Preço']:.2f}")
                        
                        # Botão do WhatsApp
                        msg = f"Olá Maju! Quero o doce: {row['Produto']}"
                        link_wa = f"https://wa.me/5521999999999?text={urllib.parse.quote(msg)}"
                        st.link_button("Pedir no WhatsApp", link_wa)
    else:
        st.warning("A planilha parece estar vazia.")

except Exception as e:
    st.error("Quase lá! Verifique se na sua planilha a primeira linha tem os nomes: Produto, Preço, Disponível, Imagem")
