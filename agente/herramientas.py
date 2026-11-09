"""
herramientas.py — Las "manos" del agente.

Un agente = un modelo de lenguaje + herramientas que puede usar.
Aquí definimos esas herramientas. Cada una es:
  (a) una función normal de Python, y
  (b) un "esquema" que le describe al modelo para qué sirve.

⚠️ IMPORTANTE: esta es la versión VULNERABLE (insegura) a propósito.
Ninguna herramienta tiene controles de seguridad. Así la atacaremos en el
Bloque 2. En el Bloque 3 vas a REEMPLAZAR estas funciones por versiones
seguras que tú mismo escribirás.
"""

import os
import subprocess
from agente import config


# ------------------------- utilidad disponible ----------------------
# Esta función de apoyo ya viene lista: te servirá en el Bloque 3 para
# comprobar si una ruta está dentro de la carpeta de trabajo del agente.
def dentro_de_carpeta(ruta):
    """Devuelve True si 'ruta' está dentro de config.CARPETA_TRABAJO."""
    base = os.path.abspath(config.CARPETA_TRABAJO)
    destino = os.path.abspath(ruta)
    return destino == base or destino.startswith(base + os.sep)


# ------------------- herramientas (versión vulnerable) --------------
def listar_archivos(carpeta="."):
    """Lista todos los archivos dentro de una carpeta (y subcarpetas)."""
    try:
        encontrados = []
        for raiz, _dirs, files in os.walk(carpeta):
            for f in files:
                encontrados.append(os.path.join(raiz, f))
        return "\n".join(encontrados) if encontrados else "(carpeta vacía)"
    except Exception as e:
        return f"ERROR: {e}"


def leer_archivo(ruta):
    """Lee y devuelve el contenido de un archivo de texto. (SIN controles)"""
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"ERROR: {e}"


def correr_comando(comando):
    """Ejecuta un comando en la terminal de Linux (VM de Colab). (SIN controles)"""
    try:
        r = subprocess.run(
            comando, shell=True, capture_output=True, text=True, timeout=20
        )
        return (r.stdout + r.stderr) or "(sin salida)"
    except Exception as e:
        return f"ERROR: {e}"


# ------------------- registro de herramientas -----------------------
# Nombres de todas las herramientas disponibles.
TODAS = ["listar_archivos", "leer_archivo", "correr_comando"]

# Esquemas: así es como el modelo "ve" cada herramienta.
ESQUEMAS = [
    {
        "type": "function",
        "function": {
            "name": "listar_archivos",
            "description": "Lista los archivos dentro de una carpeta (incluye subcarpetas).",
            "parameters": {
                "type": "object",
                "properties": {
                    "carpeta": {"type": "string", "description": "Ruta de la carpeta a listar."}
                },
                "required": ["carpeta"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "leer_archivo",
            "description": "Lee el contenido de un archivo de texto.",
            "parameters": {
                "type": "object",
                "properties": {
                    "ruta": {"type": "string", "description": "Ruta del archivo a leer."}
                },
                "required": ["ruta"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "correr_comando",
            "description": "Ejecuta un comando en la terminal de Linux y devuelve su salida.",
            "parameters": {
                "type": "object",
                "properties": {
                    "comando": {"type": "string", "description": "Comando de shell a ejecutar."}
                },
                "required": ["comando"],
            },
        },
    },
]
