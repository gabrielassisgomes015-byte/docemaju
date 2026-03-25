import streamlit as st
import urllib.parse

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Doce Maju - Loja", page_icon="🧁", layout="wide")

# --- INICIALIZAÇÃO DO CARRINHO (A MEMÓRIA DO SITE) ---
if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []

# --- FUNÇÕES DO CARRINHO ---
def adicionar_ao_carrinho(nome, preco):
    st.session_state.carrinho.append({"nome": nome, "preco": preco})
    st.toast(f"✅ {nome} adicionado!")

def limpar_carrinho():
    st.session_state.carrinho = []

# --- INTERFACE: BARRA LATERAL (CARRINHO) ---
with st.sidebar:
    st.header("🛒 Seu Carrinho")
    if not st.session_state.carrinho:
        st.write("O carrinho está vazio.")
    else:
        total = 0
        resumo_pedido = "Olá Maju! Gostaria de fazer o seguinte pedido:\n\n"
        
        for item in st.session_state.carrinho:
            st.write(f"• {item['nome']} - R$ {item['preco']}")
            # Convertendo preço para somar (troca vírgula por ponto)
            total += float(item['preco'].replace(',', '.'))
            resumo_pedido += f"- {item['nome']} (R$ {item['preco']})\n"
        
        st.write("---")
        st.subheader(f"Total: R$ {total:.2f}".replace('.', ','))
        
        # Botão para Finalizar e ir para o WhatsApp
        resumo_pedido += f"\n*Total: R$ {total:.2f}*"
        numero_maju = "5521967690731" # <--- COLOQUE O NÚMERO DA SUA IRMÃ AQUI
        link_wa = f"https://wa.me/{numero_maju}?text={urllib.parse.quote(resumo_pedido)}"
        
        st.link_button("Finalizar Pedido (WhatsApp) ✅", link_wa, use_container_width=True)
        
        if st.button("Esvaziar Carrinho 🗑️"):
            limpar_carrinho()
            st.rerun()

# --- INTERFACE: CORPO DA LOJA ---
st.title("🧁 Doce Maju - Cardápio")
st.write("Escolha seus doces e clique em adicionar!")
st.write("---")

# LISTA DE DOCES
doces = [
    {"nome": "Bombom de Uva", "preco": "11,00", "imagem": "uva.png"},
    {"nome": "Bombom de Morango", "preco": "11,00", "imagem": "morango.png"},
    {"nome": "Bolo de Pote de Brigadeiro", "preco": "7,50", "imagem": "brigadeiro.png.jpeg"}
]

col1, col2 = st.columns(2)

for i, doce in enumerate(doces):
    target_col = col1 if i % 2 == 0 else col2
    
    with target_col:
        with st.container(border=True):
            link_foto = f"https://raw.githubusercontent.com/gabrielassisgomes015-byte/docemaju/main/{doce['imagem']}"
            
            st.image(link_foto, width=250)
            st.subheader(doce['nome'])
            st.write(f"**R$ {doce['preco']}**")
            
            # Botão que adiciona ao carrinho em vez de abrir link
            st.button(f"Adicionar {doce['nome']}", 
                      key=f"btn_{i}", 
                      on_click=adicionar_ao_carrinho, 
                      args=(doce['nome'], doce['preco']),
                      use_container_width=True)

st.write("---")
st.caption("Dica: O carrinho aparece na lateral (ou no topo no celular).")
