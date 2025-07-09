import streamlit as st
from datetime import datetime, timedelta

# Configurações do app
st.set_page_config(page_title="Escala da Vovó", layout="centered")

st.title("📅 Escala de Revezamento – Fim de Semana")
st.markdown("Quem cuida da Vovó nesse fim de semana:")

# Responsáveis na ordem da escala
familia = ["Oscar", "José", "Carlos", "Maria", "Ana"]
hoje = datetime.now()
inicio_fds = hoje + timedelta(days=(5 - hoje.weekday()) % 7)
fim_fds = inicio_fds + timedelta(days=1)

# Descobre qual responsável pelo índice da semana
index_responsavel = ((inicio_fds - datetime(2024, 12, 28)).days // 7) % len(familia)
responsavel = familia[index_responsavel]

st.success(f"🗓️ {inicio_fds.strftime('%d/%m/%Y')} e {fim_fds.strftime('%d/%m/%Y')} – **{responsavel}**")

# Se desejar trocar o fim de semana
st.markdown("---")
st.subheader("Deseja propor uma troca?")
nome = st.selectbox("Quem está propondo a troca?", familia)
novo_responsavel = st.selectbox("Deseja trocar com quem?", [p for p in familia if p != nome])

if st.button("Gerar mensagem de troca"):
    mensagem = (
        f"📢 Olá família!\n\n"
        f"{nome} gostaria de trocar o fim de semana de cuidado da Vovó ("
        f"{inicio_fds.strftime('%d/%m')} e {fim_fds.strftime('%d/%m')}) com {novo_responsavel}.\n"
        f"Está tudo bem para vocês?\n\n🙏 Confirmem por aqui no grupo!"
    )
    st.text_area("Mensagem pronta para o WhatsApp:", mensagem, height=150)
    st.info("Copie e cole essa mensagem no grupo.")
