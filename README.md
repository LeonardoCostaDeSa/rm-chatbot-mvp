## Chatbot Revisa Master

O notebook `chatbot_revisa_master.ipynb` implementa um chatbot de atendimento ao cliente para a **Revisa Master**, aplicando as tecnicas de prompt engineering ensinadas nos notebooks do curso.

**Demo ao vivo:** [https://rm-chatbot-mvp-fofirvgizoxu6vfrufzd2z.streamlit.app/](https://rm-chatbot-mvp-fofirvgizoxu6vfrufzd2z.streamlit.app/)

**Funcionalidades:**
- Qualificacao de leads frios vindos do Instagram
- Identificacao de etapa academica e necessidade do lead
- Direcionamento para agendamento via WhatsApp
- Extracao automatica de dados do lead em JSON

**Modelo:** Google Gemini 2.0 Flash (gratuito). Requer a variavel `GOOGLE_API_KEY` no arquivo `.env`.
