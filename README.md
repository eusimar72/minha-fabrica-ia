# Digital Product Factory (Powered by Gemini Pro)

Uma ferramenta "All-in-One" para criar Infoprodutos completos usando Inteligência Artificial. Este aplicativo gera não apenas o conteúdo do produto, mas todo o ecossistema de vendas necessário para monetizá-lo.

## O que ele gera?

1.  **O Infoproduto (Ebook):** Título chamativo, sumário estruturado e conteúdo dos capítulos.
2.  **Página de Vendas (Landing Page):** Copywriting persuasivo focado em conversão.
3.  **Sequência de E-mails:** 5 e-mails prontos para funil de vendas (Aquecimento, Oferta, Escassez).
4.  **Visual (Capa):** Prompts otimizados para você gerar a capa em IAs de imagem (Midjourney, Bing, DALL-E).

## Pré-requisitos

1.  Python 3.8 ou superior instalado.
2.  Uma API Key do Google Gemini (Google AI Studio).
    - Obtenha gratuitamente aqui: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

## Instalação

1.  Clone este repositório ou baixe os arquivos.
2.  Navegue até a pasta do projeto:
    ```bash
    cd digital_product_factory
    ```
3.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Como usar

1.  Execute a aplicação:
    ```bash
    streamlit run app.py
    ```
2.  O navegador abrirá automaticamente (geralmente em `http://localhost:8501`).
3.  Na barra lateral:
    - Insira sua **Google API Key**.
    - Defina o **Nicho** (ex: "Emagrecimento", "Finanças", "Adestramento").
    - Defina o **Público-Alvo** (ex: "Mães pós-parto", "Jovens investidores").
    - Escolha o **Tom de Voz** (ex: "Motivacional", "Autoritário", "Amigável").
4.  Clique em **"Gerar Fábrica de Negócios"**.
5.  Navegue pelas abas para ver e copiar os resultados.

## Dicas de Monetização

- **Produtor:** Crie ebooks de nicho e venda na Kiwify/Hotmart.
- **Serviço:** Venda a "Criação de Produto Digital Express" para especialistas.
- **Lead Magnet:** Use o ebook gratuito para capturar leads e vender algo mais caro depois.
