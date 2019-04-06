"""page 103"""
phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

new_phrase = plist[1:5]
new_phrase.extend(plist[-6:-4:1][::-1])
# new_phrase = ''.join(new_phrase).replace("'", ' ')

new_phrase.remove("'")
new_phrase.insert(2, ' ')
print(new_phrase)
# on tap
