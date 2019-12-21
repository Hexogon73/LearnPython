"""page 198"""


def search4vowels(word: str) -> set:
    """Возвращает гласные, найденные в слове"""
    vowels = set('aeiou')
    return vowels.intersection(set(word))


print(search4vowels('galaxy'))
print(search4vowels('sky'))

"""page 204"""


def search4letters(phrase: str, letters: str) -> set:
    """Возвращает множество букв из 'letters', найденных в указанной фразе"""
    return set(letters).intersection(set(phrase))


print(search4letters('galaxy', 'aeiou'))
print(search4letters('sky', 'aeiou'))
