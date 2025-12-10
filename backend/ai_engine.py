import google.generativeai as genai
import os

class ProductFactoryAI:
    def __init__(self, api_key):
        self.api_key = api_key
        genai.configure(api_key=self.api_key)
        # Usando o alias que funcionou para você
        self.model = genai.GenerativeModel('gemini-flash-latest')

    def _get_response(self, prompt):
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Erro ao gerar conteúdo: {str(e)}"

    # --- MÓDULO EBOOK (Original) ---
    def generate_ebook_structure(self, niche, audience, tone):
        prompt = f"""
        Atue como um especialista em criação de infoprodutos best-sellers.
        Crie a estrutura completa de um Ebook sobre o nicho: '{niche}' para o público-alvo: '{audience}'.
        O tom de voz deve ser: '{tone}'.

        A saída deve conter:
        1. Um Título Principal Altamente Persuasivo e Viral.
        2. Um Subtítulo que prometa uma transformação.
        3. Uma lista de 5 Capítulos principais com seus respectivos sub-tópicos (bullets).
        4. Uma breve introdução (2 parágrafos) vendendo a ideia do livro.

        Formate a saída em Markdown claro.
        """
        return self._get_response(prompt)

    def generate_sales_page(self, niche, audience, product_title):
        prompt = f"""
        Atue como um Copywriter de elite.
        Escreva uma Landing Page de Alta Conversão para o produto: '{product_title}'.
        Nicho: '{niche}'. Público: '{audience}'.
        
        Estrutura: Headline Impactante, História/Dor, Solução, Benefícios, Oferta, CTA.
        Formate em Markdown.
        """
        return self._get_response(prompt)

    def generate_email_sequence(self, niche, product_title):
        prompt = f"""
        Crie uma sequência de funil de vendas de 5 dias para o produto '{product_title}' ({niche}).
        Dia 1: Conexão. Dia 2: Problema. Dia 3: Produto. Dia 4: Objeções. Dia 5: Escassez.
        """
        return self._get_response(prompt)

    def generate_image_prompts(self, niche, audience, product_title):
        prompt = f"""
        Crie 3 prompts detalhados (em inglês) para gerar uma CAPA DE EBOOK profissional para '{product_title}' ({niche}).
        Inclua estilo, cores e elementos.
        """
        return self._get_response(prompt)

    # --- NOVO MÓDULO CANAL DARK ---
    def generate_channel_identity(self, niche):
        prompt = f"""
        Atue como um estrategista de YouTube e TikTok.
        Crie a identidade completa para um CANAL DARK no nicho: '{niche}'.

        Saída Obrigatória:
        1. 5 Ideias de Nomes Únicos e Memoráveis.
        2. 3 Sub-nichos com alta demanda e pouca concorrência dentro desse tema.
        3. Descrição do Canal (Bio) otimizada para SEO e conversão.
        4. Prompt Detalhado (em inglês) para criar a LOGO do canal (Estilo, Ícone, Cores).
        5. Prompt Detalhado (em inglês) para criar o BANNER do canal.

        Formate em Markdown.
        """
        return self._get_response(prompt)

    def generate_viral_scripts(self, theme, tone):
        prompt = f"""
        Atue como um roteirista de TikTok/Reels viral.
        Crie 5 Roteiros de Vídeos Curtos (até 60s) sobre o tema: '{theme}'.
        Tom de voz: '{tone}'.

        Para CADA roteiro, siga esta estrutura EXATA:
        - Título do Vídeo (Gancho)
        - [0-3s] Gancho Visual: O que aparece na tela e o que é falado para prender a atenção.
        - [3-45s] Corpo: O conteúdo dividido em 3 cenas rápidas.
        - [45-60s] CTA: Chamada para ação (seguir, comentar ou clicar no link).
        - Sugestão de B-Roll (Imagens de fundo) para cada cena.
        - Sugestão de Prompt de Imagem (em inglês) para a Thumbnail ou cena principal.

        Separe bem os roteiros. Formate em Markdown.
        """
        return self._get_response(prompt)

    # --- NOVO MÓDULO VÍDEO ÚNICO (CONSISTÊNCIA VISUAL V2) ---
    def generate_single_video_package(self, video_topic, tone):
        prompt = f"""
        Atue como um Diretor de Cinema premiado, especialista em Continuidade Visual e Storytelling.
        Objetivo: Criar um pacote completo para um vídeo viral sobre: '{video_topic}'.
        Tom: '{tone}'.

        IMPORTANTE: O foco total é a CONSISTÊNCIA VISUAL.

        Siga esta estrutura rigorosamente:

        SEÇÃO 1: FICHA TÉCNICA (Visual Reference)
        - Defina o Personagem Principal (descreva roupas, cores, rosto, idade).
        - Defina o Cenário Principal (iluminação, época, clima, cores).
        - Defina o Estilo Artístico (ex: Cinematic, Pixar Style, Realistic 8k).

        SEÇÃO 2: ROTEIRO E DIREÇÃO
        - Título Viral.
        - Roteiro Cena-a-Cena (5 cenas chave).

        SEÇÃO 3: FÁBRICA VISUAL (PROMPTS DE CONTINUIDADE)
        - Gere 5 PROMPTS DE IMAGEM (Midjourney/Bing) em INGLÊS.
        
        ⚠️ REGRA DE OURO (CRUCIAL):
        NÃO USE PLACEHOLDERS COMO '[PERSONAGEM_MAYA]' OU '[CENÁRIO]'.
        VOCÊ DEVE ESCREVER A DESCRIÇÃO FÍSICA COMPLETA EM CADA PROMPT, REPETINDO TUDO.
        
        Exemplo ERRADO: "[PERSONAGEM_MAYA] is running in [CENÁRIO]."
        Exemplo CERTO: "A small 6-year-old girl with blonde hair in a red dress (Maya) is running in a dark forest with blue fog."

        Repita a descrição completa do personagem (roupa, rosto, cor) e do cenário em CADA um dos 5 prompts.

        SEÇÃO 4: PROMPTS DE VÍDEO (Runway/Pika)
        - Gere 5 PROMPTS DE VÍDEO em INGLÊS.
        - Siga a mesma REGRA DE OURO: Descreva o personagem visualmente em cada linha, sem usar atalhos.

        SEÇÃO 5: METADADOS (SEO)
        - Descrição, Hashtags e Tags.

        Formate em Markdown.
        """
        return self._get_response(prompt)
