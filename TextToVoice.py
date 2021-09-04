from gtts import gTTS

# Text
text = "La historia del lenguaje de programación Python se remonta hacia finales de los 80s y principio de los 90, su implementación comenzó en diciembre de 1989 cuando en Navidad Guido Van Rossum que trabajaba en el (CWI)"

# Convert text to audio
audio = gTTS(text=text, lang="es", slow=False)

# Save file audio
audio.save("voice.mp3")