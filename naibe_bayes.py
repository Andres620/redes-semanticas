from collections import Counter
import pandas as pd

# Datos
comentarios_positivos = ["La comida en este restaurante es excelente.", "Recomiendo este lugar, la atención es increíble.", "El ambiente es acogedor y la comida deliciosa.", "El personal fue amable y atento en todo momento.", "El restaurante tiene una decoración única y original."]
comentarios_negativos = ["El servicio fue muy lento y la comida estaba fría.", "No volvería a este restaurante, la calidad de la comida es pésima.", "El precio es excesivo para la calidad de la comida.", "La comida no cumplió con mis expectativas, fue decepcionante.", "El servicio al cliente es deficiente y la comida llegó tarde."]

# Tokenizar y contar frecuencia de palabras en comentarios positivos
palabras_positivas = [palabra.lower() for comentario in comentarios_positivos for palabra in comentario.split()]
frecuencia_positiva = Counter(palabras_positivas)

# Tokenizar y contar frecuencia de palabras en comentarios negativos
palabras_negativas = [palabra.lower() for comentario in comentarios_negativos for palabra in comentario.split()]
frecuencia_negativa = Counter(palabras_negativas)

# Crear DataFrame para mostrar resultados
df_positivo = pd.DataFrame(list(frecuencia_positiva.items()), columns=['Palabra', 'Positivo'])
df_negativo = pd.DataFrame(list(frecuencia_negativa.items()), columns=['Palabra', 'Negativo'])

# Combinar DataFrames en una sola tabla
df_combinado = pd.merge(df_positivo, df_negativo, on='Palabra', how='outer').fillna(0)

# Mostrar resultados
print(df_combinado)
