import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Doce Maju", page_icon="🧁", layout="wide")

# 2. Design "Blindado" (Não vai ficar preto e não vai dar erro)
st.markdown("""
    <style>
    /* Força o fundo branco e texto marrom */
    .stApp { background-color: white !important; color: #5d4037 !important; }
    
    /* Esconde menus desnecessários */
    header, footer, #MainMenu {visibility: hidden;}

    /* Título Doce Maju Rosa */
    .titulo {
        color: #d4a5b9 !important;
        font-size: 40px !important;
        text-align: center;
        font-weight: bold;
        margin-bottom: 0px;
    }

    /* Card do Doce */
    .card {
        border: 1px solid #fce4ec;
        border-radius: 15px;
        padding: 10px;
        text-align: center;
        margin-bottom: 10px;
        background-color: white;
    }

    /* Botão Pequeno e Rosa */
    div.stButton > button {
        background-color: #d4a5b9 !important;
        color: white !important;
        border-radius: 20px !important;
        border: none !important;
        padding: 5px 15px !important;
        font-size: 14px !important;
        width: auto !important;
        display: block !important;
        margin: 0 auto !important;
    }
    
    /* Garante que os campos de texto não fiquem pretos */
    input { background-color: white !important; color: black !important; }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown('<p class="titulo">Doce Maju</p>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>BOLOS & DOCES | FEITO COM AMOR</p>", unsafe_allow_html=True)

# --- PRODUTOS ---
doces = [
    {"nome": "Bombom de Uva", "preco": 11.0, "desc": "Uva com creme de Ninho", "foto": "https://via.placeholder.com/150"},
    {"nome": "Bolo de Pote", "preco": 8.0, "desc": "Massa molhadinha", "foto": "https://via.placeholder.com/150"},
    {"nome": "Brigadeiro", "preco": 7.5, "desc": "Chocolate 50%", "foto": "https://via.placeholder.com/150"},
    {"nome": "Sensação", "preco": 7.5, "desc": "Morango e chocolate", "foto": "https://via.placeholder.com/150"}
]

# --- LAYOUT LADO A LADO ---
col_lista, col_carrinho = st.columns([1.5, 1])

with col_lista:
    st.subheader("🌸 Cardápio")
    c1, c2 = st.columns(2)
    escolhidos = {}

    for i, d in enumerate(doces):
        aba = c1 if i % 2 == 0 else c2
        with aba:
            st.markdown(f"""
                <div class="card">
                    <img src="{d['foto']}" style="width:100%; border-radius:10px;">
                    <div style="font-weight:bold; margin-top:5px;">{d['nome']}</div>
                    <div style="font-size:11px; color:gray;">{d['desc']}</div>
                    <div style="color:#d4a5b9; font-weight:bold;">R$ {d['preco']:.2f}</div>
                </div>
            """, unsafe_allow_html=True)
            
            # Seletor de quantidade (Python puro)
            qtd = st.number_input(f"Qtd {d['nome']}", 0, 10, key=d['nome'], label_visibility="collapsed")
            if qtd > 0:
                escolhidos[d['nome']] = {"qtd": qtd, "sub": qtd * d['preco']}

with col_carrinho:
    st.markdown("<div style='background-color:#fff9fa; padding:15px; border-radius:15px; border:1px solid #fce4ec;'>", unsafe_allow_html=True)
    st.subheader("🛒 Pedido")
    
    if not escolhidos:
        st.write("Escolha um doce! ✨")
    else:
        total = 0
        for nome, info in escolhidos.items():
            st.write(f"💗 {info['qtd']}x {nome}")
            total += info['sub']
        
        st.write("---")
        st.write(f"**Total: R$ {total + 3.0:.2f}**")
        
        # Campos simples
        st.text_input("Seu Nome", key="nome_cli")
        st.text_input("Endereço", key="end_cli")
        st.selectbox("Pagamento", ["Pix", "Dinheiro", "Cartão"], key="pag_cli")
        
        if st.button("Finalizar Compra"):
            st.success("Pedido enviado! 💖")
            st.balloons()
    st.markdown("</div>", unsafe_allow_html=True)
