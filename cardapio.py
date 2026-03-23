import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Doce Maju", page_icon="🧁", layout="wide")

# 2. CSS COM FUNDO ROSA LINDO + GRADIENTE
st.markdown("""
    <style>
    /* FUNDO ROSA SUAVE COM GRADIENTE (Perfeito pro logo!) */
    .stApp { 
        background: linear-gradient(135deg, #fdf2f8 0%, #fce7f3 25%, #f8bbd9 50%, #fce4ec 75%, #fff 100%) !important; 
        color: #5d4037 !important; 
    }
    
    /* Container principal com sombra suave */
    .main .block-container {
        background: rgba(255,255,255,0.85) !important;
        border-radius: 20px !important;
        padding: 20px !important;
        box-shadow: 0 10px 40px rgba(212,165,185,0.15) !important;
        backdrop-filter: blur(10px);
    }
    
    header, footer, #MainMenu {visibility: hidden;}
    
    /* Títulos lilás */
    h1, h2, h3 { color: #c084fc !important; font-family: 'Segoe UI', sans-serif; text-align: center; text-shadow: 0 2px 4px rgba(0,0,0,0.1); }
    
    /* CARDS DOS DOCES (Fundo branco translúcido) */
    .doce-card {
        background: rgba(255,255,255,0.95) !important;
        border-radius: 20px !important; 
        border: 2px solid rgba(248,187,217,0.4) !important;
        margin-bottom: 15px; text-align: center; 
        box-shadow: 0 8px 25px rgba(212,165,185,0.2) !important;
        transition: all 0.3s ease !important;
    }
    .doce-card:hover {
        transform: translateY(-5px) !important;
        box-shadow: 0 15px 35px rgba(212,165,185,0.3) !important;
    }
    .doce-img { width: 100%; height: 140px; object-fit: cover; border-radius: 18px 18px 0 0; }
    .doce-info { padding: 12px; }
    .doce-nome { font-weight: bold; font-size: 16px; margin-bottom: 4px; color: #8b5cf6 !important; }
    .doce-desc { font-size: 12px; color: #6b7280; line-height: 1.3; margin-bottom: 6px; }
    .doce-preco { color: #ec4899 !important; font-weight: bold; font-size: 15px; text-shadow: 0 1px 2px rgba(0,0,0,0.1); }
    
    /* BOTÕES ROSA GRADIENTE (Pequenos e lindos) */
    div.stButton > button {
        background: linear-gradient(145deg, #ec4899, #f472b6) !important;
        color: white !important; border-radius: 25px !important; border: none !important;
        padding: 6px 16px !important; font-size: 12px !important; font-weight: bold !important;
        height: 32px !important; box-shadow: 0 4px 15px rgba(236,72,153,0.4) !important;
        transition: all 0.3s !important;
    }
    div.stButton > button:hover {
        background: linear-gradient(145deg, #db2777, #ec4899) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(236,72,153,0.6) !important;
    }
    
    /* BOTÕES DE PAGAMENTO (Mini e delicados) */
    .pagamento-btn {
        background: linear-gradient(145deg, #fef3f2, #fce7f3) !important;
        color: #ec4899 !important; border: 2px solid rgba(236,72,153,0.3) !important;
        padding: 5px 14px !important; font-size: 11px !important; margin: 2px !important;
        height: 28px !important; border-radius: 20px !important;
        font-weight: 600 !important;
    }
    .pagamento-btn:hover {
        background: linear-gradient(145deg, #ec4899, #f472b6) !important;
        color: white !important;
        box-shadow: 0 4px 15px rgba(236,72,153,0.4) !important;
    }
    
    /* Toggle de entrega lindo */
    .stToggle > div > div {
        background: linear-gradient(145deg, #fef3f2, #fce7f3) !important;
        border: 2px solid rgba(236,72,153,0.3) !important;
        border-radius: 20px !important;
    }
    
    /* Campos de texto com borda rosa */
    .stTextInput > div > div > input {
        background: rgba(255,255,255,0.95) !important; 
        color: #5d4037 !important;
        border: 2px solid rgba(248,187,217,0.5) !important; 
        border-radius: 15px !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05) !important;
    }
    
    /* Mensagens de sucesso */
    .stSuccess {
        background: linear-gradient(145deg, #ecfdf5, #d1fae5) !important;
        border: 2px solid #10b981 !important;
        border-radius: 15px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- TOPO COM GRADIENTE ---
st.markdown("""
    <div style='
        background: linear-gradient(135deg, #ec4899, #f472b6, #f9a8d4); 
        padding: 20px; 
        border-radius: 25px; 
        text-align: center; 
        box-shadow: 0 10px 40px rgba(236,72,153,0.3);
        margin-bottom: 20px;
    '>
        <h1 style='color: white !important; margin: 0; text-shadow: 0 4px 8px rgba(0,0,0,0.3); font-size: 2.5em;'>Doce Maju</h1>
        <p style='color: rgba(255,255,255,0.95); margin: 5px 0 0 0; font-size: 1.2em; font-weight: 500;'>BOLOS & DOCES | Feito com amor 💕</p>
    </div>
""", unsafe_allow_html=True)

# --- RESTO DO CÓDIGO (igual ao anterior, só mudei o CSS) ---
doces = {
    "Bombom de Uva": {"p": 11.0, "d": "Uva selecionada com creme de Ninho", "img": "https://via.placeholder.com/200x140/fce4ec/f472b6?text=Bombom+de+Uva"},
    "Bolo de Pote": {"p": 8.0, "d": "Massa artesanal super molhadinha", "img": "https://via.placeholder.com/200x140/fef3f2/ec4899?text=Bolo+de+Pote"},
    "Brigadeiro": {"p": 7.5, "d": "Chocolate belga 50% cacau", "img": "https://via.placeholder.com/200x140/f8fafc/1e293b?text=Brigadeiro"},
    "Sensação": {"p": 7.5, "d": "Morango fresco com ganache", "img": "https://via.placeholder.com/200x140/fefce8/92400e?text=Sensação"}
}

if 'carrinho' not in st.session_state:
    st.session_state.carrinho = {}
if 'entrega' not in st.session_state:
    st.session_state.entrega = False
if 'pagamento' not in st.session_state:
    st.session_state.pagamento = None

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
                    st.rerun()
            
            if nome in st.session_state.carrinho and st.session_state.carrinho[nome] > 0:
                col_qtd1, col_qtd2, col_qtd3 = st.columns([2, 1, 1])
                with col_qtd2:
                    if st.button("−", key=f"menos_{nome}"):
                        st.session_state.carrinho[nome] -= 1
                        if st.session_state.carrinho[nome] == 0:
                            del st.session_state.carrinho[nome]
                        st.rerun()
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
