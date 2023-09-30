punctuation=[" ",";",",",":","-","!","?", "\"", "."]

def groupingtextby_m(text, key):
    m = len(key)
    text = text.lower()
    for punc in punctuation:
        text = text.replace(punc, '')

    text=[text[i:i+m] for i in range(0, len(text), m)]

    if len(text[-1]) < m:
        last_word = text[-1]
        for i in range(0, m - len(last_word)):
            last_word += 'а'
        
        text[-1] = last_word
 
    return text

def encryption(grouped_text, key):

    encrypted_text = ''
    key_array = []
    for chr in key:
        key_array.append(ord(chr) - ord('а'))

    for column in range(0, len(key_array)):

        encrypted_word = ''

        min_ele = min(key_array)
       
        i = key_array.index(min_ele)
        
        for row in grouped_text:

            j = grouped_text.index(row)
            encrypted_word += grouped_text[j][i]

        key_array[i] = 12345
        encrypted_text += encrypted_word

    return encrypted_text

key = "пароль"
plaintext = "нельзя недооценивать противника"
print("\n")
print("ORIGINAL TEXT: " + plaintext)
print("KEY: " + key)
print("\n")

grouped_text = groupingtextby_m(plaintext, key)

print("GROUPED TEXT BY KEY: ", grouped_text)

print("\n")
encrypted_text = encryption(grouped_text, key)
print("ENCRYPTED TEXT: " + encrypted_text)