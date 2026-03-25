# Descrição

Este repositório contém uma adaptação em português do curso "ChatGPT Prompt Engineering for Developers" da DeepLearning.AI, focado em práticas de engenharia de prompts para aplicações com modelos de linguagem. Os notebooks apresentam exemplos práticos de como resumir, inferir, transformar e expandir textos, além de construir chatbots utilizando o Gemini, em vez do OpenAI.

## Pré-requisitos

Os notebooks desse repositório foram testados com os seguintes softwares:

- Python 3.12.3 ou superior
- VSCode (Visual Studio Code)
- Extensão Jupyter para VSCode
- Pacote `google-genai` instalado (substitui OpenAI)
- Pacote `openai` instalado (usado no chatbot)
- Git para gerenciar o repositório

## Passo-a-passo para execução local

1. **Clonar o repositório:**
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <PASTA_DO_REPOSITORIO>
   ```
2. **Criar e ativar um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. **Instalar dependências:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Abrir o VSCode e instalar a extensão Jupyter:**
   - Busque por "Jupyter" na aba de extensões e instale.
5. **Abrir e executar os notebooks:**
   - Abra os arquivos `.ipynb` no VSCode.
   - No canto superior direito do notebook, selecione como Kernel o Python do venv criado no Passo 2.
   - Execute célula por célula para testar os exemplos.

## Chatbot Revisa Master

O notebook `chatbot_revisa_master.ipynb` implementa um chatbot de atendimento ao cliente para a **Revisa Master**, aplicando as tecnicas de prompt engineering ensinadas nos notebooks do curso.

**Funcionalidades:**
- Qualificacao de leads frios vindos do Instagram
- Identificacao de etapa academica e necessidade do lead
- Direcionamento para agendamento via WhatsApp
- Extracao automatica de dados do lead em JSON

**Modelo:** OpenAI GPT (gpt-4o-mini). Requer a variavel `OPENAI_API_KEY` no arquivo `.env`.

## Agradecimentos

Este repositório é uma adaptação em português do curso [ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/) da DeepLearning.AI, originalmente ministrado por Isa Fulford (OpenAI) e Andrew Ng (DeepLearning.AI). O conteúdo foi adaptado para utilizar o Gemini como modelo de linguagem, em vez do OpenAI, visando democratizar o acesso e facilitar o uso em ambientes locais.

---

## Como citar

Para citar o curso de referência conforme a ABNT:

> DEEPLEARNING.AI. ChatGPT Prompt Engineering for Developers. Disponível em: <https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/>. Acesso em: 09 mar. 2026.

Para citar este repositório:

> VILLANI, Leonardo. ChatGPT Prompt Engineering for Developers: adaptação em português com Gemini. Disponível em: <https://github.com/villani/prompt-engineering-for-developers>. Acesso em: 09 mar. 2026.

