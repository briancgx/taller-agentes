# 🎓 Guía del facilitador — Taller de Seguridad en Agentes de IA

> Esta guía está escrita **para ti (Brian)**, asumiendo que **nunca has usado Google Colab**
> ni has subido un repo a GitHub. Sigue los pasos tal cual y vas sobrado. 💪

Índice:
1. [Qué es cada cosa (mapa mental)](#1-qué-es-cada-cosa)
2. [Antes del taller — preparación (una vez)](#2-antes-del-taller)
3. [El día del taller — montar a los alumnos](#3-el-día-del-taller)
4. [Guion bloque por bloque (qué decir y hacer)](#4-guion-bloque-por-bloque)
5. [Errores comunes y cómo salir del paso](#5-errores-comunes)
6. [Checklist de último minuto](#6-checklist)

---

## 1. Qué es cada cosa

- **Las diapositivas** (`slides/index.html`) → lo que **tú proyectas**. Es una página web animada.
- **Las notebooks** (`notebooks/*.ipynb`) → lo que **corren los alumnos** en su laptop, siguiéndote.
- **Google Colab** → una página de Google donde se abren las notebooks y se ejecutan **en la nube**
  (nadie instala nada; cada alumno tiene su propia "computadora desechable").
- **GitHub** → donde vive el repo. Colab abre las notebooks **directo desde GitHub**.
- **DeepSeek** → el modelo de IA (el "cerebro"). Se usa con una **API key** (una contraseña).

**El flujo es:** tú subes el repo a GitHub → los alumnos abren las notebooks en Colab desde GitHub →
pegan la API key que les das → corren las celdas mientras tú avanzas en las diapos.

---

## 2. Antes del taller

### 2.1 Proyectar las diapositivas

- En tu Mac, entra a la carpeta `slides/` y **haz doble clic en `index.html`**. Se abre en tu navegador.
- Controles: **flechas ← →** para avanzar/retroceder, tecla **F** para pantalla completa.
- Alternativa: `slides/taller-agentes.pptx` se abre en **Keynote/PowerPoint** (versión estática, sin animaciones).
- Consejo: usa el HTML para proyectar (se ve mejor y anima). Ten el pptx como respaldo.

### 2.2 Subir el repo a GitHub (lo haces tú)

El repo ya está listo en tu carpeta, pero todavía **no está en GitHub**. Para subirlo:

1. Entra a [github.com](https://github.com) con tu cuenta **briancgx** y crea un repositorio nuevo:
   **New repository** → nombre exacto: `taller-agentes` → **Public** → **Create repository**
   (no marques "Add a README", el repo ya trae uno).
2. En la Terminal de tu Mac, dentro de la carpeta del taller, corre:

```bash
cd ~/Documents/Taller-Misantla
git add .
git commit -m "Taller de seguridad en agentes de IA"
git branch -M main
git remote add origin https://github.com/briancgx/taller-agentes.git
git push -u origin main
```

3. Listo: recarga la página del repo en GitHub y deberías ver todos los archivos.

> ⚠️ El repo **debe ser público** para que los alumnos lo abran en Colab sin pedir permisos.
> (La carpeta `_ctf_privado/` queda fuera del repo gracias al `.gitignore`; ahí tienes tus notas privadas.)

### 2.3 Preparar los enlaces de Colab

Para cada notebook, el enlace "Abrir en Colab" tiene esta forma:

```
https://colab.research.google.com/github/briancgx/taller-agentes/blob/main/notebooks/01_construye.ipynb
```

Cambia el `01_construye` por `02_ataca` y `03_repara` para los otros dos. **Pruébalos tú antes**
(ábrelos, corre la primera celda) para confirmar que todo clona bien.

> Truco para compartir rápido: pon los 3 enlaces en un acortador o en una diapo/nota que les pegues en el chat.

### 2.4 La API key de DeepSeek

- Usaremos **una sola key para todo el grupo** (la tuya). Es lo más simple.
- Entra a tu panel de DeepSeek, asegúrate de tener **saldo** (unos pocos dólares bastan para ~30 alumnos).
- Copia la key; se la vas a dictar/pegar a los alumnos en el Bloque 0.
- 🔒 **Al terminar el taller, bórrala/rótala** en el panel de DeepSeek. Así, aunque haya quedado
  pegada en las notebooks de alguien, deja de servir.

---

## 3. El día del taller

Montaje de cada alumno (toma ~5 min, hazlo con ellos en el Bloque 0):

1. Abren el **enlace de Colab de la Notebook 1** (tú lo compartes).
2. Arriba a la izquierda, **"Copiar en Drive"** (o simplemente empezar a correr celdas — Colab les
   pedirá permiso de ejecución, que acepten).
3. Corren la **Celda 1** (prepara el entorno: clona el repo e instala la librería). Tarda ~20 s.
4. En la **celda de la API key**, reemplazan `PEGA_AQUI_LA_API_KEY` por la key que les diste.
5. Corren la **celda de prueba**: si ven "Hola, mi conexión funciona" → ✅ listos.

> Pídeles que corran **de arriba hacia abajo** y que no se salten celdas.

---

## 4. Guion bloque por bloque

> Tiempos aproximados y con holgura. Tú sueles ir rápido; si sobra, hay material extra para estirar el cierre.

### Bloque 0 · Bienvenida y setup
- **Diapos:** portada → ¿Quién soy? → Lo que vamos a hacer → El entorno → **Cómo usar Google Colab**.
- **Haz:** preséntate, explica el arco (crear → hackear → proteger) y que todo es en un entorno
  desechable. Monta a los alumnos (sección 3). Que todos lleguen a "conexión funciona".
- **Entregable:** todos con la Notebook 1 abierta y la conexión verde.

### Bloque 1 · Construye el agente 🛠️ (verde)
- **Diapos:** ¿Qué es un LLM? → Por dentro (Transformer) → De un LLM a un agente → LLM vs Agente
  → El ciclo del agente → Sus herramientas → El ciclo en código → El agente en acción → Construye tu agente.
- **Notebook:** `01_construye.ipynb`. Van corriendo celdas contigo: cargan el agente, le dan una
  tarea normal ("resume los tickets") y **lo ven decidir y actuar solo**.
- **Mensaje clave:** un agente = LLM + herramientas + bucle. Le dimos **todas** las herramientas
  **sin control**... guarda ese detalle (lo explotamos en el Bloque 2).

### Bloque 2 · Rompe el agente 🔴 (rojo)
- **Diapos:** ¿Por qué se puede atacar? → OWASP Top 10 → Ataque 1 (directa) → Ataque 2 (indirecta,
  con el archivo malicioso) → Ataque 3 (destructiva) → **Jailbreaks (bonus, cultura)** → Tu turno.
- **Notebook:** `02_ataca.ipynb`. Lanzan los **3 ataques** y ven cómo cae el agente:
  1. **Inyección directa:** le piden leer `secretos.txt` con autoridad.
  2. **Inyección indirecta (la estrella):** meten el ticket envenenado y, con una tarea normal,
     el agente filtra los secretos. Aquí detente y recálcalo: *obedeció al documento, no al usuario*.
  3. **Acción destructiva:** el agente borra archivos con `rm` sin preguntar.
- **Lo de jailbreaks** es solo para explicar en diapo (no lo hacen en la notebook): qué es, tipos
  (DAN, abuelita, ficción, opposite). Déjalo como cultura de red team.
- **Entregable:** su hoja de hallazgos con los 3 ataques.

### Bloque 3 · Repara el agente 🔵 (azul)
- **Diapos:** Defensa en profundidad → Separar datos (antes/después) → Control de acceso →
  Mínimo privilegio + humano → Cada ataque, tapado.
- **Notebook:** `03_repara.ipynb`. Implementan **3 defensas con código** (formato 🔴 antes /
  🟢 después) y **re-lanzan los ataques** para ver que ya fallan:
  1. **Separar datos de instrucciones** (system prompt + envolver el contenido).
  2. **Control de acceso** (que no salga de su carpeta).
  3. **Mínimo privilegio + confirmación humana** (`input()` antes de comandos peligrosos).
- **Nota:** en la Defensa 3B, al correr el comando aparece un **cuadro de texto** en Colab
  (el `input()`); los alumnos escriben `n` para bloquear. Avísales que eso es normal.
- **Mensaje clave:** ninguna defensa sola basta → **defensa por capas**.

### Cierre
- **Diapos:** Lo que nos llevamos → Recuérdalas → Pasa en producción → Para profundizar →
  Referencias → ¡Gracias!
- Recapitula las 3 ideas: un agente es poder · datos ≠ órdenes · defensa por capas.

---

## 5. Errores comunes

| Síntoma | Causa | Solución |
|---|---|---|
| `Invalid API key` / 401 | Key mal pegada o sin saldo | Que repeguen la key completa entre las comillas; revisa saldo en DeepSeek |
| La Celda 1 falla al clonar | El repo no es público o el nombre cambió | Confirma que el repo es **Public** y la URL es `briancgx/taller-agentes` |
| `ModuleNotFoundError: openai` | No corrieron la Celda 1 | Que corran la primera celda (instala `openai`) |
| `ModuleNotFoundError: agente` | No están dentro de la carpeta `taller` | La Celda 1 hace `%cd taller`; que la corran antes de las demás |
| El `input()` de la Defensa 3B no aparece | Se perdió el foco | Que vuelvan a correr la celda; el cuadro sale debajo |
| Va lentísimo / rate limit | Todos pegan a la vez con una sola key | Escalona: que no todos corran el agente al mismo segundo; ten saldo de sobra |
| Se "rompió" el entorno | Estado raro de la VM | **Entorno de ejecución → Reiniciar** y volver a correr desde arriba |

---

## 6. Checklist

**Antes (en casa):**
- [x] Repo subido a GitHub como **público** (`briancgx/taller-agentes`).
- [ ] Los 3 enlaces de Colab probados (clonan y corren).
- [ ] API key de DeepSeek con saldo; enlaces/key a la mano.
- [ ] `index.html` abre y proyecta bien (prueba el modo pantalla completa con F).
- [ ] CTF listo en `_ctf_privado/` por si da tiempo.

**En el aula:**
- [ ] Pide que traigan cuenta de Google ya iniciada.
- [ ] Comparte los enlaces de Colab y dicta/pega la API key.
- [ ] Confirma que todos ven "Hola, mi conexión funciona" antes de arrancar el Bloque 1.

**Al terminar:**
- [ ] 🔒 Borra/rota la API key de DeepSeek.
