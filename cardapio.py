import streamlit as st
import urllib.parse

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Doce Maju", page_icon="🧁", layout="wide")

# LINK DIRETO PARA AS FOTOS NO SEU GITHUB
LINK_FOTOS = "https://raw.githubusercontent.com/gabrielassisgomes015-byte/docemaju/main/"

# 2. ESTOQUE (Com os nomes das fotos do seu GitHub)
if 'estoque' not in st.session_state:
    st.session_state.estoque = {
        "Bombom Uva com ninho": {
            "preco": 11.0, 
            "desc": "Uvas frescas e creme Ninho", 
            "disponivel": True, 
            "imagem": "g.jpeg"
        },
        "Bombom Morango com ninho": {
            "preco": 11.0, 
            "desc": "Morango e o verdadeiro Ninho", 
            "disponivel": True, 
            "imagem": "p.jpeg"
        },
        "Bolo de Pote brigadeiro": {
            "preco": 8.0, 
            "desc": "Chocolate com morango", 
            "disponivel": True, 
            "imagem": "rango.png.jpeg"
        }
    }

# 3. MENU LATERAL
st.sidebar.title("Menu Doce Maju")
aba = st.sidebar.radio("Escolha a página:", ["🛒 Loja", "⚙️ Administração"])

# ---------------- PÁGINA DA LOJA (CLIENTE) ----------------
if aba == "🛒 Loja":
    st.markdown("<h1 style='text-align: center; color: #d4a5b9;'>Doce Maju</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'><b>🧁 FEITO COM AMOR 🧁</b></p>", unsafe_allow_html=True)
    st.divider()

    col_menu, col_linha, col_carrinho = st.columns([1.5, 0.1, 1])

    with col_menu:
        st.subheader("🌸 Nosso Cardápio")
        itens_escolhidos = {}
        
        c1, c2 = st.columns(2)
        for i, (nome, info) in enumerate(st.session_state.estoque.items()):
            if info["disponivel"]:
                lado = c1 if i % 2 == 0 else c2
                with lado:
                    with st.container(border=True):
                        # AQUI MOSTRA A IMAGEM (A linha que deu erro foi corrigida)
                        st.image(LINK_FOTOS + info["imagem"], use_container_width=True)
                            
                        st.write(f"**{nome}**")
                        st.write(f"R$ {info['preco']:.2f}")
                        qtd = st.number_input(f"Quantidade", 0, 20, key=f"venda_{nome}")
                        if qtd > 0:
                            itens_escolhidos[nome] = {"qtd": qtd, "subtotal": qtd * info['preco']}

    with col_linha:
        st.markdown('<div style="border-left: 2px solid #d4a5b9; height: 500px; margin: auto;"></div>', unsafe_allow_html=True)

    with col_carrinho:
        with st.container(border=True):
            st.subheader("🛒 Seu Pedido")
            
            if not itens_escolhidos:
                st.write("Seu carrinho está vazio. ✨")
            else:
                soma_produtos = 0
                texto_whatsapp = ""
                for nome, dados in itens_escolhidos.items():
                    st.write(f"✅ {dados['qtd']}x {nome} - R$ {dados['subtotal']:.2f}")
                    soma_produtos += dados['subtotal']
                    texto_whatsapp += f"- {dados['qtd']}x {nome}\n"
                
                st.divider()
                entrega = st.radio("Como deseja receber?", ["Retirar no Local (Grátis)", "Entrega (Taxa R$ 3,00)"])
                valor_taxa = 3.0 if "Entrega" in entrega else 0.0
                total_geral = soma_produtos + valor_taxa
                
                st.markdown(f"### Total: R$ {total_geral:.2f}")
                
                nome_cli = st.text_input("Seu Nome")
                pagamento = st.selectbox("Forma de Pagamento", ["Pix", "Dinheiro", "Cartão"])
                
                if pagamento == "Pix":
                    st.info("Chave Pix: COLOQUE_AQUI")

                if st.button("🚀 FINALIZAR NO WHATSAPP", use_container_width=True):
                    if nome_cli:
                        msg = f"*Pedido Doce Maju*\n*Cliente:* {nome_cli}\n*Tipo:* {entrega}\n\n*Itens:*\n{texto_whatsapp}\n*Total:* R$ {total_geral:.2f}\n*Pagamento:* {pagamento}"
                        # COLOQUE O NÚMERO DA SUA IRMÃ ABAIXO
                        link = f"https://wa.me/5521999999999?text={urllib.parse.quote(msg)}"
                        st.balloons()
                        st.markdown(f'<a href="{link}" target="_blank" style="text-decoration:none;"><div style="background-color:#25d366;color:white;text-align:center;padding:15px;border-radius:10px;font-weight:bold;">ENVIAR NO WHATSAPP</div></a>', unsafe_allow_html=True)
                    else:
                        st.error("Digite seu nome!")

# ---------------- PÁGINA DE ADMINISTRAÇÃO ----------------
else:
    st.title("⚙️ Painel da Maju")
    senha = st.text_input("Senha:", type="password")
    if senha == "1234":
        st.subheader("O que tem hoje?")
        for nome in st.session_state.estoque.keys():
            st.session_state.estoque[nome]["disponivel"] = st.checkbox(f"Tem {nome}?", value=st.session_state.estoque[nome]["disponivel"])
        st.success("Atualizado!")
