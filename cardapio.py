import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Doce Maju", page_icon="🧁", layout="wide")

# 2. MÁGICA DO DESIGN (CSS para copiar a foto)
st.markdown("""
    <style>
    /* Fundo degradê igual da foto */
    .stApp {
        background: linear-gradient(135deg, #ffafbd 0%, #c9ffbf 100%); /* Um degradê suave */
        background-image: linear-gradient(to right, #f8a5c2, #cd84f1) !important;
    }

    /* Esconder o que não precisa */
    header, footer {visibility: hidden;}

    /* Título Doce Maju com a fonte bonitinha */
    .titulo-topo {
        color: white;
        font-family: 'Brush Script MT', cursive;
        font-size: 60px;
        text-align: center;
        text-shadow: 2px 2px #d4a5b9;
        margin-bottom: 0px;
    }

    /* Estilo do Cardápio (Lado Esquerdo Rosa) */
    .cardapio-container {
        background-color: rgba(255, 105, 180, 0.8);
        padding: 20px;
        border-radius: 30px;
        border: 3px dashed white;
        color: white;
    }

    /* Estilo do Carrinho (Lado Direito Roxo/Branco) */
    .carrinho-container {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 20px;
        border-radius: 30px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.1);
        color: #5d4037;
    }

    /* Botão "Finalizar" igual da foto (Rosa com brilho) */
    div.stButton > button {
        background: linear-gradient(to bottom, #ff4d94, #ff0066) !important;
        color: white !important;
        border-radius: 30px !important;
        border: 2px solid white !important;
        font-weight: bold !important;
        font-size: 20px !important;
        height: 50px !important;
        width: 100% !important;
        box-shadow: 0px 5px 15px rgba(255, 0, 102, 0.4) !important;
    }

    /* Cards dos Doces Individuais */
    .doce-item {
        background: white;
        border-radius: 15px;
        padding: 10px;
        margin-bottom: 10px;
        color: #5d4037;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 2px solid #fce4ec;
    }
    </style>
    """, unsafe_allow_html=True)

# --- TOPO ---
st.markdown('<p class="titulo-topo">Doce Maju</p>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:white; font-size:20px;'>🧁 Bolos & Bombons de Pote 🧁</p>", unsafe_allow_html=True)

# --- BANCO DE DADOS ---
cardapio = {
    "Bolos de Pote": {
        "Brigadeiro": 8.0,
        "Prestigio": 8.0,
        "Morango c/ Ninho": 8.0,
        "Oreo & Nutella": 8.0
    },
    "Bombons de Pote": {
        "Ferrero Rocher": 10.0,
        "Sonho de Valsa": 10.0,
        "Ouro Branco": 10.0,
        "Beijinho": 10.0
    }
}

# --- LAYOUT ---
col1, col_espaço, col2 = st.columns([1.2, 0.1, 1])

with col1:
    st.markdown('<div class="cardapio-container">', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:white;'>❤ Cardápio ❤</h2>", unsafe_allow_html=True)
    
    escolhidos = {}
    
    for categoria, itens in cardapio.items():
        st.markdown(f"### ✨ {categoria}")
        for nome, preco in itens.items():
            # Criando o seletor de quantidade
            qtd = st.number_input(f"{nome} (R$ {preco:.2f})", min_value=0, max_value=20, key=nome)
            if qtd > 0:
                escolhidos[nome] = {"qtd": qtd, "preco": preco, "sub": qtd * preco}
    
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="carrinho-container">', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center;'>🛒 Meu Pedido</h2>", unsafe_allow_html=True)
    
    if not escolhidos:
        st.write("Seu carrinho está vazio... por enquanto! 😉")
    else:
        total = 0
        for nome, info in escolhidos.items():
            st.markdown(f"💗 **{info['qtd']}x** {nome} --- R$ {info['sub']:.2f}")
            total += info['sub']
        
        st.divider()
        st.markdown(f"### **Total: R$ {total:.2f}**")
        
        st.markdown("---")
        st.markdown("### 💳 Pagamento")
        pag = st.radio("Escolha a forma:", ["Pix", "Dinheiro", "Cartão de Crédito", "Cartão de Débito"], horizontal=True)
        
        st.text_input("Seu Nome")
        st.text_input("Endereço de Entrega")
        
        if st.button("💖 Finalizar Compra 💖"):
            st.balloons()
            st.success("Pedido enviado via WhatsApp!")
            
    st.markdown('</div>', unsafe_allow_html=True)
