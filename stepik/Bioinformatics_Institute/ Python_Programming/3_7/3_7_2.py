"""символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра
"""

original_alphabet = input()
finite_alphabet = input()
encode = input()
decode = input()

encode_alphabet = {}
decode_alphabet = {}
for k, v in zip(original_alphabet, finite_alphabet):
    encode_alphabet[k] = v
    decode_alphabet[v] = k


def coder_decoder(string, alphabet):
    encode_r = ''
    for ch in string:
        if ch in alphabet.keys():
            encode_r += alphabet[ch]
        else:
            encode_r += ch
    return encode_r


print(coder_decoder(encode, encode_alphabet))
print(coder_decoder(decode, decode_alphabet))
