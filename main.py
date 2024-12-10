#Задание №1

#Задание: Написать программу, которая принимает на вход слово и проверяет, является ли оно палиндромом.
#Условия:

    #Программа должна быть нечувствительна к регистру.
    #Игнорировать пробелы и знаки пунктуации.
#Пример использования:
    #isPalindrom("level") # True
    #isPalindrom("hello") # False

def is_palindrom(input_word):
    input_word = input("введите слово: ")
    #сначала преобразуем слово в нижний регистр 
    input_word.lower = input_word.lower()
    return input_word.lower == word.lower[::-1] 
    #проверка слова
if is_palindrom(input_word):   
    print(is_palindrom("level")) #true
else:
    print(is_palindrom("hello")) #false
is_palindrom(input_word)

#Задание №2

#Задание: Написать программу, которая принимает список слов и проверяет, какие из них являются палиндромами.
#Условия:

    #Слова передаются в виде списка через ввод пользователя.
    #Программа должна вывести все палиндромы из списка.

#Пример использования:
    #isPalindromList(["hello", "list", "level"]) # ["level"]

#def is_palindrom_list(words):
    #palindroms = ["hello", "list", "level"]
    #for word in words:


        








#Задание №3

#Задание: Написать программу, которая ищет все палиндромы в строке текста.
#Условия:

    #Программа должна игнорировать регистр и знаки пунктуации.
    #Если палиндромы повторяются, выводить их только один раз.

#Пример использования isPalindromString("Madam, Anna went to the civic center") # ["madam", "anna", "civic"]
 
