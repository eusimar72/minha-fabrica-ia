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
        'channel_id': None, 'scripts': None, # Canal Dark (Novo)
        'video_package': None # Vídeo Único
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
    
    # Sub-menu (Radio horizontal ou selectbox)
   dark_mode = st.radio("Escolha o objetivo:", ["🆕 Criar Novo Canal (Identidade)", "🔥 Gerar Vídeo Viral Específico (ATUALIZADO)"], horizontal=True)

    if dark_mode == "🆕 Criar Novo Canal (Identidade)":
        col1, col2 = st.columns(2)
        with col1:
            dark_niche = st.text_input("Nicho do Canal", placeholder="Ex: Curiosidades Históricas")
        with col2:
            dark_tone = st.selectbox("Estilo", ["Narrativa Épica", "Rápido (TikTok)", "Misterioso"], key="dark_tone_id")
        
        if st.button("🚀 Gerar Identidade do Canal", type="primary"):
            if not api_key:
                st.error("Precisa da API Key!")
            else:
                try:
                    ai = ProductFactoryAI(api_key)
                    with st.spinner("🧠 Criando Identidade..."):
                        st.session_state.generated_content['channel_id'] = ai.generate_channel_identity(dark_niche)
                    with st.spinner("📜 Criando Primeiras Ideias..."):
                        st.session_state.generated_content['scripts'] = ai.generate_viral_scripts(dark_niche, dark_tone)
                    st.success("Canal Criado!")
                except Exception as e:
                    st.error(f"Erro: {e}")

        # Exibição Identidade
        if st.session_state.generated_content['channel_id']:
            t1, t2 = st.tabs(["🆔 Identidade & Branding", "💡 Ideias Iniciais"])
            with t1: st.markdown(st.session_state.generated_content['channel_id'])
            with t2: st.markdown(st.session_state.generated_content['scripts'])

     elif dark_mode == "🔥 Gerar Vídeo Viral Específico (ATUALIZADO)":
        st.info("Aqui você gera TUDO para um vídeo único: Roteiro, Tags, Descrição e Prompts Visuais.")
        col1, col2 = st.columns(2)
        with col1:
            video_topic = st.text_input("Tema do Vídeo", placeholder="Ex: O Burro que Salvou a Criança")
        with col2:
            video_tone = st.selectbox("Estilo", ["Emocionante", "Curioso/Fatos", "Terror/Suspense", "Motivacional"], key="dark_tone_vid")
            
        if st.button("🎥 Gerar Pacote de Vídeo Completo", type="primary"):
            if not api_key:
                st.error("Precisa da API Key!")
            else:
                try:
                    ai = ProductFactoryAI(api_key)
                    with st.spinner("🎬 Produzindo Roteiro, SEO e Prompts..."):
                        st.session_state.generated_content['video_package'] = ai.generate_single_video_package(video_topic, video_tone)
                    st.success("Vídeo Pronto para Produção!")
                except Exception as e:
                    st.error(f"Erro: {e}")

        # Exibição Vídeo Único
        if st.session_state.generated_content['video_package']:
            st.markdown("---")
            st.subheader("📦 Pacote de Produção do Vídeo")
            st.markdown(st.session_state.generated_content['video_package'])
            st.download_button("📥 Baixar Pacote Completo", st.session_state.generated_content['video_package'], file_name="video_package.md")
