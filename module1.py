import math
from googletrans import Translator

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

def translate_text(text, language):
    translator = Translator()
    translated = translator.translate(text, dest=language)
    return translated.text