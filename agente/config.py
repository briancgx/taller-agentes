"""
config.py — Configuración central del agente.

Aquí solo vive la conexión a DeepSeek y la "carpeta de trabajo" del agente.
Las defensas YA NO son interruptores: las vas a IMPLEMENTAR tú con código
en el Bloque 3. Aquí no hay nada mágico que encender.
"""

import os

# -------------------------------------------------------------------
#  Conexión al modelo (DeepSeek es compatible con la API de OpenAI)
# -------------------------------------------------------------------
# La API key se toma de una variable de entorno que fijamos en la notebook.
API_KEY = os.environ.get("DEEPSEEK_API_KEY", "PON_AQUI_TU_API_KEY")
BASE_URL = "https://api.deepseek.com"
MODELO = "deepseek-chat"   # deepseek-chat soporta uso de herramientas (function calling)

# La carpeta de trabajo "oficial" del agente (su oficina).
# OJO: el archivo escenario/secretos.txt está FUERA de esta carpeta.
# En el Bloque 3 usarás este dato para impedir que el agente salga de su oficina.
CARPETA_TRABAJO = "escenario/empresa"
