import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.set_page_config(page_title="Painel Administrativo - Doce Maju", page_icon="⚙️")

# --- LOGIN SIMPLES ---
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    senha = st.text_input("Digite a senha para acessar o painel:", type="password")
    if st.button("Entrar"):
        if senha == "maju123":
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("Senha incorreta!")
else:
    # --- CONEXÃO COM A PLANILHA ---
    # Link limpo da sua planilha
    url = "https://docs.google.com/spreadsheets/d/1700n8U96k3eDg_PeN8QM1IzzfCiftx6kheqqLcnD97c/edit"
    
    conn = st.connection("gsheets", type=GSheetsConnection)
    
    # Lê os dados
    df = conn.read(spreadsheet=url)

    st.title("⚙️ Painel de Controle")
    st.write(f"Olá Maju! Aqui você gerencia sua loja em tempo real.")

    tab1, tab2 = st.tabs(["📦 Estoque e Preços", "💳 Configurações"])

    with tab1:
        st.subheader("Cardápio Atual")
        # Editor de tabela estilo Excel
        df_editado = st.data_editor(df, num_rows="dynamic")

        if st.button("💾 SALVAR ALTERAÇÕES NA LOJA"):
            conn.update(spreadsheet=url, data=df_editado)
            st.success("Tudo atualizado! O site dos clientes já está com os novos dados.")
            st.balloons()

    with tab2:
        st.subheader("Dados de Recebimento")
        st.info("Aqui você poderá configurar sua chave Pix no futuro.")
        if st.button("Sair do Painel"):
            st.session_state.autenticado = False
            st.rerun()
