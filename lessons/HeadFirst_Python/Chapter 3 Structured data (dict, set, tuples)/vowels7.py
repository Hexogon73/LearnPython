"""page 166"""
vowels = set('aeiou')
word = input("Provide a world to search for vowels: ")
found = vowels.intersection(set(word))
for vowel in sorted(found):
    print(vowel)
