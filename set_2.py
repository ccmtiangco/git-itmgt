def shift_letter(letter, shift):
    if letter.isalpha():
        base = ord('A') if letter.isupper() else ord('a')
        shifted = (ord(letter) - base + shift) % 26 + base
        return chr(shifted)
    return letter

def caesar_cipher(message, shift):
    return ''.join(shift_letter(char, shift) for char in message)

def shift_by_letter(letter, letter_shift):
    if letter_shift.isalpha():
        shift = ord(letter_shift.lower()) - ord('a')
        return shift_letter(letter, shift)
    return letter


def vigenere_cipher(message, key):
    def vigenere_cipher(message, key):
        result = []
    key_length = len(key)
    key_index = 0

    for char in message:
        shift = ord(key[key_index % key_length]) - ord('A')

        if char == " ":
            result.append(" ") 
        else:
            new_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            result.append(new_char)

        key_index += 1  

    return "".join(result)

def scytale_cipher(message, shift):
    if shift <= 0:
        return message
    length = len(message)
    num_cols = (length + shift - 1) // shift
    padded_length = num_cols * shift
    message += '_' * (padded_length - length)
    ciphered_message = []
    for col in range(num_cols):
        for row in range(shift):
            index = row * num_cols + col
            if index < len(message):
                ciphered_message.append(message[index])
    return ''.join(ciphered_message)


def scytale_decipher(message, shift):
    length = len(message)
    columns = length // shift
    deciphered = [''] * length

    for i in range(length):
        row = i % shift
        col = i // shift
        new_index = row * columns + col
        deciphered[new_index] = message[i]

    return ''.join(deciphered)

