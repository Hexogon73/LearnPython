"""page 209"""


def search4vowels(phrase: str) -> set:
    """Возвращает гласные, найденные в указанной фразе"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Возвращает множество букв из 'letters', найденных в указанной фразе"""
    return set(letters).intersection(set(phrase))


print(search4vowels('galaxy'))
print(search4vowels('sky'))
print(search4letters('galaxy'))
print(search4letters('sky'))
