import google.generativeai as genai

class ProductFactoryAI:
    def __init__(self, api_key):
        self.api_key = api_key
        genai.configure(api_key=self.api_key)
        # AQUI ESTÁ A CORREÇÃO FINAL:
        self.model = genai.GenerativeModel('gemini-2.0-flash-exp') 

    def _get_response(self, prompt):
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Erro ao gerar conteúdo: {str(e)}"
    
    # ... (o resto das funções continua igual) ...
    def generate_ebook_structure(self, niche, audience, tone):
        prompt = f"Crie a estrutura de Ebook sobre '{niche}' para '{audience}'. Tom: '{tone}'. Título, Subtítulo, 5 Capítulos e Intro. Markdown."
        return self._get_response(prompt)

    def generate_sales_page(self, niche, audience, product_title):
        prompt = f"Landing Page de Alta Conversão para '{product_title}'. Nicho: '{niche}', Público: '{audience}'. Copy completa. Markdown."
        return self._get_response(prompt)

    def generate_email_sequence(self, niche, product_title):
        prompt = f"Sequência de 5 e-mails de vendas para '{product_title}' (Nicho: '{niche}'). Funil completo."
        return self._get_response(prompt)

    def generate_image_prompts(self, niche, audience, product_title):
        prompt = f"3 prompts para Midjourney/DALL-E criar capa de ebook para '{product_title}'. Nicho: '{niche}'. Inglês."
        return self._get_response(prompt)
