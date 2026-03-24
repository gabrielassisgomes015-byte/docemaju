import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Doce Maju", page_icon="🧁", layout="wide")

# 2. DESIGN PERSONALIZADO (Fundo Rosa, Pedido Vermelho e Botões Pequenos)
st.markdown("""
    <style>
    /* FUNDO ROSA CLARINHO */
    .stApp { background-color: #ffe4e8 !important; }
    
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
        margin: 0 20px;
    }

    /* Cards Brancos do Cardápio */
    .card {
        background-color: white !important;
        border-radius: 20px;
        padding: 15px;
        text-align: center;
        margin-bottom: 10px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    }

    /* COLUNA DO PEDIDO - FUNDO VERMELHO CEREJA */
    .container-pedido {
        background-color: #e63946 !important; /* Vermelho bonito */
        padding: 20px;
        border-radius: 25px;
        color: white !important; /* Letras Brancas para ler bem */
        box-shadow: 0px 10px 20px rgba(0,0,0,0.1);
    }

    /* Botão Pequeno e Rosa */
    div.stButton > button {
        background-color: #d4a5b9 !important;
        color: white !important;
        border-radius: 25px !important;
        border: 2px solid white !important;
        font-size: 14px !important;
        font-weight: bold;
    }

    /* Ajuste dos inputs para ficarem brancos e legíveis */
    input { background-color: white !important; color: black !important; border-radius: 10px !important; }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown('<p class="titulo">Doce Maju</p>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #5d4037; font-weight: bold;'>🧁 FEITO COM AMOR 🧁</p>", unsafe_allow_html=True)

# --- PRODUTOS (Nomes Exatos que você enviou) ---
doces = [
    {"nome": "Bombom Uva com ninho", "preco": 11.0, "desc": "Uvas frescas colhidas com creme de leite Ninho", "foto": "https://via.placeholder.com/150/ffffff/e63946?text=Uva+Ninho"},
    {"nome": "Bombom Morango com ninho", "preco": 11.0, "desc": "Morango suculento com o verdadeiro Ninho", "foto": "https://via.placeholder.com/150/ffffff/e63946?text=Morango+Ninho"},
    {"nome": "Bolo de Pote brigadeiro com morango", "preco": 7.50, "desc": "Explosão de chocolate com pedaços de fruta", "foto": "https://via.placeholder.com/150/ffffff/e63946?text=Bolo+Brigadeiro"}
]

# --- LAYOUT ---
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
                    <div style="font-weight:bold; margin-top:8px; font-size:16px; color:#5d4037;">{d['nome']}</div>
                    <div style="font-size:11px; color:gray; margin-bottom:5px;">{d['desc']}</div>
                    <div style="color:#e63946; font-weight:bold;">R$ {d['preco']:.2f}</div>
                </div>
            """, unsafe_allow_html=True)
            
            qtd = st.number_input(f"Qtd {d['nome']}", 0, 20, key=f"key_{d['nome']}", label_visibility="collapsed")
            if qtd > 0:
                carrinho[d['nome']] = {"qtd": qtd, "sub": qtd * d['preco']}

with col_linha:
    st.markdown('<div class="linha-separadora"></div>', unsafe_allow_html=True)

with col_pedido:
    # AQUI ESTÁ O BOX VERMELHO QUE VOCÊ PEDIU
    st.markdown('<div class="container-pedido">', unsafe_allow_html=True)
    st.markdown("<h3 style='color:white; text-align:center;'>🛒 Seu Pedido</h3>", unsafe_allow_html=True)
    
    if not carrinho:
        st.write("Escolha suas doçuras ao lado! ✨")
    else:
        total = 0
        for nome, info in carrinho.items():
            st.markdown(f"⚪ **{info['qtd']}x** {nome} <br> <small>R$ {info['sub']:.2f}</small>", unsafe_allow_html=True)
            total += info['sub']
        
        st.markdown("<hr style='border: 0.5px solid white;'>", unsafe_allow_html=True)
        st.write(f"**Total Produtos:** R$ {total:.2f}")
        st.write("**Taxa entrega:** R$ 3,00")
        st.markdown(f"## **Total: R$ {total + 3.0:.2f}**")
        
        # Dados Brancos sobre o fundo Vermelho
        st.markdown("**📍 Dados de Entrega:**")
        nome_c = st.text_input("Seu Nome", key="n_cli")
        end_c = st.text_input("Endereço", key="e_cli")
        pag_c = st.selectbox("Pagamento", ["Pix", "Dinheiro", "Cartão"], key="p_cli")
        
        st.write("")
        if st.button("🚀 CONFIRMAR AGORA"):
            if nome_c and end_c:
                st.balloons()
                st.success("Pedido enviado! 💖")
            else:
                st.error("Preencha seu nome e endereço!")
    
    st.markdown('</div>', unsafe_allow_html=True)
