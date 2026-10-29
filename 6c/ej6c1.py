"""
Enunciado:
Utilizando la librería NLTK, implementa una función 'sentiment_analysis(text)'
que recibe como parámetro 'text' que es una cadena de strings, la misma que
debe ser analizada para saber si esa frase representa una emoción negativa o
positiva.

Se debe utilizar 'SentimentIntensityAnalyzer' que es importada desde 
'nltk.sentiment', de esta manera obtendremos una puntuación en base al número
de palabras que se esten asociando a algo positivo o negativo dentro de la frase
analizada.

Utilizaremos el módulo nltk.sentiment.vader para analizar el sentimiento de un texto.
Te recmendamos que revises la documentación:
https://www.nltk.org/api/nltk.sentiment.vader.html

En concreto, revisa la función polarity_scores(text) 

Si la puntuación es mayor de 0.05 se retorna un resultado positivo, si es menor
a -0.05 se retorna un resultado negativo y si se encuentra entre los valores
-0.05 y 0.05 inclusives, se retorna un resultado neutro.

Parámetro:
text: Cadena de strings.

Ejemplo:
    Entrada:
        "I love going to the beach on a sunny day, but I hate getting 
        sunburned."

    Salida:
        "Negative"

"""
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")

def sentiment_analysis(text):
    # Creamos un analizador de sentimientos utilizando NLTK
    analizador = SentimentIntensityAnalyzer()
    
    # Analizamos el texto y obtenemos un diccionario con las puntuaciones
    # de sentimiento negativo (neg), neutro (neu), positivo (pos)
    # y una puntuación global (compound)
    score_dict = analizador.polarity_scores(text)
    
    # Extraemos la puntuación global, que va de -1 (negativo)
    # a +1 (positivo), y la guardamos en una variable
    score = score_dict["compound"]
    
    if score > 0.05:
        return "Positive"
    elif score < -0.05:
        return "Negative"
    else:
        return "Neutral"


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
#text = "I love going to the beach on a sunny day, but I hate getting sunburned."
#print(sentiment_analysis(text))
