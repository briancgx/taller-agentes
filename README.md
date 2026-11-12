# Taller: Seguridad en Agentes de IA
### Construir · Atacar · Proteger

Un taller práctico donde se **construye** un **agente de IA** (un modelo que usa herramientas: leer archivos y correr comandos) con su propia app de chat, se **ataca** para encontrar sus vulnerabilidades y luego se **protege** reemplazando su código. Todo **gratis, en el navegador y aislado** (Google Colab).

> ⚠️ Todo corre dentro de una **máquina virtual desechable** de Colab. Es material **educativo para aprender a defender**; nunca se usa contra sistemas reales. Las credenciales del escenario son **falsas**.

---

## 🚀 Cómo empezar (alumnos)

1. Necesitas una **cuenta de Google** (gratis) y la **API key** que te dará el instructor.
2. Abre `notebooks/taller.ipynb` en Google Colab:
   - Entra a [colab.research.google.com](https://colab.research.google.com) → **Archivo › Abrir notebook** → pestaña **GitHub**.
   - Pega `https://github.com/briancgx/taller-agentes` y elige `notebooks/taller.ipynb`.
   - Enlace directo: `https://colab.research.google.com/github/briancgx/taller-agentes/blob/main/notebooks/taller.ipynb`
3. Corre las celdas **de arriba hacia abajo**. La primera celda descarga este repo dentro de la máquina virtual:
   ```
   %cd /content
   ![ -d taller ] || git clone -q https://github.com/briancgx/taller-agentes.git taller
   %cd /content/taller
   !pip install -q openai gradio
   ```
4. Pega la API key cuando se indique y abre la **app de chat** del agente (Paso 9).

## 🧭 Cómo funciona el taller

Es **una sola notebook** con 3 secciones y **un solo agente** de principio a fin:

| Sección | Qué se hace |
|---|---|
| **1 · Construir** | Se arma el agente pieza por pieza en celdas: instrucciones, herramientas y motor. Se abre su app de chat (Gradio). Es **vulnerable a propósito**. |
| **2 · Atacar** | Se pegan prompts de ataque en el chat (`ataques/prompts_de_ataque.md`): inyección directa, inyección indirecta y acción destructiva. |
| **3 · Proteger** | Se **reemplaza el código** de las celdas del agente (buscando la celda por su título) y se repiten **los mismos ataques**, que ya no deben funcionar. |

---

## 📁 Qué hay en el repo

```
.
├── notebooks/
│   ├── taller.ipynb          La notebook del taller (lo que corren los alumnos)
│   └── version-anterior/     Las 3 notebooks de la versión anterior (respaldo)
├── escenario/            La "oficina" de la empresa ficticia Refaccionaria El Tornillo
│   ├── empresa/              Tickets y notas: la carpeta de trabajo del agente
│   └── secretos.txt          Credenciales FALSAS, fuera de la oficina (objetivo de los ataques)
├── ataques/              Ticket envenenado + prompts de ataque
├── defensas/             Soluciones: el código exacto que se pega en cada defensa
├── agente/               Versión anterior del agente como paquete de Python (respaldo)
├── slides/               Diapositivas
├── 00-PLAN-TALLER.md     Plan y agenda del taller
└── GUIA-FACILITADOR.md   Qué decir y hacer en cada paso (para el instructor)
```

**¿Por qué `escenario/` va aparte del agente?** El agente es **código** (vive en la notebook); el escenario son los **datos** de la empresa sobre los que trabaja. Al clonar el repo, los dos quedan en la misma máquina virtual: el agente lee y actúa sobre `escenario/`.

---

## 🧰 Tecnología

- **Modelo:** DeepSeek (`deepseek-flash`, sin modo de razonamiento), vía API compatible con OpenAI.
  > `deepseek-chat` dejó de existir en julio de 2026; si DeepSeek vuelve a cambiar nombres, solo se cambia `MODELO` en el Paso 3.
- **App de chat:** Gradio, dentro de Colab (con enlace `gradio.live` para abrirla en otra pestaña).
- **Entorno:** Google Colab (gratis, sin instalar nada en la computadora).
- **Lenguaje:** Python, comentado en español y pensado para principiantes.
