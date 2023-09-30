alphabet="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

punctuation=[" ",";",",",":","-","!","?", "\"", "."]

def generate_table():
    reminders_alphabet = ""
    
    table = []
    
    for a in alphabet:
        
        tab = alphabet[alphabet.index(a):alphabet.index("я")] + "я" + reminders_alphabet
        table.append(tab)
        reminders_alphabet += a
        
        print(tab)

    return table

def groupingtextby_m(text, key):
    m = len(key)
    text = text.lower()
    for punc in punctuation:
        text = text.replace(punc, '')

    text=[text[i:i+m] for i in range(0, len(text), m)]
    return text

def encryption(table, word, key):

    m = len(key)
    encrypted_word = ""

    for chr in word:
    
        i = alphabet.index(chr)
        j = alphabet.index(key[0:1])

        encrypted_word += table[j][i]

        key = key[0+1:]

    return encrypted_word

def decryption(table, ciphertext, key):

    decrypted_word = ''

    for chr in ciphertext:
        
        i = alphabet.index(chr)
        j = alphabet.index(key[0:1])

        word_index = table[j].index(chr)

        decrypted_word += alphabet[word_index]

        key = key[0 + 1:]

    return decrypted_word

text = input("Enter text: ")
key = "математика"

table = generate_table()

print("\n")
grouped_by_m = groupingtextby_m(text, key)

encrypted_text = ''

for word in grouped_by_m:
    encrypted_word = encryption(table, word, key)

    encrypted_text += encrypted_word + ' '

decrypted_text = ''

for word in encrypted_text.split(' '):
    decrypted_word = decryption(table, word, key)

    decrypted_text += decrypted_word + ' '


print("\n")
print("ENCRYPTED TEXT: " + encrypted_text)

print("\n")
print("DECRYPTED TEXT: " + decrypted_text)