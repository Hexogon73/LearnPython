"""page 190"""


def search4vowels(word):
    """Выводит гласные, найденые во введенном слове"""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    for vowel in sorted(found):
        print(vowel)


search4vowels('galaxy')
