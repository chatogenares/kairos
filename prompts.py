def construir_prompt(texto, analisis):
    intent = analisis["intent"]
    tone = analisis["tone"]
    emotion = analisis["emotion"]
    level = analisis["level"]

    return (
        f"Texto original: {texto}\n"
        f"Intención: {intent}\n"
        f"Tono: {tone}\n"
        f"Emoción: {emotion}\n"
        f"Nivel: {level}\n\n"
        "Genera una respuesta profesional basada en estos datos."
    )
