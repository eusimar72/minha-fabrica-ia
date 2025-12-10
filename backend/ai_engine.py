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
