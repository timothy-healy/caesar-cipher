# caesar-cipher
This repository is for a Python implementation of a Caesar cipher.
When run, the user is given the option to encrypt, decrypt, or break. The cipher is implemented at the byte level and on letters only.
For all operations, the user can choose to operate on English text (mode 1) or on hex-encoded bytes (mode 2).

## Encryption
When encrypting, the user is expected to enter a string of letters (no spaces or non-letter characters) in mode 1.
In mode 2, the user is expected to enter a hex-encoded string.
It also asks for a number to shift by. Any integer is acceptable.
After performing the shift, the ciphertext is output as a string of letters in mode 1, and hex in mode 2.

## Decryption
The user is expected to enter the same types as with encrypting.
When entering the shift, the user should enter the shift used to encrypt it (the symmetric key), as the code handles reversing it.
After performing the shift, the plaintext is output as before, standard letters in mode 1, hex in mode 2.

## Breaking
Breaking the cipher is based on frequency analysis. I created a dictionary mapping each letter to its frequency in English.
I then created one using the corresponding byte for each letter.
When breaking a given string of only letters in mode 1, all 26 possible shifts are attempted and scored purely on letter frequency.
When breaking a given hex coded string in mode 2, all 256 possible shifts are attempted.
Each attempt is scored. The scorer evaluates each byte, punishing those that are non-ASCII values and those that are unprintable ASCII values.
The rest add to the score based on their frequency. To account for cases, each byte is normalized to lowercase.
The attempt with the highest score is the one chosen.

## Usage
```
python caesar.py
Enter 1 for encrypting, 2 for decrypting, 3 for breaking, 4 to quit.
1
Operate using regular text (1) or bytes and hex-encodings (2)?
1
What message? thequickbrownfoxjumpedoverthelazydog
Enter your desired shift: 13
Encrypted message:
gurdhvpxoebjasbkwhzcrqbiregurynmlqbt
Enter 1 for encrypting, 2 for decrypting, 3 for breaking, 4 to quit.
1
Operate using regular text (1) or bytes and hex-encodings (2)?
2
What hex-encoded message? 74686520717569636B2062726F776E20666F78206A756D706564206F76657220746865206C617A7920646F67
Enter your desired shift: 13
Encrypted message (hex):
8175722d7e827670782d6f7f7c847b2d737c852d77827a7d72712d7c83727f2d8175722d796e87862d717c74
Enter 1 for encrypting, 2 for decrypting, 3 for breaking, 4 to quit.
4
Goodbye
```
