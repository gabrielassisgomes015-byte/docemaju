import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Doce Maju - Cardápio Online", page_icon="🧁")

# 2. Estilo Visual (Cores Rosa e Marrom)
st.markdown("""
    <style>
    .main { background-color: #fce4ec; }
    .stButton>button { 
        background-color: #6d4c41; 
        color: white; 
        border-radius: 15px; 
        font-weight: bold;
    }
    .stLinkButton>a {
        background-color: #d81b60 !important;
        color: white !important;
        border-radius: 15px;
        text-align: center;
        display: block;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Memória do Estoque
if 'estoque' not in st.session_state:
    st.session_state.estoque = {
        "Bombom": True, 
        "BoloPote": True
    }

# --- BARRA LATERAL (ACESSO RESTRITO PARA A LOJA) ---
st.sidebar.title("🔐 Administração")
senha = st.sidebar.text_input("Senha de acesso:", type="password")

if senha == "maju123":
    st.sidebar.success("Acesso Liberado!")
    st.sidebar.subheader("Controle de Produtos")
    st.session_state.estoque["Bombom"] = st.sidebar.checkbox("Bombom de Pote em estoque", value=st.session_state.estoque["Bombom"])
    st.session_state.estoque["BoloPote"] = st.sidebar.checkbox("Bolos de Pote em estoque", value=st.session_state.estoque["BoloPote"])
else:
    if senha != "":
        st.sidebar.error("Senha incorreta")

# --- CONTEÚDO PRINCIPAL ---
st.title("💖 Doce Maju")
st.write("Bolos & Doces Artesanais - Feito com Amor")
st.divider()

# Seção 1: Bombom de Pote
st.header("🍫 Bombom de Pote - R$ 11,00")
st.write("• Uva com ninho")
st.write("• Morango com ninho")

if st.session_state.estoque["Bombom"]:
    if st.button("🛒 Adicionar Bombom de Pote"):
        st.balloons()
        st.toast("Ótima escolha! Clique no botão de WhatsApp abaixo para finalizar.")
else:
    st.error("🚫 No momento este item está ESGOTADO.")

st.divider()

# Seção 2: Bolos (pote)
st.header("🍰 Bolos (pote) - R$ 7,50")
st.write("• Morango")
st.write("• Brigadeiro")

if st.session_state.estoque["BoloPote"]:
    if st.button("🛒 Adicionar Bolo de Pote"):
        st.balloons()
        st.toast("Delícia! Finalize seu pedido pelo WhatsApp.")
else:
    st.error("🚫 No momento este item está ESGOTADO.")

st.info("🛵 Taxa de entrega fixa: R$ 3,00")
st.divider()

# --- BOTÕES DE CONTATO ---
st.subheader("📩 Finalizar Pedido ou Seguir a Loja")

# Link do WhatsApp com mensagem profissional
link_zap = "https://wa.me/5521967690731?text=Olá!+Vi+o+cardápio+online+da+Doce+Maju+e+gostaria+de+fazer+um+pedido."
st.link_button("💬 Finalizar Pedido no WhatsApp ✅", link_zap)

# Link do Instagram
st.link_button("📸 Visitar nosso Instagram", "https://instagram.com/docemaju.7905216")

st.caption("Cardápio Digital Oficial - Doce Maju ✨")
