import re

def is_palindrome(word):
    return word == word[::-1]

def find_palindromes(text):
    # Удаляем знаки препинания и приводим текст к нижнему регистру
    text = re.sub(r'[^\w\s]', '', text)
    words = text.lower().split()
    
    palindromes = [word for word in words if is_palindrome(word) and len(word) > 1]
    
    return palindromes

text = open("for_task1_task2.txt").read()

# Находим палиндромы
palindromes = find_palindromes(text)

# Подсчитываем количество палиндромов
palindrome_count = len(palindromes)

# Находим самый длинный палиндром
longest_palindrome = max(palindromes, key=len) if palindromes else None

# Выводим результаты
print(f"Количество палиндромов: {palindrome_count}")
if longest_palindrome:
    print(f"Самый длинный палиндром: '{longest_palindrome}'")
else:
    print("Палиндромов не найдено.")


