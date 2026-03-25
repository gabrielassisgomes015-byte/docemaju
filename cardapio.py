import streamlit as st
import urllib.parse

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Doce Maju", layout="wide")

# Inicializando o carrinho na memória do site
if 'carrinho' not in st.session_state:
    st.session_state.carrinho = {}

# 2. CABEÇALHO (LOGO E TÍTULO)
col_l1, col_l2 = st.columns([1, 4])
with col_l1:
    # Sua logo oficial aqui
    st.image("https://raw.githubusercontent.com/gabrielassisgomes015-byte/docemaju/main/logo.png.jpeg", width=100)
with col_l2:
    st.title("Doce Maju - Cardápio")

st.write("---")

# 3. LISTA DE PRODUTOS
doces = [
    {"nome": "Bombom de Uva", "preco": 11.00, "imagem": "uva.png"},
    {"nome": "Bombom de Morango", "preco": 11.00, "imagem": "morango.png"},
    {"nome": "Bolo de Pote", "preco": 7.50, "imagem": "brigadeiro.png.jpeg"}
]

# 4. EXIBIÇÃO DOS PRODUTOS
cols = st.columns(4)
for i, doce in enumerate(doces):
    with cols[i % 4]:
        with st.container(border=True):
            link_foto = f"https://raw.githubusercontent.com/gabrielassisgomes015-byte/docemaju/main/{doce['imagem']}"
            st.image(link_foto, width=150)
            st.subheader(doce['nome'])
            st.write(f"R$ {doce['preco']:.2f}")
            
            if st.button(f"Adicionar +", key=doce['nome']):
                nome = doce['nome']
                st.session_state.carrinho[nome] = st.session_state.carrinho.get(nome, 0) + 1
                st.toast(f"{nome} adicionado!")

st.write("---")

# 5. ÁREA DO CARRINHO (SOMA E OPÇÕES)
if st.session_state.carrinho:
    st.header("🛒 Seu Pedido")
    
    total_doces = 0
    resumo_texto = "PEDIDO DOCE MAJU:\n"
    
    for item, qtd in st.session_state.carrinho.items():
        # Busca o preço na lista original
        preco_unit = next(d['preco'] for d in doces if d['nome'] == item)
        subtotal = preco_unit * qtd
        total_doces += subtotal
        st.write(f"{qtd}x {item} - R$ {subtotal:.2f}")
        resumo_texto += f"- {qtd}x {item} (R$ {subtotal:.2f})\n"

    st.write("---")
    
    # Opções de Entrega
    tipo_entrega = st.radio("Como quer receber?", ["Entrega (R$ 3,00)", "Retirada (Grátis)"])
    taxa = 3.00 if "Entrega" in tipo_entrega else 0.00
    total_geral = total_doces + taxa
    
    # Opções de Pagamento
    pagamento = st.selectbox("Forma de Pagamento", ["Pix", "Dinheiro"])
    
    st.write(f"### Total Geral: R$ {total_geral:.2f}")
    
    # Botão para Limpar Carrinho
    if st.button("Esvaziar Carrinho"):
        st.session_state.carrinho = {}
        st.rerun()

    # 6. BOTÃO FINAL PARA O WHATSAPP
    resumo_final = (
        f"{resumo_texto}"
        f"------------------\n"
        f"Subtotal: R$ {total_doces:.2f}\n"
        f"Entrega: R$ {taxa:.2f}\n"
        f"TOTAL: R$ {total_geral:.2f}\n"
        f"Pagamento: {pagamento}\n"
        f"Tipo: {tipo_entrega}"
    )
    
    link_wa = f"https://wa.me/5521999999999?text={urllib.parse.quote(resumo_final)}"
    st.link_button("✅ FINALIZAR PEDIDO NO WHATSAPP", link_wa, use_container_width=True)
else:
    st.info("Seu carrinho está vazio. Adicione doces acima!")
