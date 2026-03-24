import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Doce Maju", page_icon="🧁", layout="wide")

# 2. DESIGN PERSONALIZADO (Fundo Rosa e Linha Divisória)
st.markdown("""
    <style>
    /* FUNDO ROSA CLARINHO EM TUDO */
    .stApp { 
        background-color: #ffe4e8 !important; 
    }
    
    header, footer, #MainMenu {visibility: hidden;}

    /* Título Doce Maju */
    .titulo {
        color: #d4a5b9 !important;
        font-size: 45px !important;
        text-align: center;
        font-family: 'Times New Roman', serif;
        font-weight: bold;
        margin-bottom: 0px;
    }

    /* Linha que separa o Cardápio do Pedido */
    .linha-separadora {
        border-left: 2px solid #d4a5b9;
        height: 100vh;
        margin-left: 20px;
        margin-right: 20px;
    }

    /* Cards Brancos sobre o fundo rosa */
    .card {
        background-color: white !important;
        border-radius: 20px;
        padding: 15px;
        text-align: center;
        margin-bottom: 15px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    }

    /* Botão Pequeno e Rosa */
    div.stButton > button {
        background-color: #d4a5b9 !important;
        color: white !important;
        border-radius: 25px !important;
        border: none !important;
        padding: 5px 20px !important;
        font-size: 14px !important;
        font-weight: bold;
    }

    /* Ajuste para os textos de input não sumirem no fundo */
    input { background-color: white !important; color: black !important; }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown('<p class="titulo">Doce Maju</p>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #5d4037;'>🧁 BOLOS & DOCES ARTESANAIS 🧁</p>", unsafe_allow_html=True)

# --- PRODUTOS (Nomes consertados) ---
doces = [
    {"nome": "Bombom de Uva", "preco": 11.0, "desc": "Uva verde fresca com creme de Ninho", "foto": "https://via.placeholder.com/150/ffffff/d4a5b9?text=Bombom+Uva"},
    {"nome": "Bolo de Pote Gourmet", "preco": 8.0, "desc": "Camadas cremosas de puro sabor", "foto": "https://via.placeholder.com/150/ffffff/d4a5b9?text=Bolo+Pote"},
    {"nome": "Brigadeiro Tradicional", "preco": 7.5, "desc": "Receita clássica com chocolate 50%", "foto": "https://via.placeholder.com/150/ffffff/d4a5b9?text=Brigadeiro"},
    {"nome": "Sensação de Morango", "preco": 7.5, "desc": "Morango com ganache de chocolate", "foto": "https://via.placeholder.com/150/ffffff/d4a5b9?text=Sensação"}
]

# --- LAYOUT COM SEPARAÇÃO ---
col_cardapio, col_linha, col_pedido = st.columns([1.5, 0.1, 1])

with col_cardapio:
    st.markdown("### 🌸 Nosso Cardápio")
    c1, c2 = st.columns(2)
    carrinho = {}

    for i, d in enumerate(doces):
        lado = c1 if i % 2 == 0 else c2
        with lado:
            st.markdown(f"""
                <div class="card">
                    <img src="{d['foto']}" style="width:100%; border-radius:12px;">
                    <div style="font-weight:bold; margin-top:8px; font-size:18px;">{d['nome']}</div>
                    <div style="font-size:12px; color:gray; margin-bottom:5px;">{d['desc']}</div>
                    <div style="color:#d4a5b9; font-weight:bold; font-size:16px;">R$ {d['preco']:.2f}</div>
                </div>
            """, unsafe_allow_html=True)
            
            # Seletor discreto
            qtd = st.number_input(f"Qtd {d['nome']}", 0, 20, key=f"key_{d['nome']}", label_visibility="collapsed")
            if qtd > 0:
                carrinho[d['nome']] = {"qtd": qtd, "sub": qtd * d['preco']}

with col_linha:
    # Cria a linha vertical visual
    st.markdown('<div class="linha-separadora"></div>', unsafe_allow_html=True)

with col_pedido:
    # Fundo branco para a área do carrinho também
    st.markdown("<div style='background-color:white; padding:20px; border-radius:20px;'>", unsafe_allow_html=True)
    st.markdown("### 🛒 Seu Pedido")
    
    if not carrinho:
        st.write("Selecione suas doçuras ao lado! ✨")
    else:
        total = 0
        for nome, info in carrinho.items():
            st.write(f"💖 **{info['qtd']}x** {nome}")
            total += info['sub']
        
        st.divider()
        st.write(f"**Total Produtos:** R$ {total:.2f}")
        st.write("**Taxa de Entrega:** R$ 3,00")
        st.markdown(f"## **Total: R$ {total + 3.0:.2f}**")
        
        # Dados do Cliente
        st.text_input("Seu Nome")
        st.text_input("Endereço Completo")
        st.selectbox("Forma de Pagamento", ["Pix", "Dinheiro", "Cartão"])
        
        if st.button("🚀 FINALIZAR PEDIDO"):
            st.balloons()
            st.success("Pedido enviado com sucesso!")
    
    st.markdown("</div>", unsafe_allow_html=True)
