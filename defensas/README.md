# Soluciones de las defensas (Sección 3)

Cada archivo trae el código **exacto** que se pega en la notebook `notebooks/taller.ipynb`.
Cada fragmento indica qué celda reemplaza (las celdas se identifican por su título `# === CELDA: ... ===`).

| Archivo | Defensa | Celda que reemplaza | Ataque que cierra |
|---|---|---|---|
| `defensa_1_separar_datos.py` | 1A instrucciones con reglas · 1B datos marcados | `INSTRUCCIONES` · `HERRAMIENTA leer_archivo` | Inyección directa e indirecta (LLM01) |
| `defensa_2_control_acceso.py` | Control de acceso | `HERRAMIENTA leer_archivo` | Lectura de `secretos.txt` |
| `defensa_3_minimo_privilegio.py` | 3A sin terminal · 3B aprobación humana | `HERRAMIENTAS PERMITIDAS` · `HERRAMIENTA correr_comando` | Borrado destructivo (LLM06) |

Después de pegar y correr la celda, se borra el chat y se repiten los mismos prompts de `ataques/prompts_de_ataque.md`.

> Ninguna defensa sola basta: la seguridad real es **por capas** (defensa en profundidad).
