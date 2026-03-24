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
        if senha == "maju123": # Você pode mudar essa senha
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("Senha incorreta!")
else:
    # --- CONEXÃO COM A PLANILHA ---
    # Substitua o link abaixo pelo link da sua planilha do Google (com permissão de edição)
    url = "https://docs.google.com/spreadsheets/d/17OOn8U96k3eDg_PeN0QMlIzzfCiftx6kheqqLcnD97c/edit?gid=0#gid=0"
    conn = st.connection("gsheets", type=GSheetsConnection)
    
    df = conn.read(spreadsheet=url)

    st.title("⚙️ Painel de Controle")
    st.write("Olá Maju! Aqui você gerencia sua loja em tempo real.")

    tab1, tab2 = st.tabs(["📦 Estoque e Preços", "💳 Configurações"])

    with tab1:
        st.subheader("Cardápio Atual")
        st.write("Dica: Clique duas vezes na célula para mudar o preço ou o nome.")
        
        # Editor de tabela estilo Excel
        df_editado = st.data_editor(df, num_rows="dynamic")

        if st.button("💾 SALVAR ALTERAÇÕES NA LOJA"):
            conn.update(spreadsheet=url, data=df_editado)
            st.success("Tudo atualizado! O site dos clientes já está com os novos dados.")
            st.balloons()

    with tab2:
        st.subheader("Dados de Recebimento")
        st.info("Aqui você poderá configurar sua chave Pix e taxas no futuro.")
        if st.button("Sair do Painel"):
            st.session_state.autenticado = False
            st.rerun()
