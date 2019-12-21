"""page 194"""


def search4vowels(word):
    """Возвращает булево значение в зависимости от присудствия гласных в слове"""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return bool(found)


print(search4vowels('galaxy'))
