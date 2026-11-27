ALPHABET_SIZE = 26

message: str = input("Message: ")
key: int = int(input("Key: "))



cyphertext = ""

#Encryption Loop    
for character in message:
    if "A" <= character <= "Z": #For Capital letters
        shifted = ord(character) + key
        if shifted > ord("Z"):
            shifted-= ALPHABET_SIZE
        cyphertext += chr(shifted)

    elif "a" <= character <= "z": #For Simple letters
        shifted = ord(character) + key
        if shifted > ord("z"):
            shifted -= ALPHABET_SIZE
        cyphertext += chr(shifted)

    else:
        cyphertext += character

print(cyphertext)

plaintext = ""

#Decryption Loop    
for character in cyphertext:
    if "A" <= character <= "Z": #For Capital letters
        shifted = ord(character) - key
        if shifted < ord("A"):
            shifted += ALPHABET_SIZE
        plaintext += chr(shifted)

    elif "a" <= character <= "z": #For Simple letters
        shifted = ord(character) - key
        if shifted < ord("a"):
            shifted += ALPHABET_SIZE
        plaintext += chr(shifted)
        
    else:
        plaintext += character

print(plaintext)

#Check if decryption is correct
assert message == plaintext, "Decryption failed"