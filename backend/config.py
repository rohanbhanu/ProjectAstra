# ==========================
# Ollama Configuration
# ==========================

OLLAMA_URL = "http://localhost:11434/api/generate"

AVAILABLE_MODELS = {
    "fast": "tinyllama",
    "smart": "gemma3:1b"
}

MODEL_NAME = AVAILABLE_MODELS["smart"]


TEMPERATURE = 0.2
TOP_P = 0.9
NUM_PREDICT = 500

# ==========================
# Backend Configuration
# ==========================

REQUEST_TIMEOUT = 120

# ==========================
# Logging
# ==========================

LOG_LEVEL = "INFO"

# ==========================
# Streamlit
# ==========================

PAGE_TITLE = "Project Astra"
PAGE_ICON = "🤖"


STOP_WORDS =[
    "User:",
    "Assistant:",
    "Human:",
    "Project Astra:"]


