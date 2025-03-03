#Задание1
def is_palindrome(word):
    word = word.lower()
    word = ''.join(char for char in word if char.isalnum())
    return word == word[::-1]

user_input = input("Введите слово: ")

if is_palindrome(user_input):
    print(f"Слово '{user_input}' является палиндромом.")
else:
    print(f"Слово '{user_input}' не является палиндромом.")
    
#Задание2
def is_palindrom(word):
    word = word.lower()
    word = ''.join(char for char in word if char.isalnum())
    return word == word[::-1]

def find_palindromes(words):
    palindromes = [word for word in words if is_palindrom(word)]
    return palindromes

user_input = input("Введите слова через пробел: ")
words_list = user_input.split()

palindromes = find_palindromes(words_list)

if palindromes:
    print("Палиндромы из списка:", palindromes)
else:
    print("Палиндромов нет.")

#Задание3
import string

def is_palindrom(word):
    word = word.lower()
    word = ''.join(char for char in word if char.isalnum())
    return word == word[::-1]

def find_palindromes_in_text(text):
    text = text.lower()
    text = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in text)
    words = text.split()
   
    palindromes = set(word for word in words if is_palindrom(word))
    return palindromes

user_input = input("Введите текст: ")

palindromes = find_palindromes_in_text(user_input)

if palindromes:
    print("Найденные палиндромы:", ', '.join(palindromes))
else:
    print("Палиндромов нет.")
