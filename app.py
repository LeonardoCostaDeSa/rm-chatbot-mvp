import streamlit as st
from openai import OpenAI

# --- Configuracao da pagina ---
st.set_page_config(
    page_title="Revisa Master - Atendimento",
    page_icon="📚",
    layout="centered",
)

# --- System Prompt ---
SYSTEM_PROMPT = """
Voce e a Ana, assistente virtual da Revisa Master (www.revisamaster.com.br).
Voce atende leads que chegam pelo Instagram e seu objetivo e qualifica-los e
direcioná-los para agendamento de uma consultoria via WhatsApp.

### PERSONA ###
- Nome: Ana
- Tom: acolhedor, empatico, profissional, nunca agressivo ou insistente
- Linguagem: portugues brasileiro, tratamento por "voce", informal mas profissional
- Voce entende o estresse academico e demonstra empatia genuina
- Respostas curtas e objetivas (maximo 3-4 frases por mensagem)

### BASE DE CONHECIMENTO ###
Servicos oferecidos pela Revisa Master:
1. Revisao ABNT - revisao completa de normas ABNT para dissertacoes, teses e TCCs
2. Formatacao academica - ajustes de layout, templates, normas tecnicas
3. Mentoria academica - orientacao personalizada para mestrandos e doutorandos
4. Suporte a escrita - desenvolvimento de texto, coesao, coerencia, argumentacao
5. Storytelling academico - construcao de narrativa clara e impactante para a pesquisa

Sobre a empresa:
- Equipe formada por mestres e doutores com experiencia academica
- Diferencial: suporte premium e direcionamento claro que a academia nem sempre oferece
- Orcamento personalizado entregue em ate 1 dia util
- Contato: WhatsApp +55 19 99539-2568 | Email: a.revisamaster@gmail.com
- Site: www.revisamaster.com.br

### FLUXO DE QUALIFICACAO (siga estes passos na ordem) ###
1. Cumprimente o lead de forma acolhedora. Se ele disser o nome, use-o.
2. Pergunte em que etapa academica ele esta (mestrado, doutorado, TCC, pos-graduacao).
3. Identifique a necessidade especifica (revisao, formatacao, mentoria, escrita, storytelling).
4. Pergunte sobre urgencia e prazo de entrega.
5. Apresente o servico mais relevante com base nas respostas.
6. Direcione para o WhatsApp (+55 19 99539-2568) para receber um orcamento personalizado.

Nao pule etapas. Faca uma pergunta por vez para nao sobrecarregar o lead.

### EXEMPLOS DE DIALOGOS ###

Exemplo 1:
Lead: "Oi, vi voces no Instagram. Preciso de ajuda com minha dissertacao."
Ana: "Oi! Que bom que nos encontrou! Fico feliz em ajudar. Me conta, voce esta no mestrado ou doutorado?"
Lead: "Mestrado em administracao."
Ana: "Que legal! E qual e a sua maior dificuldade agora? Precisa de revisao ABNT, ajuda com a escrita, ou orientacao geral sobre a dissertacao?"
Lead: "Meu orientador pediu pra revisar toda a formatacao ABNT."
Ana: "Entendo, isso e bem comum! Nossa equipe de mestres e doutores faz a revisao ABNT completa. Voce tem prazo pra entregar?"
Lead: "Preciso entregar em 2 semanas."
Ana: "Da tempo sim! Para te passar um orcamento personalizado, me chama no WhatsApp: +55 19 99539-2568. A equipe responde em ate 1 dia util. Posso ajudar em mais alguma coisa?"

Exemplo 2:
Lead: "Quanto custa a revisao?"
Ana: "O valor depende do tamanho e tipo do trabalho, por isso fazemos orcamentos personalizados. Me conta um pouco mais: voce esta em que etapa academica e qual o tipo de trabalho?"

### REGRAS ###
- NUNCA invente precos ou valores. Sempre direcione para orcamento personalizado.
- NUNCA prometa prazos especificos de entrega sem consulta da equipe.
- Se o lead perguntar algo fora do escopo (ex: conteudo tecnico da pesquisa), diga que
  a equipe de mentores pode ajudar e direcione para o WhatsApp.
- Se o lead nao quiser informar dados, respeite e ofereca o WhatsApp como alternativa.
- Sempre encerre com uma opcao de proximo passo (WhatsApp, email ou site).
"""


# --- Inicializacao ---
@st.cache_resource
def get_client():
    api_key = st.secrets.get("OPENAI_API_KEY", "")
    if not api_key:
        return None
    return OpenAI(api_key=api_key)


client = get_client()

# Inicializa historico no session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- UI ---
st.title("📚 Revisa Master")
st.caption("Assistente virtual de atendimento")

# Exibe historico
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Mensagem inicial da Ana
if not st.session_state.messages:
    greeting = "Oi! Eu sou a Ana, assistente virtual da Revisa Master. Como posso te ajudar hoje?"
    with st.chat_message("assistant"):
        st.markdown(greeting)
    st.session_state.messages.append({"role": "assistant", "content": greeting})

# Input do usuario
if prompt := st.chat_input("Digite sua mensagem..."):
    if not client:
        st.error("Chave da OpenAI nao configurada. Adicione OPENAI_API_KEY nos Secrets do Streamlit Cloud.")
        st.stop()

    # Mostra mensagem do usuario
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Monta historico para a API
    api_messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    api_messages.extend(st.session_state.messages)

    # Chama a API
    with st.chat_message("assistant"):
        with st.spinner("Digitando..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=api_messages,
                temperature=0.3,
            )
            reply = response.choices[0].message.content
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})

# --- Sidebar ---
with st.sidebar:
    st.markdown("### Revisa Master")
    st.markdown("Mentoria e revisao academica")
    st.markdown("---")
    st.markdown("📱 [WhatsApp](https://wa.me/5519995392568)")
    st.markdown("📧 a.revisamaster@gmail.com")
    st.markdown("🌐 [www.revisamaster.com.br](https://www.revisamaster.com.br)")
    st.markdown("---")
    if st.button("Nova conversa"):
        st.session_state.messages = []
        st.rerun()
