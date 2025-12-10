import streamlit as st
import os
from backend.ai_engine import ProductFactoryAI

st.set_page_config(page_title="Digital Product Factory", page_icon="🚀", layout="wide")

if 'generated_content' not in st.session_state:
    st.session_state.generated_content = {'ebook': None, 'copy': None, 'emails': None, 'prompts': None}
if 'has_generated' not in st.session_state:
    st.session_state.has_generated = False

st.title("🚀 Digital Product Factory")
st.markdown("**Transforme ideias em Negócios Digitais completos em segundos.**")

with st.sidebar:
    st.header("⚙️ Configuração")
    api_key = st.text_input("Google Gemini API Key", type="password")
    st.markdown("---")
    st.header("📝 Detalhes do Projeto")
    niche = st.text_input("Nicho de Mercado", placeholder="Ex: Adestramento de Cães")
    audience = st.text_input("Público-Alvo", placeholder="Ex: Donos de primeira viagem")
    tone = st.selectbox("Tom de Voz", ["Profissional e Autoritário", "Amigável e Motivacional", "Direto e 'Hard Sell'", "Empático e Emocional"])
    generate_btn = st.button("✨ Gerar Fábrica de Negócios", type="primary")

if generate_btn:
    if not api_key:
        st.error("⚠️ Insira sua API Key do Google Gemini.")
    elif not niche or not audience:
        st.warning("⚠️ Preencha o Nicho e o Público-Alvo.")
    else:
        try:
            ai = ProductFactoryAI(api_key)
            st.session_state.has_generated = False
            
            with st.spinner("🤖 Gerando Estrutura do Produto (Gemini 2.0)..."):
                st.session_state.generated_content['ebook'] = ai.generate_ebook_structure(niche, audience, tone)
            
            product_title = f"Guia Definitivo: {niche}"

            with st.spinner("✍️ Escrevendo Copy..."):
                st.session_state.generated_content['copy'] = ai.generate_sales_page(niche, audience, product_title)
            
            with st.spinner("📧 Criando E-mails..."):
                st.session_state.generated_content['emails'] = ai.generate_email_sequence(niche, product_title)
            
            with st.spinner("🎨 Projetando Capa..."):
                st.session_state.generated_content['prompts'] = ai.generate_image_prompts(niche, audience, product_title)

            st.session_state.has_generated = True
            st.success("✅ Sucesso!")

        except Exception as e:
            st.error(f"Erro: {str(e)}")

if st.session_state.has_generated:
    tab1, tab2, tab3, tab4 = st.tabs(["📚 Produto", "💰 Vendas", "📧 E-mails", "🎨 Capa"])
    with tab1:
        st.markdown(st.session_state.generated_content['ebook'])
    with tab2:
        st.markdown(st.session_state.generated_content['copy'])
    with tab3:
        st.markdown(st.session_state.generated_content['emails'])
    with tab4:
        st.markdown(st.session_state.generated_content['prompts'])
