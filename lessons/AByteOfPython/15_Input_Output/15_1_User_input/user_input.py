# -*- coding: utf-8 -*-


def reverse(text):
    text = text.lower()
    text = ''.join([c for c in text if c not in (' ', ',', '"', '\'')])
    return text[::-1]


def is_palindrome(text):
    text = text.lower()
    text = ''.join([c for c in text if c not in (' ', ',', '"', '\'')])
    return text == reverse(text)


something = input('Input text: ')
if is_palindrome(something):
    print('True, it\'s palindrome')
else:
    print('False it isn\'t palindrome')

# А роза упала на лапу Азора
