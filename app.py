import streamlit as st
import os
from backend.ai_engine import ProductFactoryAI

# Configuração da Página
st.set_page_config(
    page_title="Digital Product Factory",
    page_icon="🚀",
    layout="wide"
)

# Inicialização do Session State para persistência
if 'generated_content' not in st.session_state:
    st.session_state.generated_content = {
        'ebook': None,
        'copy': None,
        'emails': None,
        'prompts': None
    }
if 'has_generated' not in st.session_state:
    st.session_state.has_generated = False

# Título e Header
st.title("🚀 Digital Product Factory")
st.markdown("""
**Transforme ideias em Negócios Digitais completos em segundos.**
Esta ferramenta usa IA para gerar o Produto, a Copy, os E-mails e o Visual.
""")

# Sidebar para Configurações
with st.sidebar:
    st.header("⚙️ Configuração")
    
    api_key = st.text_input("Google Gemini API Key", type="password", help="Pegue sua chave no Google AI Studio")
    
    st.markdown("---")
    st.header("📝 Detalhes do Projeto")
    
    niche = st.text_input("Nicho de Mercado", placeholder="Ex: Adestramento de Cães")
    audience = st.text_input("Público-Alvo", placeholder="Ex: Donos de primeira viagem")
    tone = st.selectbox("Tom de Voz", ["Profissional e Autoritário", "Amigável e Motivacional", "Direto e 'Hard Sell'", "Empático e Emocional"])
    
    generate_btn = st.button("✨ Gerar Fábrica de Negócios", type="primary")

    st.markdown("---")
    st.info("💡 Dica: Seja específico no Nicho e Público para resultados melhores.")

# Lógica de Geração
if generate_btn:
    if not api_key:
        st.error("⚠️ Por favor, insira sua API Key do Google Gemini na barra lateral.")
    elif not niche or not audience:
        st.warning("⚠️ Por favor, preencha o Nicho e o Público-Alvo.")
    else:
        try:
            # Instancia a IA
            ai = ProductFactoryAI(api_key)
            
            # Limpa estado anterior
            st.session_state.has_generated = False
            
            with st.spinner("🤖 Ligando as turbinas... Gerando Estrutura do Produto..."):
                st.session_state.generated_content['ebook'] = ai.generate_ebook_structure(niche, audience, tone)
            
            # Fallback simples para título
            product_title = f"Guia Definitivo: {niche}"

            with st.spinner("✍️ Escrevendo a Carta de Vendas (Copywriting)..."):
                st.session_state.generated_content['copy'] = ai.generate_sales_page(niche, audience, product_title)
            
            with st.spinner("📧 Criando Sequência de E-mails..."):
                st.session_state.generated_content['emails'] = ai.generate_email_sequence(niche, product_title)
            
            with st.spinner("🎨 Projetando a Capa (Prompts)..."):
                st.session_state.generated_content['prompts'] = ai.generate_image_prompts(niche, audience, product_title)

            st.session_state.has_generated = True
            st.success("✅ Negócio Digital Gerado com Sucesso!")

        except Exception as e:
            st.error(f"Ocorreu um erro durante a geração: {str(e)}")

# Exibição dos Resultados (usando session_state para persistir após interações)
if st.session_state.has_generated:
    # Abas para exibição
    tab1, tab2, tab3, tab4 = st.tabs(["📚 Produto (Ebook)", "💰 Página de Vendas", "📧 E-mails", "🎨 Capa (Prompts)"])

    with tab1:
        st.subheader("Estrutura do Infoproduto")
        content = st.session_state.generated_content['ebook']
        st.markdown(content)
        st.download_button("📥 Baixar Estrutura", content, file_name="ebook_structure.md")

    with tab2:
        st.subheader("Copy para Landing Page")
        content = st.session_state.generated_content['copy']
        st.markdown(content)
        st.download_button("📥 Baixar Copy", content, file_name="sales_page.md")

    with tab3:
        st.subheader("Sequência de E-mails")
        content = st.session_state.generated_content['emails']
        st.markdown(content)
        st.download_button("📥 Baixar E-mails", content, file_name="email_sequence.md")

    with tab4:
        st.subheader("Prompts para Gerador de Imagem")
        content = st.session_state.generated_content['prompts']
        st.markdown(content)
        st.info("Copie os prompts em inglês e cole no Midjourney, Bing Image Creator ou DALL-E.")

elif not generate_btn: # Estado inicial (apenas se não acabou de clicar)
    # Estado inicial (Placeholder)
    st.info("👈 Preencha os dados na barra lateral e clique em 'Gerar' para começar.")
    
    # Exemplo visual do que será gerado
    st.markdown("### Exemplo do que você pode criar:")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Ebooks", value="∞")
    with col2:
        st.metric(label="Landing Pages", value="Alta Conversão")
    with col3:
        st.metric(label="Funis de E-mail", value="5 Dias")
    with col4:
        st.metric(label="Custo", value="R$ 0,00")
