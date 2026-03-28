import streamlit as st
import sounddevice as sd
from scipy.io.wavfile import write
import whisper
from openai import OpenAI
from dotenv import load_dotenv
import os
import tempfile

# ==============================
# 🔐 CONFIG API KEY
# ==============================
load_dotenv()
client = OpenAI()

# ==============================
# 🧠 CARREGAR MODELO WHISPER
# ==============================
@st.cache_resource
def load_model():
    return whisper.load_model("base")

model = load_model()

# ==============================
# 🎤 GRAVAÇÃO DE ÁUDIO
# ==============================
def gravar_audio(duracao=5, fs=44100):
    st.info("🎤 Gravando áudio...")

    audio = sd.rec(int(duracao * fs), samplerate=fs, channels=1)
    sd.wait()

    file_name = "recording.wav"  # ✔️ arquivo fixo (mais seguro no Windows)
    write(file_name, fs, audio)

    return file_name

# ==============================
# 🧠 TRANSCRIÇÃO
# ==============================
def transcrever(audio_file):
    result = model.transcribe(audio_file, language="pt")
    return result["text"]

# ==============================
# 🤖 IA
# ==============================
def responder(texto):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": texto}
        ]
    )
    return response.choices[0].message.content


# ==============================
# 🎨 INTERFACE
# ==============================
st.set_page_config(page_title="Assistente de Voz IA", layout="centered")

st.title("🎤 Assistente de Voz com IA")
st.write("Clique no botão e fale...")

# Histórico
if "chat" not in st.session_state:
    st.session_state.chat = []

# Botão de gravação
if st.button("🎤 Gravar voz"):
    try:
        audio_file = gravar_audio(5)
        texto = transcrever(audio_file)

        resposta = responder(texto)

        st.session_state.chat.append(("Você", texto))
        st.session_state.chat.append(("IA", resposta))

    except Exception as e:
        st.error(f"Erro: {e}")

# Exibir chat
st.divider()

for autor, msg in st.session_state.chat:
    if autor == "Você":
        st.markdown(f"🧑 **Você:** {msg}")
    else:
        st.markdown(f"🤖 **IA:** {msg}")