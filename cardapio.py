import streamlit as st
from datetime import datetime

# 1. Configuração da Página
st.set_page_config(
    page_title="Doce Maju - Bolos & Doces", 
    page_icon="🧁", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Estilo Visual baseado no seu Logo (Lilás, Rosa e Marrom)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Fundo Pérola para destacar o logo */
    .stApp { background-color: #fdfafb; }
    
    /* Cores do Logo */
    h1 { color: #d4a5b9 !important; font-family: 'Brush Script MT', cursive; font-size: 50px !important; text-align: center; margin-bottom: 0px;}
    h2, h3 { color: #5d4037 !important; font-family: 'Segoe UI', sans-serif; text-align: center;}
    
    .subtitulo {
        text-align: center;
        color: #5d4037;
        font-weight: bold;
        letter-spacing: 2px;
        margin-top: -20px;
        margin-bottom: 20px;
    }

    /* Card de Produto */
    .produto-card {
        background-color: white;
        padding: 20px;
        border-radius: 20px;
        border: 2px solid #f3e5f5; /* Lilás bem clarinho como a batedeira */
        box-shadow: 0px 4px 15px rgba(212, 165, 185, 0.2);
        margin-bottom: 20px;
    }

    /* Botão Rosa do Logo */
    .stButton>button {
        background-color: #d4a5b9 !important; /* Rosa queimado do logo */
        color: white !important;
        border-radius: 25px !important;
        border: none !important;
        width: 100%;
        font-weight: bold;
        height: 45px;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #c48da4 !important;
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Cabeçalho Personalizado (O SEU LOGO)
col_logo1, col_logo2, col_logo3 = st.columns([1, 2, 1])
with col_logo2:
    # Quando você tiver o link da sua foto, troque o link abaixo:
    st.image("https://cdn-icons-png.flaticon.com/512/9041/9041922.png", width=150) 
    st.markdown("<h1>Doce Maju</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitulo'>BOLOS & DOCES</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#d4a5b9;'>💕 Feito com amor 💕</p>", unsafe_allow_html=True)

# 4. Dados (Cardápio)
if 'pedidos_recebidos' not in st.session_state:
    st.session_state.pedidos_recebidos = []

if 'estoque' not in st.session_state:
    st.session_state.estoque = {
        "Bombom de Uva": {"preco": 11.0, "status": True, "desc": "Uva com creme de Ninho"},
        "Bombom de Morango": {"preco": 11.0, "status": True, "desc": "Morango com creme de Ninho"},
        "Bolo de Brigadeiro": {"preco": 7.5, "status": True, "desc": "Massa fofinha e brigadeiro artesanal"},
        "Bolo de Morango": {"preco": 7.5, "status": True, "desc": "O clássico com frutas frescas"},
        "Chocolate com Morango": {"preco": 7.5, "status": True, "desc": "Combinação perfeita"}
    }

# --- ABAS ---
tab_loja, tab_maju = st.tabs(["🧁 Cardápio", "🔐 Painel Maju"])

with tab_loja:
    carrinho = {}
    st.write("---")
    
    for nome, dados in st.session_state.estoque.items():
        st.markdown('<div class="produto-card">', unsafe_allow_html=True)
        c1, c2 = st.columns([1, 2])
        with c1:
            st.image("https://cdn-icons-png.flaticon.com/512/2553/2553642.png", width=80)
        with c2:
            st.markdown(f"**{nome}**")
            st.caption(dados["desc"])
            st.markdown(f"<span style='color:#d4a5b9; font-weight:bold;'>R$ {dados['preco']:.2f}</span>", unsafe_allow_html=True)
            
            if dados["status"]:
                qtd = st.number_input(f"Qtd", min_value=0, max_value=20, key=f"cli_{nome}")
                if qtd > 0:
                    carrinho[nome] = {"qtd": qtd, "subtotal": qtd * dados["preco"]}
            else:
                st.error("Esgotado")
        st.markdown('</div>', unsafe_allow_html=True)

    if carrinho:
        st.subheader("🛵 Dados para Entrega")
        nome_cli = st.text_input("Seu Nome")
        end_cli = st.text_input("Endereço Completo")
        pag_cli = st.selectbox("Pagamento", ["Pix", "Dinheiro", "Cartão"])
        
        total = sum(i['subtotal'] for i in carrinho.values()) + 3.0
        st.markdown(f"### Total: R$ {total:.2f}")
        
        if st.button("CONFIRMAR PEDIDO"):
            if nome_cli and end_cli:
                st.session_state.pedidos_recebidos.append({
                    "id": len(st.session_state.pedidos_recebidos)+1,
                    "cliente": nome_cli, "end": end_cli, "itens": carrinho.copy(),
                    "total": total, "pag": pag_cli, "status": "Novo",
                    "hora": datetime.now().strftime("%H:%M")
                })
                st.success("Pedido enviado! Prepare o coração para o doce!")
                st.balloons()

with tab_maju:
    senha = st.text_input("Senha", type="password")
    if senha == "maju123":
        if not st.session_state.pedidos_recebidos:
            st.info("Aguardando o primeiro pedido de hoje...")
        else:
            for p in reversed(st.session_state.pedidos_recebidos):
                with st.expander(f"Pedido #{p['id']} - {p['cliente']}"):
                    st.write(f"🏠 {p['end']} | 💰 {p['pag']}")
                    for item, info in p['itens'].items():
                        st.write(f"- {info['qtd']}x {item}")
                    if st.button(f"Entregue #{p['id']}"):
                        p['status'] = "OK"
                        st.rerun()
