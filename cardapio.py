import streamlit as st

# 1. Configuração e "Modo Claro" Forçado
st.set_page_config(page_title="Doce Maju", page_icon="🧁", layout="wide")

st.markdown("""
    <style>
    /* Força o fundo branco e tira o preto do Dark Mode */
    .stApp { background-color: #ffffff !important; color: #5d4037 !important; }
    
    /* Títulos com a cor do logo */
    h1, h2, h3 { color: #d4a5b9 !important; font-family: 'Segoe UI', sans-serif; }

    /* Deixando os campos de texto brancos e delicados */
    input { background-color: #ffffff !important; border: 1px solid #fce4ec !important; color: #5d4037 !important; border-radius: 10px !important; }
    
    /* BOTÕES PEQUENOS E REDONDOS (Estilo iFood) */
    div.stButton > button {
        background-color: #d4a5b9 !important;
        color: white !important;
        border-radius: 20px !important;
        border: none !important;
        padding: 5px 15px !important;
        font-size: 14px !important;
        height: auto !important;
        width: auto !important; /* Não ocupa a tela toda */
        transition: 0.3s;
    }

    /* Card dos Doces - Clean e com vida */
    .doce-card {
        background: #fff;
        padding: 15px;
        border-radius: 15px;
        border: 1px solid #fce4ec;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
        margin-bottom: 10px;
    }
    
    /* Esconde o menu de cima do Streamlit */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("<h1 style='text-align: center;'>🧁 Doce Maju</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #5d4037;'>BOLOS & DOCES | Feito com amor</p>", unsafe_allow_html=True)

st.write("---")

# --- CONTEÚDO EM DUAS COLUNAS ---
col_cardapio, col_pedido = st.columns([1.5, 1])

with col_cardapio:
    st.subheader("🌸 Cardápio do Dia")
    
    doces = {
        "Bombom de Uva": 11.0,
        "Bombom de Morango": 11.0,
        "Bolo de Brigadeiro": 7.5,
        "Chocolate com Morango": 7.5
    }
    
    carrinho = {}
    
    for doce, preco in doces.items():
        st.markdown(f"""
            <div class="doce-card">
                <b>{doce}</b><br>
                <span style="color: #d4a5b9;">R$ {preco:.2f}</span>
            </div>
        """, unsafe_allow_html=True)
        
        # Seletor pequeno de quantidade
        qtd = st.number_input(f"Qtd {doce}", min_value=0, max_value=10, key=doce, label_visibility="collapsed")
        if qtd > 0:
            carrinho[doce] = {"qtd": qtd, "subtotal": qtd * preco}

with col_pedido:
    st.subheader("🛒 Meu Carrinho")
    
    if not carrinho:
        st.write("Selecione um doce ao lado! ✨")
    else:
        total = 0
        for item, info in carrinho.items():
            st.write(f"✅ {info['qtd']}x {item}")
            total += info['subtotal']
        
        st.write("---")
        st.write(f"**Total: R$ {total + 3.0:.2f}** (com entrega)")
        
        # Campos de texto brancos (sem o preto do vídeo)
        nome = st.text_input("Seu Nome", placeholder="Como te chamamos?")
        endereco = st.text_input("Endereço", placeholder="Rua, número e bairro")
        pagamento = st.selectbox("Pagamento", ["Pix", "Dinheiro", "Cartão"])
        
        if st.button("Finalizar Pedido"):
            if nome and endereco:
                st.success("Pedido enviado! 💖")
                st.balloons()
            else:
                st.error("Preencha os dados de entrega!")
