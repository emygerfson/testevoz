# 🎤 Assistente de Voz com IA

Aplicação web que grava sua voz, transcreve com **Whisper** (OpenAI) e responde usando o **GPT-4o-mini**.

## 🚀 Como usar

### 1. Pré-requisitos
- Python 3.9+
- Chave de API da OpenAI

### 2. Instalação

```bash
# Clone o repositório
git clone https://github.com/emygerfson/testevoz.git
cd testevoz

# Instale as dependências
pip install -r requirements.txt
```

### 3. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
OPENAI_API_KEY="sua-chave-aqui"
```

### 4. Executar

```bash
streamlit run app.py
```

## 🛠️ Tecnologias

| Tecnologia | Uso |
|---|---|
| [Streamlit](https://streamlit.io) | Interface web |
| [Whisper](https://github.com/openai/whisper) | Transcrição de voz |
| [OpenAI GPT-4o-mini](https://platform.openai.com) | Respostas da IA |
| [SoundDevice](https://python-sounddevice.readthedocs.io) | Gravação de áudio |

## 📁 Estrutura

```
├── app.py           # Código principal
├── requirements.txt # Dependências
├── .env             # Variáveis de ambiente (não versionado)
└── .gitignore
```
