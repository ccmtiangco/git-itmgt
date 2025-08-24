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
    key_repeated = []
    key_length = len(key)
    key_index = 0

    for char in message:
        if char.isalpha():
            key_repeated.append(key[key_index % key_length])
            key_index += 1
        else:
            key_repeated.append(char)

    ciphered_message = []
    for m_char, k_char in zip(message, key_repeated):
        if m_char.isalpha():
            shift = ord(k_char.lower()) - ord('a')
            ciphered_message.append(shift_letter(m_char, shift))
        else:
            ciphered_message.append(m_char)

    return ''.join(ciphered_message)

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
    if shift <= 0:
        return message
    length = len(message)
    num_cols = (length + shift - 1) // shift
    num_full_cols = length % shift
    if num_full_cols == 0:
        num_full_cols = shift
    deciphered_message = [''] * length
    index = 0
    for col in range(num_cols):
        for row in range(shift):
            if col < num_full_cols or row < (length // num_cols):
                deciphered_message[row * num_cols + col] = message[index]
                index += 1
    return ''.join(deciphered_message).rstrip('_')