import google.generativeai as genai
import os

class ProductFactoryAI:
    def __init__(self, api_key):
        self.api_key = api_key
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-1.0-pro')

    def _get_response(self, prompt):
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Erro ao gerar conteúdo: {str(e)}"

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
        Atue como um Copywriter de elite (nível Ogilvy ou Gary Halbert).
        Escreva o texto completo de uma Landing Page de Alta Conversão para o produto: '{product_title}'.
        Nicho: '{niche}'.
        Público: '{audience}'.

        Estrutura obrigatória da Copy:
        1. HEADLINE: Deve parar o scroll e chocar ou prometer algo incrível.
        2. SUBHEADLINE: Complementa a promessa.
        3. A HISTÓRIA/DOR: Descreva a situação atual de dor do leitor (Pacing and Leading).
        4. A SOLUÇÃO: Apresente o produto como a única solução viável.
        5. BENEFÍCIOS (Bullets): Lista de 5 a 7 benefícios claros (não características).
        6. PARA QUEM É: Qualifique o lead.
        7. OFERTA IRRESISTÍVEL: Preço (sugira um valor fictício ancorado), Bônus e Garantia.
        8. CTA (Call to Action): Frase de botão forte.

        Use gatilhos mentais de Urgência, Escassez e Autoridade. Formate em Markdown.
        """
        return self._get_response(prompt)

    def generate_email_sequence(self, niche, product_title):
        prompt = f"""
        Crie uma sequência de funil de vendas de 5 dias via E-mail Marketing para vender o produto '{product_title}' no nicho de '{niche}'.

        Estrutura dos E-mails:
        - Dia 1: Agradecimento pelo interesse + História de Origem (conexão).
        - Dia 2: Conteúdo de valor + Apresentação do Problema Oculto.
        - Dia 3: A Grande Revelação (Apresentação do Produto) + Prova Social (fictícia).
        - Dia 4: Quebra de Objeções (FAQ) + Benefícios Lógicos.
        - Dia 5: Última Chamada (Escassez Real/Urgência) - "Vai fechar/Preço vai subir".

        Para cada e-mail, inclua:
        - Assunto (Subject Line) altamente clicável.
        - Corpo do e-mail persuasivo.
        
        Separe os e-mails claramente.
        """
        return self._get_response(prompt)

    def generate_image_prompts(self, niche, audience, product_title):
        prompt = f"""
        Atue como um Engenheiro de Prompt especialista em Midjourney e DALL-E 3.
        Crie 3 opções de prompts detalhados para gerar uma CAPA DE EBOOK profissional para o produto: '{product_title}'.
        Nicho: '{niche}'.
        Público: '{audience}'.

        Os prompts devem incluir detalhes sobre:
        - Estilo artístico (ex: minimalista, 3D render, fotorealista, ilustração vetorial).
        - Elementos visuais centrais.
        - Cores predominantes (psicologia das cores para o nicho).
        - Iluminação e composição.
        - Aspect Ratio (--ar 2:3 para ebooks).

        Forneça os prompts em inglês (pois as IAs funcionam melhor em inglês), mas explique a ideia em português antes de cada um.
        """
        return self._get_response(prompt)
