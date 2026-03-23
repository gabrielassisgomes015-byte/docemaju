import streamlit as st

# 1. Configuração da Página (Título e Layout)
st.set_page_config(page_title="PDV Moderno", layout="wide")

# 2. Estilo Customizado (Opcional - para botões mais bonitos)
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #2e7d32;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Divisão da Tela: Coluna Esquerda (Cardápio) e Direita (Checkout)
col_cardapio, col_checkout = st.columns([2, 1])

with col_cardapio:
    st.header("🍴 Nosso Cardápio")
    
    # Criando uma grade (grid) de produtos
    p_col1, p_col2 = st.columns(2)
    
    with p_col1:
        st.image("https://placeholder.com", caption="Hambúrguer X-Tudo")
        st.write("**R$ 25,00**")
        if st.button("Adicionar", key="btn1"):
            st.toast("Adicionado ao carrinho!")

    with p_col2:
        st.image("https://placeholder.com", caption="Batata Especial")
        st.write("**R$ 18,00**")
        if st.button("Adicionar", key="btn2"):
            st.toast("Adicionado ao carrinho!")

with col_checkout:
    st.header("💰 Finalizar")
    st.write("---")
    
    st.subheader("Forma de Pagamento")
    
    # Botões de pagamento organizados
    pay_col1, pay_col2 = st.columns(2)
    with pay_col1:
        st.button("💳 Cartão")
        st.button("💵 Dinheiro")
    with pay_col2:
        st.button("📱 PIX")
        st.button("➕ Outro")
    
    st.write("---")
    st.metric(label="Total a Pagar", value="R$ 43,00")
    
    if st.button("CONCLUIR VENDA", type="primary"):
        st.success("Venda realizada com sucesso!")
