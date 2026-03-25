import streamlit as st
import urllib.parse

# 1. CONFIGURAÇÃO
st.set_page_config(page_title="Doce Maju", layout="wide")

# Inicializando a "memória" do site
if 'carrinho' not in st.session_state:
    st.session_state.carrinho = {}
if 'pix' not in st.session_state:
    st.session_state.pix = "Chave não cadastrada"
if 'esgotados' not in st.session_state:
    st.session_state.esgotados = []

# 2. CABEÇALHO
col_l1, col_l2 = st.columns([1, 4])
with col_l1:
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
            
            # Verifica se está esgotado
            if doce['nome'] in st.session_state.esgotados:
                st.error("🚫 ESGOTADO")
            else:
                st.write(f"R$ {doce['preco']:.2f}")
                if st.button(f"Adicionar +", key=f"btn_{doce['nome']}"):
                    st.session_state.carrinho[doce['nome']] = st.session_state.carrinho.get(doce['nome'], 0) + 1
                    st.toast(f"{doce['nome']} no carrinho!")

st.write("---")

# 5. CARRINHO E FINALIZAÇÃO
if st.session_state.carrinho:
    st.header("🛒 Seu Pedido")
    total_doces = 0
    resumo_itens = ""
    
    for item, qtd in st.session_state.carrinho.items():
        preco_unit = next(d['preco'] for d in doces if d['nome'] == item)
        subtotal = preco_unit * qtd
        total_doces += subtotal
        st.write(f"**{qtd}x** {item} - R$ {subtotal:.2f}")
        resumo_itens += f"- {qtd}x {item}\n"

    entrega = st.radio("Entrega ou Retirada?", ["Entrega (R$ 3,00)", "Retirada (Grátis)"])
    taxa = 3.0 if "Entrega" in entrega else 0.0
    pagamento = st.selectbox("Pagamento", ["Pix", "Dinheiro"])
    
    total_final = total_doces + taxa
    st.write(f"### Total: R$ {total_final:.2f}")
    
    if pagamento == "Pix":
        st.warning(f"Chave PIX para pagamento: **{st.session_state.pix}**")

    # Botão WhatsApp
    msg = f"NOVO PEDIDO:\n{resumo_itens}Total: R$ {total_final:.2f}\nPagamento: {pagamento}\n{entrega}"
    link_wa = f"https://wa.me/5521999999999?text={urllib.parse.quote(msg)}"
    st.link_button("✅ ENVIAR PEDIDO", link_wa, use_container_width=True)

# ---------------------------------------------------------
# 6. ÁREA DA ADMINISTRAÇÃO (BEM ESCONDIDA NO FINAL)
# ---------------------------------------------------------
st.write("\n" * 20) # Empurra o botão para baixo para ninguém ver fácil
with st.expander(" "): # Expander sem nome para ficar invisível
    st.subheader("⚙️ Painel da Maju")
    senha = st.text_input("Senha de Acesso", type="password")
    
    if senha == "maju123": # Você pode mudar a senha aqui
        st.success("Acesso liberado!")
        
        # Mudar PIX
        nova_pix = st.text_input("Cadastrar Nova Chave PIX", value=st.session_state.pix)
        if st.button("Salvar Chave PIX"):
            st.session_state.pix = nova_pix
            st.rerun()
            
        # Marcar Esgotado
        st.write("---")
        st.write("Gerenciar Estoque:")
        for d in doces:
            check = st.checkbox(f"Esgotado: {d['nome']}", value=(d['nome'] in st.session_state.esgotados))
            if check and d['nome'] not in st.session_state.esgotados:
                st.session_state.esgotados.append(d['nome'])
            elif not check and d['nome'] in st.session_state.esgotados:
                st.session_state.esgotados.remove(d['nome'])
        
        if st.button("Atualizar Estoque"):
            st.rerun()
