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

El enlace "Abrir en Colab" de la notebook del taller es:

```
https://colab.research.google.com/github/briancgx/taller-agentes/blob/main/notebooks/taller.ipynb
```

Es **una sola notebook** para todo el taller. **Pruébala tú antes** de punta a punta (incluida la app
de chat y los prompts de `ataques/prompts_de_ataque.md`) para confirmar que todo funciona.

> Truco para compartir rápido: pon el enlace en un acortador o en una diapo.

### 2.4 La API key de DeepSeek

- Usaremos **una sola key para todo el grupo** (la tuya). Es lo más simple.
- Entra a tu panel de DeepSeek, asegúrate de tener **saldo** (unos pocos dólares bastan para ~30 alumnos).
- Copia la key; se la vas a dictar/pegar a los alumnos en el Bloque 0.
- 🔒 **Al terminar el taller, bórrala/rótala** en el panel de DeepSeek. Así, aunque haya quedado
  pegada en las notebooks de alguien, deja de servir.

---

## 3. El día del taller

Montaje de cada alumno (toma ~5 min, hazlo con ellos en el Bloque 0):

1. Abren el **enlace de Colab de `taller.ipynb`** (tú lo compartes).
2. Arriba a la izquierda, **"Copiar en Drive"** (o simplemente empezar a correr celdas — Colab les
   pedirá permiso de ejecución, que acepten).
3. Corren la **Celda 1** (clona el repo e instala `openai` y `gradio`). Tarda ~30 s.
4. En la **celda de la API key**, reemplazan `PEGA_AQUI_LA_API_KEY` por la key que les diste.
5. Corren la **celda de prueba**: si ven "Hola, mi conexión funciona" → ✅ listos.

> Pídeles que corran **de arriba hacia abajo** y que no se salten celdas.

---

## 4. Guion bloque por bloque

> Tiempos aproximados y con holgura. Tú sueles ir rápido; si sobra, hay material extra para estirar el cierre.

### Bloque 0 · Bienvenida y setup
- **Diapos:** portada → ¿Quién soy? → El plan → El entorno → El repositorio → Cómo se monta el entorno →
  Abrir la notebook → Cómo usar Colab → Pasos 1 a 3 (descargar, API key, probar conexión).
- **Haz:** preséntate, explica el arco (crear → hackear → proteger) y que todo es en un entorno
  desechable. Monta a los alumnos (sección 3). Que todos lleguen a "conexión funciona".
- **Entregable:** todos con `taller.ipynb` abierta y la conexión verde.

### Bloque 1 · Construye el agente 🛠️ (verde)
- **Diapos:** Concepto LLM → Así predice un LLM → Transformer → Concepto Agente → De un LLM a un agente →
  El ciclo → Pasos 4 a 10 (escenario, instrucciones, herramientas, motor, app de chat, primeras pruebas)
  → Tres vulnerabilidades del agente.
- **Notebook:** `taller.ipynb`, Sección 1. Arman el agente celda por celda (instrucciones,
  herramientas, herramientas permitidas, motor), abren la **app de chat** y le piden algo normal
  ("resume los tickets"): **lo ven decidir y actuar solo**.
- **Mensaje clave:** un agente = LLM + herramientas + bucle. Le dimos **todas** las herramientas
  **sin control**... guarda ese detalle (lo explotamos en el Bloque 2).

### Bloque 2 · Rompe el agente 🔴 (rojo)
- **Diapos:** Red Team vs Blue Team → AI Red Team → Red Team vs AI Red Team → Concepto inyección →
  ¿Por qué se puede atacar? → OWASP → Ataque 1 + Prueba tú → Ataque 2 + Prueba tú → Ataque 3 + Prueba tú
  → Jailbreak (concepto y técnicas) → Hoja de hallazgos.
- **Notebook:** `taller.ipynb`, Sección 2. Pegan los prompts de `ataques/prompts_de_ataque.md` en el chat
  (borrando la conversación entre prueba y prueba) y ven cómo cae el agente:
  1. **Inyección directa:** le piden leer `secretos.txt` con autoridad.
  2. **Inyección indirecta (la estrella):** meten el ticket envenenado y, con una tarea normal,
     el agente filtra los secretos. Aquí detente y recálcalo: *obedeció al documento, no al usuario*.
  3. **Acción destructiva:** el agente borra archivos con `rm` sin preguntar.
- **Lo de jailbreaks** es solo para explicar en diapo (no lo hacen en la notebook): qué es, tipos
  (DAN, abuelita, ficción, opposite). Déjalo como cultura de red team.
- **Entregable:** su hoja de hallazgos con los 3 ataques.

### Bloque 3 · Repara el agente 🔵 (azul)
- **Diapos:** Defensa en profundidad → Cómo se aplica cada defensa → D1A → D1B → Prueba → Control de
  acceso → D2 → Prueba → La terminal todavía da acceso → Mínimo privilegio → D3A → Humano en el bucle →
  D3B → Prueba → Resumen.
- **Notebook:** `taller.ipynb`, Sección 3. **Reemplazan el código** de las celdas del agente
  (buscándolas por su título `# === CELDA: ... ===`), las corren y **repiten los mismos prompts**:
  1. **Separar datos de instrucciones** (system prompt + envolver el contenido).
  2. **Control de acceso** (que no salga de su carpeta).
  3. **Mínimo privilegio + aprobación humana** (sin terminal; y si la necesita, el comando queda
     en espera hasta que el humano escriba `aprobar` o `rechazar` en el chat).
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
| `NameError` (p. ej. `cliente` o `MEMORIA`) | Se saltaron celdas | Correr de arriba hacia abajo, sin saltarse ninguna |
| La defensa "no hace nada" | Pegaron el código pero no corrieron la celda | Correr la celda editada con ▶ y borrar el chat antes de repetir el ataque |
| El chat no carga dentro de Colab | El visor de Colab falló | Abrir el enlace `gradio.live` que imprime la celda de la app |
| Va lentísimo / rate limit | Todos pegan a la vez con una sola key | Escalona: que no todos corran el agente al mismo segundo; ten saldo de sobra |
| El chat se comporta raro tras muchas pruebas | La conversación acumulada influye | Borrar el chat (papelera) antes de cada prueba |
| Se "rompió" el entorno | Estado raro de la VM | **Entorno de ejecución → Reiniciar** y volver a correr desde arriba |

---

## 6. Checklist

**Antes (en casa):**
- [x] Repo subido a GitHub como **público** (`briancgx/taller-agentes`).
- [ ] `taller.ipynb` probada de punta a punta en Colab (chat, ataques y defensas).
- [ ] API key de DeepSeek con saldo; enlaces/key a la mano.
- [ ] El deck actual (artifact de Slides) proyecta bien; `slides/` del repo trae la versión anterior.
- [ ] CTF listo en `_ctf_privado/` por si da tiempo.

**En el aula:**
- [ ] Pide que traigan cuenta de Google ya iniciada.
- [ ] Comparte el enlace de Colab y la API key.
- [ ] Confirma que todos ven "Hola, mi conexión funciona" antes de arrancar el Bloque 1.

**Al terminar:**
- [ ] 🔒 Borra/rota la API key de DeepSeek.
