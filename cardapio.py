import streamlit as st
import urllib.parse # Serve para preparar o texto para o WhatsApp

# 1. Configuração da Página
st.set_page_config(page_title="Doce Maju", page_icon="🧁", layout="wide")

# --- COLOQUE O NÚMERO DA SUA IRMÃ AQUI (Com DDD e sem espaços) ---
NUMERO_WHATSAPP = "5521967690731" 

# Inicializando o estoque
if 'estoque' not in st.session_state:
    st.session_state.estoque = {
        "Bombom Uva com ninho": {"preco": 11.0, "desc": "Uvas frescas e creme Ninho", "disponivel": True},
        "Bombom Morango com ninho": {"preco": 11.0, "desc": "Morango e o verdadeiro Ninho", "disponivel": True},
        "Bolo de Pote brigadeiro": {"preco": 7.50, "desc": "Chocolate com morango", "disponivel": True}
    }

# NAVEGAÇÃO
st.sidebar.title("Menu")
pagina = st.sidebar.radio("Ir para:", ["Loja (Cliente)", "Administração"])

if pagina == "Loja (Cliente)":
    st.markdown("<h1 style='text-align: center; color: #d4a5b9;'>Doce Maju</h1>", unsafe_allow_html=True)
    st.divider()

    col_cardapio, col_linha, col_pedido = st.columns([1.5, 0.1, 1])

    with col_cardapio:
        st.subheader("🌸 Cardápio")
        carrinho = {}
        c1, c2 = st.columns(2)
        
        for i, (nome, dados) in enumerate(st.session_state.estoque.items()):
            if dados["disponivel"]:
                coluna = c1 if i % 2 == 0 else c2
                with coluna:
                    with st.container(border=True):
                        st.write(f"**{nome}**")
                        st.write(f"R$ {dados['preco']:.2f}")
                        qtd = st.number_input(f"Qtd", 0, 20, key=f"cli_{nome}")
                        if qtd > 0:
                            carrinho[nome] = {"qtd": qtd, "sub": qtd * dados['preco'], "preco_uni": dados['preco']}

    with col_linha:
        st.markdown('<div style="border-left: 2px solid #d4a5b9; height: 500px; margin: auto;"></div>', unsafe_allow_html=True)

    with col_pedido:
        with st.container(border=True):
            st.subheader("🛒 Seu Pedido")
            if not carrinho:
                st.write("Escolha uma doçura! ✨")
            else:
                resumo_txt = "" # Variável para guardar o texto do WhatsApp
                total_produtos = 0
                for nome, info in carrinho.items():
                    st.write(f"{info['qtd']}x {nome}")
                    resumo_txt += f"- {info['qtd']}x {nome} (R$ {info['sub']:.2f})\n"
                    total_produtos += info['sub']
                
                tipo_envio = st.radio("Como deseja receber?", ["Retirada (Grátis)", "Entrega (Taxa R$ 3,00)"])
                taxa = 3.0 if tipo_envio == "Entrega (Taxa R$ 3,00)" else 0.0
                total_final = total_produtos + taxa
                
                st.divider()
                st.subheader(f"Total: R$ {total_final:.2f}")

                nome_c = st.text_input("Seu Nome")
                end_c = st.text_input("Endereço (se for entrega)")
                pag_c = st.selectbox("Pagamento", ["Pix", "Dinheiro", "Cartão"])

                # Botão que gera a mensagem
                if st.button("🚀 ENVIAR PEDIDO PARA O WHATSAPP", use_container_width=True):
                    if nome_c:
                        # Criando o texto da mensagem
                        mensagem = f"*Novo Pedido - Doce Maju*\n\n"
                        mensagem += f"*Cliente:* {nome_c}\n"
                        mensagem += f"*Tipo:* {tipo_envio}\n"
                        if taxa > 0: mensagem += f"*Endereço:* {end_c}\n"
                        mensagem += f"\n*Itens:*\n{resumo_txt}"
                        mensagem += f"\n*Total:* R$ {total_final:.2f}\n"
                        mensagem += f"*Pagamento:* {pag_c}"
                        
                        # Codifica o texto para o link do navegador
                        texto_codificado = urllib.parse.quote(mensagem)
                        link_whatsapp = f"https://wa.me/{NUMERO_WHATSAPP}?text={texto_codificado}"
                        
                        st.balloons()
                        # Cria um link clicável que abre o zap
                        st.markdown(f"""
                            <a href="{link_whatsapp}" target="_blank">
                                <div style="text-align:center; background-color:#25d366; color:white; padding:15px; border-radius:10px; font-weight:bold; text-decoration:none;">
                                    CLIQUE AQUI PARA ABRIR O WHATSAPP E FINALIZAR
                                </div>
                            </a>
                        """, unsafe_allow_html=True)
                    else:
                        st.error("Por favor, preencha seu nome!")

# ---------------- ADMINISTRAÇÃO ----------------
else:
    st.title("⚙️ Painel da Maju")
    senha = st.text_input("Senha:", type="password")
    if senha == "1234":
        st.subheader("Gerenciar Disponibilidade")
        for nome in st.session_state.estoque.keys():
            st.session_state.estoque[nome]["disponivel"] = st.checkbox(f"{nome}", value=st.session_state.estoque[nome]["disponivel"])
