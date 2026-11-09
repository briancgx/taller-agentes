# 🤖🔐 Taller: Seguridad en Agentes de IA
### Construye · Rompe · Repara

Un taller práctico donde **construimos** un **agente de IA** (un modelo que usa
herramientas: leer archivos y correr comandos), aprendemos a **atacarlo** para
encontrar sus vulnerabilidades, y luego lo **blindamos** con defensas reales.
Todo **gratis, en el navegador y aislado** (Google Colab).

> ⚠️ Todo corre dentro de una **máquina virtual desechable** de Colab. Es material
> **educativo para aprender a defender**; nunca se usa contra sistemas reales.

---

## 🚀 Cómo empezar (alumnos)

1. Necesitas una **cuenta de Google** (gratis) y la **API key** que te dará el instructor.
2. Abre las notebooks en Google Colab, **en orden**:
   - `notebooks/01_construye.ipynb` → construir el agente
   - `notebooks/02_ataca.ipynb` → atacarlo (equipo rojo)
   - `notebooks/03_repara.ipynb` → defenderlo (equipo azul)
3. En cada notebook, corre las celdas **de arriba hacia abajo**. Pega la API key cuando se indique.

**Para abrir una notebook en Colab:** entra a [colab.research.google.com](https://colab.research.google.com),
pestaña **GitHub**, pega `https://github.com/briancgx/taller-agentes` y elige la notebook.

---

## 📁 Qué hay en el repo

```
.
├── notebooks/        Las notebooks del taller (lo que corren los alumnos)
├── agente/           El motor del agente
│   ├── config.py         Conexión a DeepSeek y carpeta de trabajo
│   ├── herramientas.py   Las "manos" del agente (listar, leer, correr comando)
│   └── agente.py         El bucle que hace que el agente razone y actúe
├── escenario/        La "empresa" ficticia que el agente administra
│   ├── empresa/          Tickets y notas (datos legítimos)
│   └── secretos.txt      Credenciales FALSAS (el objetivo de los ataques)
├── ataques/          Material para el Bloque 2 (incluye un ticket "envenenado")
├── defensas/         Soluciones de referencia del Bloque 3
├── slides/           Diapositivas (HTML animado + .pptx)
├── 00-PLAN-TALLER.md Plan y agenda del taller
└── GUIA-FACILITADOR.md  Qué decir y hacer en cada paso (para el instructor)
```

---

## 🧰 Tecnología

- **Modelo:** DeepSeek (`deepseek-chat`), vía API compatible con OpenAI.
- **Entorno:** Google Colab (gratis, sin instalar nada).
- **Lenguaje:** Python. El código está comentado en español y pensado para principiantes.
