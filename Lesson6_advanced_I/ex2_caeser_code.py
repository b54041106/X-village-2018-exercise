word = input("明文：")
d = 3
caesar_cipher=list(word)
i = 0
while i < len(caesar_cipher):
    if ord(caesar_cipher[i]) < 123-d:
        caesar_cipher[i] = chr(ord(word[i]) + d)
    else:
        caesar_cipher[i] = chr(ord(word[i]) + d - 26)
    i = i+1
print(caesar_cipher,',',d)

    