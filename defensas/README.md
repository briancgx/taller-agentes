# 🛡️ Soluciones de las defensas (Bloque 3)

Aquí están las versiones **completas y correctas** de cada defensa, por si un alumno
se atora o quieres mostrar la solución. En el taller, la idea es que ellos las
**escriban/peguen** en la notebook y entiendan qué hace cada línea.

| Archivo | Defensa | Ataque que tapa |
|---|---|---|
| `defensa_1_separar_datos.py` | Separar datos de instrucciones (prompt + envolver contenido) | Inyección directa e indirecta (LLM01) |
| `defensa_2_control_acceso.py` | Control de acceso / scope de carpeta | Fuga de `secretos.txt` |
| `defensa_3_minimo_privilegio.py` | Mínimo privilegio + confirmación humana | Borrado destructivo (LLM06) |

> Recuerda: ninguna defensa sola basta. La seguridad real es **por capas**
> (defensa en profundidad).
