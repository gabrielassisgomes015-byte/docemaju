import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Doce Maju", page_icon="🧁", layout="wide")

# 2. LIMPEZA TOTAL DO DESIGN (Adeus botões pretos!)
st.markdown("""
    <style>
    /* Força fundo branco e texto marrom do logo */
    .stApp { background-color: #ffffff !important; color: #5d4037 !important; }
    
    /* Remove barras e menus desnecessários */
    header, footer, #MainMenu {visibility: hidden;}

    /* Títulos com a cor da batedeira (Lilás/Rosa) */
    h1, h2, h3 { color: #d4a5b9 !important; font-family: 'Segoe UI', sans-serif; text-align: center; }

    /* CARD DO DOCE (Foto em cima, descrição embaixo) */
    .doce-card {
        background: #fff;
        border-radius: 15px;
        border: 1px solid #fce4ec;
        margin-bottom: 15px;
        text-align: center;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.03);
    }
    .doce-img { width: 100%; height: 130px; object-fit: cover; border-radius: 15px 15px 0 0; }
    .doce-info { padding: 8px; }
    .doce-nome { font-weight: bold; font-size: 15px; margin-bottom: 2px; }
    .doce-desc { font-size: 11px; color: #888; line-height: 1.1; margin-bottom: 5px; }
    .doce-preco { color: #d4a5b9; font-weight: bold; font-size: 14px; }

    /* BOTÕES PEQUENOS E LINDOS (Rosa do Logo) */
    div.stButton > button {
        background-color: #d4a5b9 !important;
        color: white !important;
        border-radius: 20px !important;
        border: none !important;
        padding: 5px 20px !important;
        font-size: 13px !important;
        font-weight: bold !important;
        height: auto !important;
        width: auto !important;
        margin: 0 auto !important;
        display: block !important;
    }
    
    /* Ajuste dos campos de texto para não ficarem pretos */
    input, .stSelectbox, .stNumberInput {
        background-color: #ffffff !important;
        color: #5d4037 !important;
        border: 1px solid #fce4ec !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- TOPO (Igual ao seu Logo) ---
st.markdown("<h1>Doce Maju</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #5d4037; margin-top: -20px;'>BOLOS & DOCES | Feito com amor</p>", unsafe_allow_html=True)
st.write("---")

# --- LISTA DE DOCES (Para você colocar as fotos) ---
doces = {
    "Bombom de Uva": {"p": 11.0, "d": "Uva selecionada com creme de Ninho", "img": "https://via.placeholder.com/200x130?text=Sua+Foto+Aqui"},
    "Bolo de Pote": {"p": 8.0, "d": "Massa artesanal super molhadinha", "img": "https://via.placeholder.com/200x130?text=Sua+Foto+Aqui"},
    "Brigadeiro": {"p": 7.5, "d": "Chocolate belga 50% cacau", "img": "https://via.placeholder.com/200x130?text=Sua+Foto+Aqui"},
    "Sensação": {"p": 7.5, "d": "Morango fresco com ganache", "img": "https://via.placeholder.com/200x130?text=Sua+Foto+Aqui"}
}

# --- DIVISÃO: CARDÁPIO (Esquerda) e PEDIDO (Direita) ---
col_menu, col_pedido = st.columns([1.8, 1])

with col_menu:
    st.markdown("### 🌸 Cardápio")
    c1, c2 = st.columns(2)
    carrinho = {}

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
            
            # Seletor discreto
            qtd = st.number_input(f"Qtd {nome}", 0, 20, key=nome, label_visibility="collapsed")
            if qtd > 0:
                carrinho[nome] = {"q": qtd, "t": qtd * info['p']}

with col_pedido:
    st.markdown("### 🛒 Seu Pedido")
    if not carrinho:
        st.write("Escolha as delícias ao lado! ✨")
    else:
        total = 0
        for n, d in carrinho.items():
            st.write(f"💖 **{d['q']}x** {n}")
            total += d['t']
        
        st.divider()
        st.write(f"**Produtos:** R$ {total:.2f}")
        st.write("**Entrega:** R$ 3,00")
        st.markdown(f"## **Total: R$ {total + 3.0:.2f}**")
        
        # Dados de entrega simples e bonitos
        st.text_input("Seu Nome")
        st.text_input("Endereço")
        st.selectbox("Pagamento", ["Pix", "Dinheiro", "Cartão"])
        
        if st.button("Finalizar Pedido"):
            st.balloons()
            st.success("Pedido enviado para a Maju!")
