"""
This program applies a caesar cipher to a given message. It can encrypt,
decrypt with a known key, or break. It can either operate on English letters,
or hex-encoded bytes. In the latter case, all output is hex.
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


def caesar_shift(message, shift):
    """
    Performs the shift on bytes by the input amount.

    Args:
        message: Message in bytes to be shifted.
        shift: Desired shift as int.

    Returns:
        bytes: The shifted bytes.
    """
    return bytes([((b + shift) % 256) for b in message])

def caesar_shift_text(message, shift):
    """
    Performs the shift on regular English text.
    Spaces and non-letter characters are not supported.

    Args:
        message: str of message to be shifted.
        shift: Desired shift as int.

    Returns:
        str: The shifted message.
    """
    output = ""
    message = message.lower()
    for char in message:
        # using ascii values 97 through 122 (inclusive)
        # mod 26 translated 97
        shifted_char = chr(((ord(char) - 97 + shift) % 26) + 97)
        output += shifted_char
    return output


def scorer(plaintext):
    """
    Scores plaintext based on how much it resembles English language.

    Args:
        plaintext: Plaintext as bytes to be evaluated.

    Returns:
        float: The score of the plaintext.
    """
    score = 0
    for b in plaintext:
        if b > 127: # this means byte is unprintable
            score -= 0.05
        elif b < 32: # also unprintable
            score -= 0.05
        else:
            b = b | 0x20 # forcing to lowercase
            score += FREQ_BYTES_DICT.get(b, 0)
    return score


def break_caesar(ciphertext):
    """
    Breaks a caesar cipher done on bytes.

    Args:
        ciphertext: Ciphertext as bytes.

    Returns:
        bytes: Decrypted plaintext.
    """
    best_score = float("-inf")
    best_attempt = b""
    for shift in range(256):
        attempt = caesar_shift(ciphertext, shift)
        score = scorer(attempt)
        if score > best_score:
            best_score = score
            best_attempt = attempt
    return best_attempt

def break_caesar_text(ciphertext_str):
    """
    Breaks a caesar cipher done only on letters.
    Spaces and non-letter characters are not supported.

    Args:
        ciphertext_str: Ciphertext as a str.
    
    Returns:
        str: Decrypted plaintext as a str.

    """
    best_score = float("-inf")
    best_candidate = ""
    for shift in range(26):
        candidate = caesar_shift_text(ciphertext_str, shift)
        score = scorer(bytes(candidate, "ascii"))
        if score > best_score:
            best_score = score
            best_candidate = candidate
    return best_candidate

def get_shift(mode):
    """
    Gets the desired shift from the user.

    Args:
        mode: 1 for text only, 2 for all bytes.

    Returns:
        int: The user's desired shift.
    """
    shift = 0

    if mode == 1:
        modulus = 26
    elif mode == 2:
        modulus = 256
    else:
        return 0

    while shift == 0:
        shift = int(input("Enter your desired shift: ")) % modulus
        if shift == 0:
            print("This results in no shift. Enter a new number.")
    
    return shift

def get_message(mode):
    """
    Gets the message to be encrypted/decrypted from the user.

    Args:
        mode: 1 for text only, 2 for operating on bytes from input hex.

    Returns:
        str or bytes: User's message as str (mode 1) or bytes (mode 2).
    """
    if mode == 1:
        message = input("What message? ").strip()
    elif mode == 2:
        message_hex = input("What hex-encoded message? ").strip()
        message = bytes.fromhex(message_hex)
    else:
        message = ""
    return message


def main():
    print("Enter 1 for encrypting, 2 for decrypting, 3 for breaking, 4 to quit.")
    choice = int(input())

    while choice != 4:
        print("Operate using regular text (1) or bytes and hex-encodings (2)?")
        mode = int(input())

        if choice == 1:
            if mode == 1:
                plaintext_str = get_message(mode)
                shift = get_shift(mode)
                ciphertext_str = caesar_shift_text(plaintext_str, shift)
                print("Encrypted message:")
                print(ciphertext_str)

            elif mode == 2:
                plaintext = get_message(mode)
                shift = get_shift(mode)
                ciphertext_hex = caesar_shift(plaintext, shift).hex()
                print("Encrypted message (hex):")
                print(ciphertext_hex)

            else:
                print("Invalid mode.")
        
        elif choice == 2:
            if mode == 1:
                ciphertext_str = get_message(mode)
                shift = 26 - get_shift(mode)
                plaintext_str = caesar_shift_text(ciphertext_str, shift)
                print("Decrypted message:")
                print(plaintext_str)

            elif mode == 2:
                ciphertext = get_message(mode)
                shift = 256 - get_shift(mode)
                plaintext_hex = caesar_shift(ciphertext, shift).hex()
                print("Decrypted message:")
                print(plaintext_hex)

            else:
                print("Invalid mode.")

        
        elif choice == 3:
            if mode == 1:
                ciphertext_str = get_message(mode)
                plaintext_str = break_caesar_text(ciphertext_str)
                print("Decrypted message:")
                print(plaintext_str)

            elif mode == 2:
                ciphertext = get_message(mode)
                plaintext_hex = break_caesar(ciphertext).hex()
                print("Decrypted message:")
                print(plaintext_hex)
            
            else:
                print("Invalid mode.")
        
        else:
            print("Invalid choice")
        
        print("Enter 1 for encrypting, 2 for decrypting, 3 for breaking, 4 to quit.")
        choice = int(input())
    print("Goodbye")

if __name__ == "__main__":
    main()
