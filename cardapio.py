import streamlit as st
from datetime import datetime

# 1. Configuração da Página
st.set_page_config(
    page_title="Doce Maju - Cardápio Online", 
    page_icon="🧁", 
    layout="wide", # Usamos wide para ter os dois lados (esquerda e direita)
    initial_sidebar_state="collapsed"
)

# 2. Estilo Visual (Baseado no seu Logo: Rosa, Lilás e Marrom)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stApp { background-color: #fdfafb; }
    
    /* Estilo dos Títulos */
    .titulo-maju {
        color: #d4a5b9; 
        font-family: 'Times New Roman', serif; 
        font-size: 40px; 
        font-weight: bold;
        margin-bottom: 0px;
    }
    .subtitulo {
        color: #5d4037;
        font-size: 14px;
        letter-spacing: 2px;
        margin-bottom: 20px;
    }

    /* Card de Produto (Lado Esquerdo) */
    .produto-card {
        background-color: white;
        padding: 15px;
        border-radius: 12px;
        border-left: 5px solid #d4a5b9;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.02);
        margin-bottom: 10px;
    }

    /* Coluna do Pedido (Lado Direito) */
    .coluna-pedido {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #fce4ec;
        position: sticky;
        top: 10px;
    }

    /* Botão Finalizar */
    .stButton>button {
        background-color: #d4a5b9 !important;
        color: white !important;
        border-radius: 10px !important;
        border: none !important;
        width: 100%;
        font-weight: bold;
        height: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Dados dos Doces
if 'estoque' not in st.session_state:
    st.session_state.estoque = {
        "Bombom de Uva": 11.0,
        "Bombom de Morango": 11.0,
        "Bolo de Brigadeiro": 7.5,
        "Bolo de Brigadeiro com Morango": 7.5,
        "Chocolate com Morango": 7.5
    }

# --- LAYOUT EM DUAS COLUNAS ---
col_cardapio, col_finalizar = st.columns([1.5, 1]) # Lado esquerdo maior que o direito

# --- LADO ESQUERDO: CARDÁPIO ---
with col_cardapio:
    st.markdown('<p class="titulo-maju">Doce Maju</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitulo">BOLOS & DOCES</p>', unsafe_allow_html=True)
    st.write("### 🍰 Escolha suas delícias:")
    
    carrinho = {}
    
    for nome, preco in st.session_state.estoque.items():
        st.markdown(f'''
            <div class="produto-card">
                <span style="color:#5d4037; font-weight:bold;">{nome}</span><br>
                <span style="color:#d4a5b9;">R$ {preco:.2f}</span>
            </div>
        ''', unsafe_allow_html=True)
        
        # Seletor de quantidade logo abaixo do card
        qtd = st.number_input(f"Qtd {nome}", min_value=0, max_value=20, key=f"v_{nome}")
        if qtd > 0:
            carrinho[nome] = {"qtd": qtd, "total": qtd * preco}
        st.write("")

# --- LADO DIREITO: FINALIZAR PEDIDO (O "CARRINHO") ---
with col_finalizar:
    st.markdown('<div class="coluna-pedido">', unsafe_allow_html=True)
    st.markdown("### 🛒 Seu Pedido")
    
    if not carrinho:
        st.info("Seu carrinho está vazio. Selecione os doces ao lado! ✨")
    else:
        # Lista o que a pessoa escolheu
        total_produtos = 0
        for item, info in carrinho.items():
            st.write(f"**{info['qtd']}x** {item} - R$ {info['total']:.2f}")
            total_produtos += info['total']
        
        st.divider()
        
        # Campos de Informação
        st.markdown("**📍 Dados para Entrega:**")
        nome_cliente = st.text_input("Seu Nome")
        endereco = st.text_input("Endereço (Rua, Nº, Bairro)")
        forma_pagamento = st.selectbox("Como deseja pagar?", ["Pix", "Dinheiro", "Cartão (Levar maquininha)"])
        
        taxa_entrega = 3.0
        total_geral = total_produtos + taxa_entrega
        
        st.markdown(f"**Produtos:** R$ {total_produtos:.2f}")
        st.markdown(f"**Entrega:** R$ {taxa_entrega:.2f}")
        st.markdown(f"## **Total: R$ {total_geral:.2f}**")
        
        if st.button("🚀 CONFIRMAR PEDIDO AGORA"):
            if nome_cliente and endereco:
                # Aqui você pode adicionar a lógica de salvar o pedido
                st.success(f"Prontinho, {nome_cliente}! Seu pedido foi enviado para a Maju.")
                st.balloons()
            else:
                st.error("Ops! Preencha seu nome e endereço para pedirmos.")
    
    st.markdown('</div>', unsafe_allow_html=True)
