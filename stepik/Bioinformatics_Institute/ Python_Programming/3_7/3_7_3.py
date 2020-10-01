# https://stepik.org/lesson/3380/step/4?unit=963
"""Простейшая система проверки орфографии основана на использовании списка известных слов.
 Каждое слово в проверяемом тексте ищется в этом списке и, если такое слово не найдено, оно помечается, как ошибочное.

Напишем подобную систему.

Через стандартный ввод подаётся следующая структура: первой строкой — количество d записей в списке известных слов,
после передаётся  d строк с одним словарным словом на строку, затем — количество l строк текста,
после чего — l строк текста.

Напишите программу, которая выводит слова из текста, которые не встречаются в словаре. Регистр слов не учитывается.
Порядок вывода слов произвольный. Слова, не встречающиеся в словаре, не должны повторяться в выводе программы.
"""
count_words = int(input())
glossary = []
for i in range(count_words):
    word = input().lower()
    glossary.append(word)

count_str = int(input())
text = []
for i in range(count_str):
    string = input()
    text.append(string)

words_that_not_in_dictionary = set()
for s in text:
    splited = s.split()
    for w in splited:
        if w.lower() not in glossary:
            words_that_not_in_dictionary.add(w)

for s in words_that_not_in_dictionary:
    print(s)
