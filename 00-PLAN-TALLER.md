# Taller: Seguridad en Agentes de IA — "Construye, Rompe, Repara"

**Formato:** Individual, cada quien en su laptop
**Modelo:** DeepSeek (`deepseek-chat`), una API key provista por el facilitador
**Entorno:** Google Colab (navegador, sin instalar nada, VM aislada y desechable)
**Nivel asumido:** principiante — todo pre-armado, los alumnos corren celdas y hacen cambios pequeños

> 📘 Este documento explica **el diseño y el porqué**. Para el **paso a paso de cómo dar el taller**
> (subir a GitHub, enlaces de Colab, guion bloque por bloque, errores comunes), usa
> **[GUIA-FACILITADOR.md](GUIA-FACILITADOR.md)**.

---

## 1. Idea central

Los alumnos viven el ciclo completo de seguridad de un agente de IA:

1. **Construyen** un agente que usa herramientas reales (leer archivos, correr comandos).
2. **Lo atacan** para ver cómo un agente con herramientas puede ser manipulado (inyección de prompts, fuga de datos, abuso de herramientas).
3. **Lo reparan** con defensas en código y comprueban que los mismos ataques ya no funcionan.

El mensaje que se llevan: *un agente no es un chatbot; es un chatbot con manos. Darle manos sin controles es el riesgo.*

---

## 2. Por qué estas decisiones técnicas

| Decisión | Razón |
|---|---|
| **Google Colab en vez de Docker** | Cero instalación. 30 laptops distintas = instalar Docker en vivo es ruleta rusa. Colab corre en el navegador; cada alumno obtiene una VM Linux aislada y **desechable**: el agente puede borrar archivos y correr comandos sin riesgo real. Si algo se rompe, "Reiniciar entorno" y listo. |
| **DeepSeek vía SDK de OpenAI** | DeepSeek es compatible con la API de OpenAI (`base_url=https://api.deepseek.com`). El mismo código sirve si cambias de proveedor. Soporta *function calling*, que es lo que hace que un agente use herramientas. |
| **Notebooks para seguir en clase** | Los alumnos no escriben el agente desde cero: corren celdas ya hechas y hacen cambios pequeños (prompts, configuraciones, reemplazar funciones). Siguen la notebook mientras tú avanzas en las diapos. |
| **Escenario realista** | El agente es un "asistente de oficina" que lee una carpeta de documentos. Uno trae instrucciones ocultas: es el caso real de *inyección indirecta* que sufren los agentes de producción hoy. |

### Sobre la API key
- Usamos **una sola key** para todo el grupo. Riesgos: *rate limit* y que quede expuesta en las notebooks.
- La key se pega en una celda (`os.environ['DEEPSEEK_API_KEY'] = '...'`) y **se rota/borra en el panel de DeepSeek al terminar** el taller. Es de bajo valor y la rotas el mismo día.
- Ten saldo suficiente: ~30 alumnos × varias llamadas = unos pocos dólares. DeepSeek es barato.

---

## 3. Los bloques (alto nivel)

> Tiempos y guion detallado en [GUIA-FACILITADOR.md](GUIA-FACILITADOR.md). Hay holgura: si vas rápido, sobra material.

- **Bloque 0 — Bienvenida y setup.** Quién eres, qué haremos, el entorno y cómo usar Colab. Todos llegan a "conexión funciona".
- **Bloque 1 — Construye** (`01_construye.ipynb`). Qué es un LLM y un agente, el ciclo, las herramientas; ponen el agente a trabajar y lo ven decidir y actuar solo.
- **Bloque 2 — Rompe** (`02_ataca.ipynb`). Equipo rojo: inyección directa, inyección indirecta (la estrella) y acción destructiva. Cada ataque se etiqueta con su entrada del **OWASP Top 10 para LLM**. Jailbreaks se cubren como cultura (solo en diapo).
- **Bloque 3 — Repara** (`03_repara.ipynb`). Equipo azul: 3 defensas en código (separar datos, control de acceso, mínimo privilegio + confirmación humana), re-lanzando los ataques para ver que ya fallan. Mensaje: **defensa en profundidad**.
- **Cierre.** Las 3 ideas que se llevan + recursos.

---

## 4. Materiales (estado)

- [x] **Notebook 1 – Construye** (`notebooks/01_construye.ipynb`)
- [x] **Notebook 2 – Ataca** (`notebooks/02_ataca.ipynb`)
- [x] **Notebook 3 – Repara** (`notebooks/03_repara.ipynb`)
- [x] **Motor del agente** (`agente/`) + **escenario** (`escenario/`, `ataques/`) + **soluciones** (`defensas/`)
- [x] **Diapositivas** (`slides/index.html` animado + `slides/taller-agentes.pptx`)
- [x] **Guía del facilitador** (`GUIA-FACILITADOR.md`)
- [x] **Subir el repo a GitHub** (público, `briancgx/taller-agentes`)

---

## 5. Riesgos logísticos y plan B

| Riesgo | Mitigación |
|---|---|
| WiFi del aula malo | Colab y DeepSeek son ligeros (texto). Pide que abran la notebook antes de empezar; ten la key lista. |
| Alumno sin cuenta Google | Colab la necesita. Avisa de antemano. Plan B: trabajar en pareja con quien sí tenga. |
| Rate limit de DeepSeek | Escalona: no todos corren el agente al mismo segundo. Ten saldo de sobra. |
| Van más lento | Puedes saltar el ataque 3 o acortar la parte de defensas; lo esencial son los ataques 1 y 2 y la defensa 1. |
| Van más rápido (tu caso) | Hay material extra de sobra para estirar el cierre. |
