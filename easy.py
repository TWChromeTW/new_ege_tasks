import re
from collections import Counter

def analyze_text(text):
    # Удаляем знаки препинания и переводим текст в нижний регистр
    text = re.sub(r'[^\w\s]', '', text.lower())
    
    # Разделяем текст на слова
    words = text.split()
    
    # Подсчитываем количество вхождений каждого слова
    word_counts = Counter(words)
    
    # Находим слово с максимальным и минимальным количеством повторений
    max_word = max(word_counts, key=word_counts.get)
    
    
    return max_word, word_counts[max_word]

text = open("for_task1_task2.txt").read()

max_word, max_count = analyze_text(text)

print(f"Слово с максимальным количеством повторений: '{max_word}' ({max_count} раз(а))")

