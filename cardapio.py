import streamlit as st
import urllib.parse

# 1. CONFIGURAÇÃO DA ABA (ÍCONE)
st.set_page_config(
    page_title="Doce Maju",
    page_icon="https://raw.githubusercontent.com/gabrielassisgomes015-byte/docemaju/main/logo.png.jpeg",
    layout="wide"
)

# Inicializando a memória do sistema
if 'carrinho' not in st.session_state:
    st.session_state.carrinho = {}
if 'pix' not in st.session_state:
    st.session_state.pix = "Chave não cadastrada"
if 'esgotados' not in st.session_state:
    st.session_state.esgotados = []

# Estilo visual
st.markdown("""
    <style>
    [data-testid="stImage"] { display: flex; justify-content: center; }
    .stButton button { width: 100%; border-radius: 10px; background-color: #f0f2f6; }
    </style>
    """, unsafe_allow_html=True)

# 2. CABEÇALHO COM LOGO
col_l, col_t = st.columns([1, 5])
with col_l:
    st.image("https://raw.githubusercontent.com/gabrielassisgomes015-byte/docemaju/main/logo.png.jpeg", width=120)
with col_t:
    st.title("Doce Maju - Cardápio")
    st.write("Escolha suas delícias abaixo!")

st.write("---")

# 3. LISTA DE DOCES
doces = [
    {"nome": "Bombom de Uva", "preco": 11.00, "imagem": "uva.png"},
    {"nome": "Bombom de Morango", "preco": 11.00, "imagem": "morango.png"},
    {"nome": "Bolo de Pote", "preco": 7.50, "imagem": "brigadeiro.png.jpeg"}
]

# 4. VITRINE DE PRODUTOS
cols = st.columns(4)
for i, doce in enumerate(doces):
    with cols[i % 4]:
        with st.container(border=True):
            link_foto = f"https://raw.githubusercontent.com/gabrielassisgomes015-byte/docemaju/main/{doce['imagem']}"
            st.image(link_foto, width=150)
            st.subheader(doce['nome'])
            
            if doce['nome'] in st.session_state.esgotados:
                st.error("🚫 ESGOTADO")
            else:
                st.write(f"**R$ {doce['preco']:.2f}**")
                if st.button(f"Adicionar +", key=f"add_{doce['nome']}"):
                    st.session_state.carrinho[doce['nome']] = st.session_state.carrinho.get(doce['nome'], 0) + 1
                    st.toast(f"{doce['nome']} adicionado!")

st.write("---")

# 5. SISTEMA DO CARRINHO (SOMA E FINALIZAÇÃO)
if st.session_state.carrinho:
    st.header("🛒 Seu Carrinho")
    total_doces = 0
    resumo_itens = ""
    
    for item, qtd in st.session_state.carrinho.items():
        preco_unit = next(d['preco'] for d in doces if d['nome'] == item)
        subtotal = preco_unit * qtd
        total_doces += subtotal
        st.write(f"**{qtd}x** {item} - R$ {subtotal:.2f}")
        resumo_itens += f"- {qtd}x {item}\n"

    st.write("---")
    
    # Opções de Entrega e Pagamento
    col_ent, col_pag = st.columns(2)
    with col_ent:
        entrega = st.radio("Como deseja receber?", ["Entrega (R$ 3,00)", "Retirada (Grátis)"])
    with col_pag:
        pagamento = st.selectbox("Forma de Pagamento:", ["Pix", "Dinheiro"])
    
    taxa_entrega = 3.0 if "Entrega" in entrega else 0.0
    total_final = total_doces + taxa_entrega
    
    st.write(f"## Total Geral: R$ {total_final:.2f}")
    
    if pagamento == "Pix":
        st.warning(f"Chave PIX: **{st.session_state.pix}**")

    # Botão WhatsApp
    msg = f"PEDIDO DOCE MAJU:\n{resumo_itens}------------------\nSubtotal: R$ {total_doces:.2f}\nEntrega: R$ {taxa_entrega:.2f}\nTOTAL: R$ {total_final:.2f}\nPagamento: {pagamento}\n{entrega}"
    link_wa = f"https://wa.me/5521999999999?text={urllib.parse.quote(msg)}"
    
    st.link_button("✅ FINALIZAR PEDIDO NO WHATSAPP", link_wa, use_container_width=True)

    if st.button("Limpar Carrinho"):
        st.session_state.carrinho = {}
        st.rerun()
else:
    st.info("O carrinho está vazio.")

# 6. PAINEL ADMIN (ESCONDIDO NO FINAL)
st.write("\n" * 30) 
with st.expander(" "):
    st.write("### Administração")
    senha = st.text_input("Senha", type="password")
    if senha == "maju123":
        st.session_state.pix = st.text_input("Cadastrar Chave PIX", value=st.session_state.pix)
        st.write("---")
        st.write("Controle de Estoque:")
        for d in doces:
            check = st.checkbox(f"Esgotado: {d['nome']}", value=(d['nome'] in st.session_state.esgotados))
            if check and d['nome'] not in st.session_state.esgotados:
                st.session_state.esgotados.append(d['nome'])
            elif not check and d['nome'] in st.session_state.esgotados:
                st.session_state.esgotados.remove(d['nome'])
        if st.button("Salvar Mudanças"):
            st.rerun()
