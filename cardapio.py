import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Doce Maju - Cardápio Online", page_icon="🧁")

# 2. Estilo Visual "Com Vida" (Rosa, Branco e Marrom)
st.markdown("""
    <style>
    .stApp { background-color: #fff5f8; }
    
    h1, h2, h3 { color: #5d4037 !important; }

    /* Cartão do Produto */
    .produto-card {
        background-color: white;
        padding: 15px;
        border-radius: 20px;
        border-left: 8px solid #ff80ab;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }

    /* Botão de Adicionar */
    .stButton>button {
        background-color: #ff80ab !important;
        color: white !important;
        border-radius: 20px !important;
        border: none !important;
        font-weight: bold;
        transition: 0.3s;
    }
    
    .stButton>button:hover { background-color: #f06292 !important; scale: 1.02; }

    /* Botão do WhatsApp */
    .stLinkButton>a {
        background-color: #4caf50 !important;
        color: white !important;
        border-radius: 25px !important;
        text-align: center;
        font-weight: bold;
        padding: 12px;
        display: block;
        text-decoration: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Gerenciamento de Estoque (Senha: maju123)
if 'estoque' not in st.session_state:
    st.session_state.estoque = {
        "Bombom Uva": True, "Bombom Morango": True,
        "Bolo Brigadeiro": True, "Bolo Morango": True, "Bolo Chocolate Morango": True
    }

with st.sidebar:
    st.title("🔐 Administração")
    senha = st.text_input("Senha da Loja:", type="password")
    if senha == "maju123":
        st.success("Acesso Liberado")
        for item in st.session_state.estoque:
            st.session_state.estoque[item] = st.checkbox(f"{item} em estoque", value=st.session_state.estoque[item])

# --- CONTEÚDO DO SITE ---
st.title("🧁 Doce Maju")
st.subheader("Cardápio de Delícias Artesanais")
st.write("---")

def exibir_item(nome, preco, desc, chave):
    st.markdown(f'<div class="produto-card">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])
    with col1:
        # Espaço reservado para sua foto real
        st.image("https://cdn-icons-png.flaticon.com/512/2553/2553642.png", width=90)
    with col2:
        st.markdown(f"**{nome}**")
        st.write(f"R$ {preco}")
        if st.session_state.estoque[chave]:
            if st.button(f"Selecionar {nome}", key=chave):
                st.toast(f"{nome} adicionado!")
                st.balloons()
        else:
            st.error("Esgotado")
    st.markdown('</div>', unsafe_allow_html=True)

# --- SEÇÃO DE BOMBONS ---
st.header("🍫 Bombons de Pote (R$ 11,00)")
exibir_item("Bombom de Uva", "11,00", "Uva com Ninho", "Bombom Uva")
exibir_item("Bombom de Morango", "11,00", "Morango com Ninho", "Bombom Morango")

st.write("")

# --- SEÇÃO DE BOLOS ---
st.header("🍰 Bolos no Pote (R$ 7,50)")
exibir_item("Bolo de Brigadeiro", "7,50", "Chocolate cremoso", "Bolo Brigadeiro")
exibir_item("Bolo de Brigadeiro com Morango", "7,50", "O clássico com fruta", "Bolo Morango")
exibir_item("Chocolate com Morango", "7,50", "Sensação irresistível", "Bolo Chocolate Morango")

st.divider()
st.info("🛵 Taxa de entrega: R$ 3,00")

# --- WHATSAPP ---
link_zap = "https://wa.me/5521967690731?text=Olá!+Gostaria+de+fazer+um+pedido+da+Doce+Maju."
st.link_button("🟢 FINALIZAR PEDIDO NO WHATSAPP", link_zap)
