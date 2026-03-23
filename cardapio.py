import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Doce Maju", page_icon="🧁", layout="wide")

# 2. CSS COM FUNDO ROSA LINDO
st.markdown("""
    <style>
    /* FUNDO ROSA GRADIENTE PERFEITO */
    .stApp { 
        background: linear-gradient(135deg, #fdf2f8 0%, #fce7f3 25%, #f8bbd9 50%, #fce4ec 75%, #fff 100%) !important; 
        color: #5d4037 !important; 
    }
    .main .block-container {
        background: rgba(255,255,255,0.9) !important;
        border-radius: 20px !important;
        padding: 20px !important;
        box-shadow: 0 10px 40px rgba(212,165,185,0.2) !important;
    }
    header, footer, #MainMenu {visibility: hidden;}
    
    h1, h2, h3 { color: #c084fc !important; font-family: 'Segoe UI', sans-serif; text-align: center; }
    
    /* CARDS DOS DOCES */
    .doce-card {
        background: rgba(255,255,255,0.95) !important;
        border-radius: 20px !important; border: 2px solid rgba(248,187,217,0.4) !important;
        margin-bottom: 15px; text-align: center; box-shadow: 0 8px 25px rgba(212,165,185,0.2) !important;
        transition: all 0.3s ease !important;
    }
    .doce-card:hover { transform: translateY(-5px) !important; box-shadow: 0 15px 35px rgba(212,165,185,0.3) !important; }
    .doce-img { width: 100%; height: 140px; object-fit: cover; border-radius: 18px 18px 0 0; }
    .doce-info { padding: 12px; }
    .doce-nome { font-weight: bold; font-size: 16px; margin-bottom: 4px; color: #8b5cf6 !important; }
    .doce-desc { font-size: 12px; color: #6b7280; line-height: 1.3; margin-bottom: 6px; }
    .doce-preco { color: #ec4899 !important; font-weight: bold; font-size: 15px; }
    
    /* BOTÕES ROSA */
    div.stButton > button {
        background: linear-gradient(145deg, #ec4899, #f472b6) !important;
        color: white !important; border-radius: 25px !important; border: none !important;
        padding: 6px 16px !important; font-size: 12px !important; font-weight: bold !important;
        height: 32px !important; box-shadow: 0 4px 15px rgba(236,72,153,0.4) !important;
    }
    div.stButton > button:hover {
        background: linear-gradient(145deg, #db2777, #ec4899) !important;
        box-shadow: 0 8px 25px rgba(236,72,153,0.6) !important;
    }
    
    /* BOTÕES PAGAMENTO */
    [data-testid="column"]:nth-child(1) div.stButton > button,
    [data-testid="column"]:nth-child(2) div.stButton > button,
    [data-testid="column"]:nth-child(3) div.stButton > button {
        background: linear-gradient(145deg, #fef3f2, #fce7f3) !important;
        color: #ec4899 !important; border: 2px solid rgba(236,72,153,0.3) !important;
        padding: 5px 14px !important; font-size: 11px !important; height: 28px !important;
    }
    [data-testid="column"]:nth-child(1) div.stButton > button:hover,
    [data-testid="column"]:nth-child(2) div.stButton > button:hover,
    [data-testid="column"]:nth-child(3) div.stButton > button:hover {
        background: linear-gradient(145deg, #ec4899, #f472b6) !important;
        color: white !important;
    }
    
    /* Campos de texto */
    .stTextInput > div > div > input {
        background: rgba(255,255,255,0.95) !important; color: #5d4037 !important;
        border: 2px solid rgba(248,187,217,0.5) !important; border-radius: 15px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- TOPO ---
st.markdown("""
    <div style='background: linear-gradient(135deg, #ec4899, #f472b6, #f9a8d4); 
                padding: 25px; border-radius: 25px; text-align: center; 
                box-shadow: 0 15px 50px rgba(236,72,153,0.4); margin-bottom: 25px;'>
        <h1 style='color: white !important; margin: 0; font-size: 2.8em;'>Doce Maju</h1>
        <p style='color: rgba(255,255,255,0.95); margin: 8px 0 0 0; font-size: 1.3em;'>BOLOS & DOCES | Feito com amor 💕</p>
    </div>
""", unsafe_allow_html=True)

# --- DOCES ---
doces = {
    "Bombom de Uva": {"p": 11.0, "d": "Uva selecionada com creme de Ninho", "img": "https://via.placeholder.com/200x140/fce4ec/f472b6?text=Bombom+de+Uva"},
    "Bolo de Pote": {"p": 8.0, "d": "Massa artesanal super molhadinha", "img": "https://via.placeholder.com/200x140/fef3f2/ec4899?text=Bolo+de+Pote"},
    "Brigadeiro": {"p": 7.5, "d": "Chocolate belga 50% cacau", "img": "https://via.placeholder.com/200x140/f8fafc/1e293b?text=Brigadeiro"},
    "Sensação": {"p": 7.5, "d": "Morango fresco com ganache", "img": "https://via.placeholder.com/200x140/fefce8/92400e?text=Sensação"}
}

# --- SESSION STATE ---
if 'carrinho' not in st.session_state:
    st.session_state.carrinho = {}
if 'entrega' not in st.session_state:
    st.session_state.entrega = False
if 'pagamento' not in st.session_state:
    st.session_state.pagamento = None

# --- LAYOUT ---
col_menu, col_pedido = st.columns([1.8, 1])

with col_menu:
    st.markdown("### 🌸 Cardápio")
    c1, c2 = st.columns(2)
    
    for i, (nome, info) in enumerate(doces.items()):
        lado = c1 if i % 2 == 0 else c2
        with lado:
            st.markdown(f"""
                <div class="doce-card">
                    <img src="{info['img']}" class="doce-img">
                    <div class="doce-info">
                        <div class="doce-nome">{nome}</div>
                        <div class="doce-desc">{info['d']}</div>
                        <div class="doce-preco">R$ {info['p']:.2f}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            col_btn1, col_btn2 = st.columns([3, 1])
            with col_btn2:
                if st.button(f"+ {nome}", key=f"add_{nome}"):
                    if nome not in st.session_state.carrinho:
                        st.session_state.carrinho[nome] = 0
                    st.session_state.carrinho[nome] += 1
            
            if nome in st.session_state.carrinho and st.session_state.carrinho[nome] > 0:
                col_qtd1, col_qtd2, col_qtd3 = st.columns([2, 1, 1])
                with col_qtd2:
                    if st.button("−", key=f"menos_{nome}"):
                        st.session_state.carrinho[nome] -= 1
                        if st.session_state.carrinho[nome] <= 0:
                            del st.session_state.carrinho[nome]
                with col_qtd3:
                    st.markdown(f"<div style='font-weight: bold; color: #ec4899; font-size: 14px;'>{st.session_state.carrinho[nome]}x</div>", unsafe_allow_html=True)

with col_pedido:
    st.markdown("### 🛒 Seu Pedido")
    
    if not st.session_state.carrinho:
        st.markdown("**💖 Escolha as delícias ao lado!**")
    else:
        total_produtos = 0
        for nome, qtd in st.session_state.carrinho.items():
            preco = doces[nome]["p"]
            subtotal = qtd * preco
            total_produtos += subtotal
            st.write(f"🍰 **{qtd}x** {nome} - R$ {subtotal:.2f}")
        
        st.divider()
        
        col_entrega1, col_entrega2 = st.columns([3, 1])
        with col_entrega1:
            st.markdown("**📦 Quer entrega?**")
        with col_entrega2:
            st.session_state.entrega = st.toggle("Sim", value=st.session_state.entrega)
        
        valor_entrega = 3.0 if st.session_state.entrega else 0.0
        total_geral = total_produtos + valor_entrega
        
        st.markdown(f"**Produtos:** R$ {total_produtos:.2f}")
        st.markdown(f"**Entrega:** R$ {valor_entrega:.2f}")
        st.markdown(f"### **TOTAL: R$ {total_geral:.2f}**")
        
        st.divider()
        
        nome = st.text_input("👩 Seu Nome")
        if st.session_state.entrega:
            endereco = st.text_input("📍 Endereço completo")
        
        st.markdown("**💳 Como pagar?**")
        col_pix, col_din, col_cart = st.columns(3)
        with col_pix:
            if st.button("💳 Pix", key="pix"):
                st.session_state.pagamento = "Pix"
        with col_din:
            if st.button("💵 Dinheiro", key="din"):
                st.session_state.pagamento = "Dinheiro"
        with col_cart:
            if st.button("💳 Cartão", key="cart"):
                st.session_state.pagamento = "Cartão"
        
        if st.session_state.pagamento:
            st.success(f"✅ Pagamento: **{st.session_state.pagamento}**")
        
        if st.button("✨ Finalizar Pedido", use_container_width=True):
            if nome and st.session_state.pagamento:
                st.balloons()
                st.markdown(f"""
                <div style='background: linear-gradient(135deg, #ecfdf5, #d1fae5); 
                            color: #065f46; padding: 25px; border-radius: 20px; 
                            text-align: center; border: 3px solid #10b981; 
                            box-shadow: 0 10px 40px rgba(16,185,129,0.3);'>
                    <h3 style='color: #065f46 !important;'>🎉 Pedido Confirmado!</h3>
                    <p style='font-size: 16px;'><strong>{nome}</strong></p>
                    <p style='font-size: 18px; font-weight: bold;
