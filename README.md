# caesar-cipher
This repository is for a Python implementation of a Caesar cipher.
When run, the user is given the option to encrypt, decrypt, or break. The cipher is implemented at the byte level.

## Encryption
When encrypting, the user is expected to enter a standard ASCII encoded string.
It also asks for a number to shift the bytes by. Any integer is acceptable.
After performing the shift, the bytes are then output as a hex string to account for shifts that create non-ASCII values.

## Decryption
When decrypting, the user is expected to enter a hex string since the encryption resulted in a hex string.
When entering the shift, the user should enter the shift used to encrypt it, as the code handles reversing it.
After performing the shift, the bytes are now output as a standard, readable ASCII string.

## Breaking
Breaking the cipher is based on frequency analysis. I created a dictionary mapping each letter to its frequency in English.
I then created one using the corresponding byte for each letter. When breaking a given hex coded string, all 256 possible shifts are attempted.
Each attempt is scored. The scorer evaluates each byte, punishing those that are non-ASCII values and those that are unprintable ASCII values.
The rest add to the score based off their frequency. To account for cases, each byte is normalized to lowercase.
The attempt with the highest score is the one chosen.

## Usage
python caesar.py
Enter 1 for encrypting, 2 for decrypting, 3 for breaking, 4 to quit.

1

What message would you like to encrypt? the quick brown fox jumps over the lazy dog

Enter your desired shift: 7

Encrypted message (hex):

7b6f6c27787c706a72276979767e75276d767f27717c74777a27767d6c79277b6f6c2773688180276b766e
