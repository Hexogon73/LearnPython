"""page 189"""


def search4vowels():
    """Выводит гласные, найденые во введенном слове"""
    vowels = set('aeiou')
    word = input('Provide a world to search for vowels: ')
    found = vowels.intersection(set(word))
    for vowel in sorted(found):
        print(vowel)


search4vowels()
