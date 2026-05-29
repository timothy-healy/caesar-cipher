"""
    This program applies a caesar cipher to a given message. It can encrypt,
    decrypt with a known key, or break.
"""
#frequency of each letter in English
FREQ_DICT = {
    " ":0.13,
    "e":0.124167,
    "t":0.0969225,
    "a":0.0820011,
    "i":0.0768052,
    "n":0.0764055,
    "o":0.0714095,
    "s":0.0706768,
    "r":0.0668132,
    "l":0.0448308,
    "d":0.0363709,
    "h":0.0350386,
    "c":0.0344391,
    "u":0.028777,
    "m":0.0281775,
    "f":0.0235145,
    "p":0.0203171,
    "y":0.0189182,
    "g":0.0181188,
    "w":0.0135225,
    "v":0.0124567,
    "b":0.0106581,
    "k":0.00393019,
    "x":0.00219824,
    "j":0.0019984,
    "q":0.0009325,
    "z":0.000599
}

# make the letters the corresponding byte values
FREQ_BYTES_DICT = {ord(k):v for k,v in FREQ_DICT.items()}

"""
    The caesar_shift function expects a plain byte string
    and an integer 0 < shift < 256.
    Performs the given shift and outputs the encrypted bytes.
"""
def caesar_shift(plain_bytes, shift):
    return bytes([((b + shift) % 256) for b in plain_bytes])

"""
    The scorer uses the FREQ_BYTE_DICT to score a given decrypting attempt.
    The more it seems like real English, the higher the score.
"""
def scorer(attempt):
    score = 0
    for b in attempt:
        if b > 127: # this means byte is unprintable
            score -= 0.05
        elif b < 32: # also unprintable
            score -= 0.05
        else:
            b = b | 0x20 # forcing to lowercase
            score += FREQ_BYTES_DICT.get(b, 0)
    return score

"""
    break_caesar tries all 256 possible shifts and uses the scorer to determine
    the best one. Outputs the one with the highest score
"""
def break_caesar(cipher_bytes):
    best_score = float("-inf")
    best_attempt = b""
    for shift in range(256):
        attempt = caesar_shift(cipher_bytes, shift)
        score = scorer(attempt)
        if score > best_score:
            best_score = score
            best_attempt = attempt
    return best_attempt

def main():
    print("Enter 1 for encrypting, 2 for decrypting, 3 for breaking, 4 to quit.")
    choice = int(input())

    while choice != 4:
        if choice == 1:
            message = bytes(input("What message would you like to encrypt? ").strip(), "ascii")
            shift = 0
            while shift == 0:
                shift = int(input("Enter your desired shift: ")) % 256
                if shift == 0:
                    print("This results in no shift. Enter a new number: ")

            encrypted_message = caesar_shift(message, shift).hex()
            print("Encrypted message (hex):")
            print(encrypted_message)
        
        elif choice == 2:
            message = bytes.fromhex(input("What hex-coded message would you like to decrypt? ").strip())
            shift = 0
            while shift == 0:
                shift = int(input("Enter the desired shift: ")) % 256
                if shift == 0:
                    print("This results in no shift. Enter a new number: ")

            decrypted_message = caesar_shift(message, 256 - shift).decode("ascii")
            print("Decrypted message:")
            print(decrypted_message)
        
        elif choice == 3:
            message = bytes.fromhex(input("What hex-coded message would you like to decrypt? ").strip())
            decrypted_message = break_caesar(message).decode("ascii")

            print("Decrypted message: ")
            print(decrypted_message)
        
        else:
            print("Invalid choice")
        
        print("Enter 1 for encrypting, 2 for decrypting, 3 for breaking, 4 to quit.")
        choice = int(input())
    print("Goodbye")

if __name__ == "__main__":
    main()
