import streamlit as st
import google.generativeai as genai

st.title("🕵️ Detetive de Modelos")

api_key = st.text_input("Cole sua API Key aqui:", type="password")

if st.button("Testar Conexão"):
    try:
        genai.configure(api_key=api_key)
        st.write("✅ Conexão feita! Buscando modelos disponíveis...")
        
        models = []
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                models.append(m.name)
        
        if models:
            st.success(f"Modelos encontrados: {models}")
        else:
            st.error("Nenhum modelo encontrado para essa chave! Verifique se sua conta tem permissão.")
            
    except Exception as e:
        st.error(f"Erro fatal: {str(e)}")
