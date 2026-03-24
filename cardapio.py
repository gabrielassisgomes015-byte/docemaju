import streamlit as st
import urllib.parse
from datetime import datetime

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Doce Maju - Loja", page_icon="🧁", layout="wide")

# TRUQUE PARA ESCONDER O MENU DE PÁGINAS DO CLIENTE
st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {display: none;}
        .main { background-color: #fffafb; }
    </style>
""", unsafe_allow_html=True)

# INICIALIZAÇÃO DO ESTOQUE (MEMÓRIA)
if 'estoque' not in st.session_state:
    st.session_state.estoque = {
        "Bombom Uva com ninho": {"preco": 11.0, "desc": "Uvas frescas e creme Ninho", "disponivel": True, "imagem": "g.jpeg"},
        "Bombom Morango com ninho": {"preco": 11.0, "desc": "Morango e o verdadeiro Ninho", "disponivel": True, "imagem": "p.jpeg"},
        "Bolo de Pote brigadeiro": {"preco": 7.50, "desc": "Chocolate com morango", "disponivel": True, "imagem": "rango.png.jpeg"}
    }
if 'pedidos_recebidos' not in st.session_state: st.session_state.pedidos_recebidos = []
if 'chave_pix' not in st.session_state: st.session_state.chave_pix = "Chave não cadastrada"

LINK_FOTOS = "https://raw.githubusercontent.com/gabrielassisgomes015-byte/docemaju/main/"

# --- INTERFACE DA LOJA ---
st.title("🧁 Doce Maju")
st.write("### Feito com amor para adoçar seu dia!")

col_loja, col_carrinho = st.columns([2, 1])

with col_loja:
    itens_selecionados = {}
    c1, c2 = st.columns(2)
    produtos_ativos = [p for p, v in st.session_state.estoque.items() if v["disponivel"]]
    
    for i, nome in enumerate(produtos_ativos):
        info = st.session_state.estoque[nome]
        target_col = c1 if i % 2 == 0 else c2
        with target_col:
            with st.container(border=True):
                st.image(LINK_FOTOS + info["imagem"], use_container_width=True)
                st.subheader(nome)
                st.write(f"R$ {info['preco']:.2f}")
                qtd = st.number_input(f"Quantidade", 0, 20, key=f"loja_{nome}")
                if qtd > 0:
                    itens_selecionados[nome] = {"qtd": qtd, "subtotal": qtd * info['preco']}

with col_carrinho:
    with st.container(border=True):
        st.header("🛒 Seu Pedido")
        if not itens_selecionados:
            st.write("Seu carrinho está vazio.")
        else:
            total = 0
            resumo = ""
            for n, d in itens_selecionados.items():
                st.write(f"{d['qtd']}x {n}")
                total += d['subtotal']
                resumo += f"{d['qtd']}x {n}; "
            
            st.divider()
            envio = st.selectbox("Entrega", ["Retirada (Grátis)", "Entrega (+ R$ 3,00)"])
            taxa = 3.0 if "Entrega" in envio else 0.0
            total_final = total + taxa
            
            if taxa > 0: endereco = st.text_input("Endereço completo:")
            else: endereco = "Retirada"
            
            pagamento = st.selectbox("Pagamento", ["Pix", "Cartão", "Dinheiro"])
            if pagamento == "Pix": st.warning(f"Chave Pix: {st.session_state.chave_pix}")
            
            nome_cli = st.text_input("Seu Nome:")
            st.subheader(f"Total: R$ {total_final:.2f}")

            if st.button("🚀 FINALIZAR"):
                if nome_cli:
                    # Salva para a Administração
                    st.session_state.pedidos_recebidos.append({
                        "Hora": datetime.now().strftime("%H:%M"), "Cliente": nome_cli,
                        "Pedido": resumo, "Total": total_final, "Pgto": pagamento, "Endereço": endereco
                    })
                    # Link WhatsApp
                    msg = f"*NOVO PEDIDO*\n*Cliente:* {nome_cli}\n*Itens:* {resumo}\n*Total:* R$ {total_final:.2f}\n*Pagamento:* {pagamento}"
                    st.link_button("AVISAR NO WHATSAPP", f"https://wa.me/5521999999999?text={urllib.parse.quote(msg)}")
                    st.balloons()
