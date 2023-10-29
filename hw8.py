print("------------Задание 1------------")
numbers_list = [1, -3, 8, 5, 9, -12, 42]
new_numbers = list(filter(lambda x: x % 2 == 0, numbers_list))
print(new_numbers)

print("------------Задание 2------------")
persons = [("Max", 52), ("Anna", 45)]
person_new = sorted(persons, key=lambda x: x[1])
print(person_new)

print("------------Задание 3------------")


def first_vowel(s):
    letters = {"а", "е", "ё", "и", "о", "у", "э", "ю", "я"}
    return s[0].lower in letters


text = [("Ананас", "Апельсин"), ("Яблоко", "Груша"), ("Вишня", "Помело")]
text_new = list(filter(first_vowel, text))
print(text_new)

print("------------Задание 4------------")
numbers_list_2 = [1, 3, 7, -5, 10]
new_numbers_2 = list(map(lambda x: x ** 2, numbers_list_2))
print(new_numbers_2)

print("------------Задание 5------------")


def sort_words(words: list):
    sorted_words = sorted(words, key=lambda x: len(x), reverse=True)
    return sorted_words


words = ["Жираф", "Собака", "Кот", "Слон", "Обезьяна", "Пума"]
sorted_list = sort_words(words)
print(sorted_list)

print("------------Задание 6------------")
text = "Python is a high-level, general-purpose programming language".lower()
letters = ("p", "y", "t", "h", "o", "n")
filtered_letters = list(filter(lambda letter: letter in letters, text))
print(filtered_letters)

print("------------Задание 7------------")


def multiply(numbers):
    result = []
    for number in numbers:
        result.append(number * 10)
    return result


numbers_list_3 = [1, 2, 7, -10]
new_numbers = multiply(numbers_list_3)
print(new_numbers)

print("------------Задание 8------------")
text = ("Михаил", "Татьяна", "Ангелина", "Виктор")
sorted_words = sorted(text)
print(sorted_words)

print("------------Задание 9------------")
def palindrome_filter(strings):
    filtered_strings = list(filter(is_palindrome, strings))
    return filtered_strings


def is_palindrome(string):
    return string == string[::-1]


text = ["торт", "мадам", "око", "кошка"]
palindrome = palindrome_filter(text)
print(palindrome)

print("------------Задание 10------------")


def sort_words_by_vowels(words):
    def count_vowels(word):
        vowels = ["а", "е", "ё", "и", "о", "у", "э", "ю", "я"]
        count = 0
        for letter in word:
            if letter.lower() in vowels:
                count += 1
        return count

    sorted_words = sorted(words, key=count_vowels)
    return sorted_words


text = ["Клён", "Мандаринка", "Апельсиновый", "Каштан", "Ольха"]
sorted_words = sort_words_by_vowels(text)
print(sorted_words)

print("------------Задание 11------------")
text = ["Облачно", "Туман", "Дождь", "Солнечно", "Град"]
new_text = list(map(lambda x: x.upper(), text))
print(new_text)

print("------------Задание 12------------")
text = ["Облачно", "Туман", "Дождь", "Солнечно", "Град"]
new_text = list(map(lambda x: x + "Hello", text))
print(new_text)

print("------------Задание 13------------")


def sort_words_by_vowels(words):
    def count_vowels(word):
        vowel = ["а"]
        count = 0
        for letter in word:
            if letter.lower() in vowel:
                count += 1
        return count

    sorted_words = sorted(words, key=count_vowels)
    return sorted_words


text = ["Клён", "Мандаринка", "Апельсиновый", "Каштан", "Ольха"]
sorted_words = sort_words_by_vowels(text)
print(sorted_words)

print("------------Задание 14------------")


def sort_by_unique_letters(words):
    sorted_words = sorted(words, key=lambda x: len(set(x)))
    return sorted_words


words = ["Зоя", "Ирина", "Сергей", "Екатерина", "Игорь"]
sorted_words = sort_by_unique_letters(words)
print(sorted_words)