# Kairos v0.1

Kairos es un micro‑motor de estilo e intención que:
- analiza un texto,
- construye un prompt,
- llama al modelo `qwen3.5` de Ollama,
- genera tres estilos: profesional, persuasivo y Kairos.

## Estructura del proyecto

Kairos/
│── main.py
│── analyzer.py
│── prompts.py
│── styles.py
│── requirements.txt
│── readme.md


## Uso

Ejecuta:  python main.py


Escribe cualquier texto y Kairos generará:
- una versión profesional,
- una versión persuasiva,
- una versión estilo Kairos.

## Requisitos

- Python 3.10+
- Ollama instalado
- Modelo `qwen3.5` descargado: ollama pull qwen3.5


## Estado

Versión mínima funcional (v0.1).  
Preparado para extender análisis, estilos y lógica interna.
