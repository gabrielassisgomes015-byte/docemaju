import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Doce Maju", page_icon="🧁", layout="wide")

# 2. O DESIGN (HTML/CSS) - Isso aqui controla as cores e tamanhos
st.markdown("""
    <style>
    /* Força o fundo branco e ignora o modo escuro do celular */
    .stApp { background-color: #ffffff !important; color: #5d4037 !important; }
    header, footer, #MainMenu {visibility: hidden;}

    /* Título Doce Maju */
    .titulo-maju {
        color: #d4a5b9; 
        font-family: 'cursive'; 
        font-size: 45px; 
        text-align: center; 
        margin-bottom: 0px;
        font-weight: bold;
    }
    
    .subtitulo {
        text-align: center;
        color: #5d4037;
        font-size: 14px;
        letter-spacing: 2px;
        margin-bottom: 30px;
    }

    /* CARD DO DOCE (Foto em cima, texto embaixo) */
    .card-doce {
        background: white;
        border-radius: 15px;
        border: 1px solid #fce4ec;
        margin-bottom: 10px;
        text-align: center;
        overflow: hidden;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    }
    
    .img-doce {
        width: 100%;
        height: 140px;
        object-fit: cover;
    }

    .info-container { padding: 10px; }
    .nome-doce { font-weight: bold; font-size: 16px; color: #5d4037; }
    .desc-doce { font-size: 12px; color: #888; margin: 5px 0; line-height: 1.2; }
    .preco-doce { color: #d4a5b9; font-weight: bold; }

    /* BOTÃO ROSA PEQUENO (Adeus botões pretos gigantes) */
    div.stButton > button {
        background-color: #d4a5b9 !important;
        color: white !important;
        border-radius: 20px !important;
        border: none !important;
        padding: 5px 20px !important;
        font-size: 14px !important;
        font-weight: bold !important;
        width: auto !important;
        display: block !important;
        margin: 0 auto !important;
    }

    /* Garante que as caixas de texto fiquem brancas */
    input { background-color: white !important; color: black !important; border: 1px solid #fce4ec !important; }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown('<p class="titulo-maju">Doce Maju</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitulo">BOLOS & DOCES • FEITO COM AMOR</p>', unsafe_allow_html=True)

# --- LISTA DE PRODUTOS ---
# Para colocar as fotos reais, é só trocar o link entre as aspas em "foto"
produtos = [
    {"nome": "Bombom de Uva", "preco": 11.0, "desc": "Uva fresca com creme de Ninho", "foto": "https://via.placeholder.com/300x140/fce4ec/d4a5b9?text=Foto+Doce"},
    {"nome": "Bolo de Pote", "preco": 8.0, "desc": "Massa molhadinha e recheio cremoso", "foto": "https://via.placeholder.com/300x140/fce4ec/d4a5b9?text=Foto+Doce"},
    {"nome": "Brigadeiro Gourmet", "preco": 7.5, "desc": "Chocolate 50% cacau e granulado belga", "foto": "https://via.placeholder.com/300x140/fce4ec/d4a5b9?text=Foto+Doce"},
    {"nome": "Chocolate c/ Morango", "preco": 7.5, "desc": "Sensação de morango e ganache", "foto": "https://via.placeholder.com/300x140/fce4ec/d4a5b9?text=Foto+Doce"}
]

# --- DIVISÃO EM DUAS COLUNAS ---
col_cardapio, col_carrinho = st.columns([1.8, 1])

with col_cardapio:
    st.markdown("### 🧁 Cardápio")
    c1, c2 = st.columns(2)
    carrinho_final = {}

    for i, p in enumerate(produtos):
        alvo = c1 if i % 2 == 0 else c2
        with alvo:
            # HTML do Card
            st.markdown(f"""
                <div class="card-doce">
                    <img src="{p['foto']}" class="img-doce">
                    <div class="info-container">
                        <div class="nome-doce">{p['nome']}</div>
                        <div class="desc-doce">{p['desc']}</div>
                        <div class="preco-doce">R$ {p['preco']:.2f}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Seletor de quantidade (Python)
            qtd = st.number_input(f"Qtd {p['nome']}", 0, 20, key=p['nome'], label_visibility="collapsed")
            if qtd > 0:
                carrinho_final[p['nome']] = {"qtd": qtd, "sub": qtd * p['preco']}
            st.write("")

with col_carrinho:
    st.markdown("<div style='background-color:#fff9fa; padding:20px; border-radius:15px; border
