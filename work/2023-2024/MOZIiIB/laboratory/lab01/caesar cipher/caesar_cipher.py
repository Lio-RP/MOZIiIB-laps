#реализовать шифр цезаря с произвольным ключом k

def caesar_cipher(text, k):
    incryption = ''
    
    for char in text:

        shift = ''

        if char.isalpha():

            if char.isupper():
                shift = 65
               
            else:
                shift = 97

            char_index = ord(char) - shift
            incryption += chr((char_index + k) % 26 + shift)

        else:
            incryption += char
    
    return incryption

def decryption(incryptedText, k):
    text = ''
    
    for char in incryptedText:

        shift = ''

        if char.isalpha():

            if char.isupper():
                shift = 65
               
            else:
                shift = 97

            char_index = ord(char) - shift
            text += chr((char_index - k) % 26 + shift)

        else:
            text += char
    
    return text

plainText = input("Enter Text: ")
key = 3
ciphertext = caesar_cipher(plainText, key)

print("\nШифрование")
print("Plaintext:", plainText)
print("Ciphertext:", ciphertext)

print("")
print("Расшифровка")
decrypted = decryption(ciphertext, key)
print("Ciphertext:", ciphertext)
print("Plaintext:", decrypted)
