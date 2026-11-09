"""
DEFENSA 3 — Mínimo privilegio + confirmación humana.
Tapa: borrado destructivo (OWASP LLM06, Excessive Agency).

Dos técnicas:
  A) Mínimo privilegio: no darle al agente herramientas que no necesita.
     Se hace al llamar al agente, con el parámetro herramientas_permitidas.
  B) Confirmación humana: para comandos peligrosos, pedir aprobación con input().

Uso en la notebook:
    from agente import herramientas

    # A) Mínimo privilegio (ej.: resumir tickets NO necesita la terminal)
    ejecutar_agente(
        tarea,
        system_prompt=PROMPT_SEGURO,
        herramientas_permitidas=['listar_archivos', 'leer_archivo'],
    )

    # B) Confirmación humana antes de correr comandos
    herramientas.correr_comando = correr_comando
"""

import subprocess


def correr_comando(comando):
    # Confirmación humana antes de ejecutar algo en la terminal.
    permiso = input(f"[HUMANO] ¿Permitir correr: {comando}? (s/n) ")
    if permiso.strip().lower() != "s":
        return "COMANDO CANCELADO por el humano."
    r = subprocess.run(comando, shell=True, capture_output=True, text=True, timeout=20)
    return (r.stdout + r.stderr) or "(sin salida)"
