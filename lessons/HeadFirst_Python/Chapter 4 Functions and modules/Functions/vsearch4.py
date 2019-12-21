"""page 195"""


def search4vowels(word):
    """Возвращает гласные, найденные в слове"""
    vowels = set('aeiou')
    return vowels.intersection(set(word))


print(search4vowels('galaxy'))
print(search4vowels('sky'))
