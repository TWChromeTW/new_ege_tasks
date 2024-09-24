import re
from collections import Counter

# Функция для расчета времени на пересказ текста
def calculate_time(text):
    # Разделяем текст на абзацы
    paragraphs = text.strip().split("\n")
    
    total_time = 0  # Общее время
    for paragraph in paragraphs:
        # Удаляем знаки препинания и переводим текст в нижний регистр
        cleaned_paragraph = re.sub(r'[^\w\s]', '', paragraph)
        letters_count = len(cleaned_paragraph)
        
        # Определяем базовое время в зависимости от количества букв
        if letters_count < 160:
            time = 2  # минуты
        elif 160 <= letters_count <= 230:
            time = 3.5  # минуты
        else:
            time = 7  # минут
        
        # Считаем количество повторяющихся слов
        words = cleaned_paragraph.lower().split()
        word_counts = Counter(words)
        
        # Вычисляем количество повторений (считаем количество слов с повторением > 1)
        repetitions = sum(count - 1 for count in word_counts.values() if count > 1)
        
        # Уменьшаем время на 15 секунд (0.25 минуты) за каждое повторение
        time -= repetitions * 0.25
        
        # Обеспечиваем, что время не может быть меньше 0
        if time < 0:
            time = 0
        
        total_time += time
    
    return total_time

text = open("for_task3.txt")

# Подсчитываем необходимое время
required_time = calculate_time(text)

# Выводим результат
print(f'Ване понадобится {required_time:.2f} минут(ы) для выполнения домашнего задания.')



