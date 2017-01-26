def alphabet_position(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return (alphabet.index(letter.lower()))

def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    if char.lower() not in alphabet:
        encrypted = char
    else:
        rotated_index = alphabet_position(char) + rot
        if rotated_index < 26:
            encrypted = encrypted + alphabet[rotated_index]
        else:
            encrypted = encrypted + alphabet[rotated_index % 26]
    if char.islower():
        return (encrypted)
    else:
        return (encrypted.upper())

def encrypt(text, rot):
    rotated = []
    for x in text:
        rotated.append(rotate_character(x, rot))
    return ''.join(rotated)
