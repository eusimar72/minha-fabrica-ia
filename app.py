import streamlit as st
import os
from backend.ai_engine import ProductFactoryAI

# Configuração da Página
st.set_page_config(
    page_title="Digital Empire Factory",
    page_icon="👑",
    layout="wide"
)

# Inicialização do Session State
if 'generated_content' not in st.session_state:
    st.session_state.generated_content = {
        'ebook': None, 'copy': None, 'emails': None, 'prompts': None, # Ebook
        'channel_id': None, 'scripts': None # Canal Dark
    }

# Header Principal
st.title("👑 Digital Empire Factory")
st.markdown("### Construa seu Império Digital: Ebooks & Canais Dark")

# Sidebar - Configuração Global
with st.sidebar:
    st.header("🔑 Acesso")
    api_key = st.text_input("Google Gemini API Key", type="password")
    if not api_key:
        st.warning("Insira sua chave para começar!")
    st.markdown("---")
    
    # Seletor de Modo
    mode = st.radio("O que vamos criar hoje?", ["📘 Fábrica de Ebooks", "🎬 Fábrica de Canal Dark"])

# --- LÓGICA: FÁBRICA DE EBOOKS ---
if mode == "📘 Fábrica de Ebooks":
    st.header("📘 Criador de Infoprodutos")
    
    col1, col2 = st.columns(2)
    with col1:
        niche = st.text_input("Nicho (Ebook)", placeholder="Ex: Adestramento de Cães")
    with col2:
        audience = st.text_input("Público-Alvo", placeholder="Ex: Donos iniciantes")
    tone = st.selectbox("Tom de Voz", ["Profissional", "Motivacional", "Direto", "Emocional"], key="ebook_tone")
    
    if st.button("✨ Gerar Ebook Completo", type="primary"):
        if not api_key:
            st.error("Precisa da API Key!")
        else:
            try:
                ai = ProductFactoryAI(api_key)
                with st.spinner("📚 Criando Estrutura..."):
                    st.session_state.generated_content['ebook'] = ai.generate_ebook_structure(niche, audience, tone)
                
                title_placeholder = f"Guia: {niche}"
                with st.spinner("✍️ Escrevendo Copy..."):
                    st.session_state.generated_content['copy'] = ai.generate_sales_page(niche, audience, title_placeholder)
                with st.spinner("📧 Criando Funil de E-mails..."):
                    st.session_state.generated_content['emails'] = ai.generate_email_sequence(niche, title_placeholder)
                with st.spinner("🎨 Gerando Capas..."):
                    st.session_state.generated_content['prompts'] = ai.generate_image_prompts(niche, audience, title_placeholder)
                st.success("Sucesso!")
            except Exception as e:
                st.error(f"Erro: {e}")

    # Exibição Ebook
    if st.session_state.generated_content['ebook']:
        t1, t2, t3, t4 = st.tabs(["Estrutura", "Página de Vendas", "E-mails", "Capas"])
        with t1: st.markdown(st.session_state.generated_content['ebook'])
        with t2: st.markdown(st.session_state.generated_content['copy'])
        with t3: st.markdown(st.session_state.generated_content['emails'])
        with t4: st.markdown(st.session_state.generated_content['prompts'])

# --- LÓGICA: FÁBRICA DE CANAL DARK ---
elif mode == "🎬 Fábrica de Canal Dark":
    st.header("🎬 Criador de Canais Virais")
    
    col1, col2 = st.columns(2)
    with col1:
        dark_niche = st.text_input("Tema do Canal", placeholder="Ex: Curiosidades Históricas, Estoicismo, Crimes Reais")
    with col2:
        dark_tone = st.selectbox("Estilo do Vídeo", ["Narrativa Épica", "Rápido e Dinâmico (TikTok)", "Misterioso/Suspense", "Educativo"], key="dark_tone")
    
    if st.button("🎥 Gerar Identidade & Roteiros", type="primary"):
        if not api_key:
            st.error("Precisa da API Key!")
        else:
            try:
                ai = ProductFactoryAI(api_key)
                with st.spinner("🧠 Criando Identidade do Canal (Nomes, Bio, Logo)..."):
                    st.session_state.generated_content['channel_id'] = ai.generate_channel_identity(dark_niche)
                
                with st.spinner("✍️ Escrevendo 5 Roteiros Virais..."):
                    st.session_state.generated_content['scripts'] = ai.generate_viral_scripts(dark_niche, dark_tone)
                st.success("Canal Dark Planejado!")
            except Exception as e:
                st.error(f"Erro: {e}")

    # Exibição Canal Dark
    if st.session_state.generated_content['channel_id']:
        t1, t2 = st.tabs(["🆔 Identidade Visual & Branding", "📜 5 Roteiros Virais"])
        with t1: 
            st.subheader("Identidade do Canal")
            st.markdown(st.session_state.generated_content['channel_id'])
            st.info("Copie os prompts de Logo e Banner e use no Bing Image Creator.")
        with t2: 
            st.subheader("Roteiros de Vídeo")
            st.markdown(st.session_state.generated_content['scripts'])
