"""
DEFENSA 3 — Mínimo privilegio + aprobación humana. Cierra: el borrado destructivo (LLM06).

Se pega en la celda indicada de notebooks/taller.ipynb (reemplazando su código) y se corre con ▶.
"""

# ---- 3A · reemplaza la celda: # === CELDA: HERRAMIENTAS PERMITIDAS ===
# === CELDA: HERRAMIENTAS PERMITIDAS ===   (DEFENSA 3A)
# Para revisar tickets y notas NO hace falta la terminal: se la quitamos.
HERRAMIENTAS = ["listar_archivos", "leer_archivo"]
print("✅ Herramientas permitidas:", HERRAMIENTAS)


# ---- 3B · reemplaza otra vez la celda: # === CELDA: HERRAMIENTAS PERMITIDAS ===
# === CELDA: HERRAMIENTAS PERMITIDAS ===   (DEFENSA 3B)
HERRAMIENTAS = ["listar_archivos", "leer_archivo", "correr_comando"]
print("✅ Herramientas permitidas:", HERRAMIENTAS)

# ---- 3B · y reemplaza la celda: # === CELDA: HERRAMIENTA correr_comando ===
# === CELDA: HERRAMIENTA correr_comando ===   (DEFENSA 3B)
def correr_comando(comando):
    """Ya no ejecuta nada sola: deja el comando esperando a que un humano lo apruebe."""
    global COMANDO_PENDIENTE
    COMANDO_PENDIENTE = comando
    return ("COMANDO EN ESPERA: no se ejecutó. Muéstrale al usuario el comando exacto "
            "y dile que escriba 'aprobar' o 'rechazar'.")
