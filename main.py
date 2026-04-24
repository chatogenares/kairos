import subprocess
from analyzer import analyze
from prompts import construir_prompt
from styles import (
    estilo_profesional,
    estilo_persuasivo,
    estilo_kairos
)

def llamar_llm(prompt):
    resultado = subprocess.run(
        ["ollama", "run", "qwen3.5", prompt],
        capture_output=True,
        text=True
    )
    return resultado.stdout.strip()

def main():
    texto = input("Escribe texto: ")

    # 1. Analizar
    analisis = analyze(texto)

    # 2. Construir prompt
    prompt = construir_prompt(texto, analisis)

    # 3. Llamar al modelo
    respuesta = llamar_llm(prompt)

    # 4. Aplicar estilos
    print("\n--- Profesional ---")
    print(estilo_profesional(respuesta))

    print("\n--- Persuasivo ---")
    print(estilo_persuasivo(respuesta))

    print("\n--- Kairos ---")
    print(estilo_kairos(respuesta))

if __name__ == "__main__":
    main()
