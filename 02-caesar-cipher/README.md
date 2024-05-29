# Caesar Cipher Program

## Introduction

The [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher) is one of the simplest and most well-known encryption techniques. Named after Julius Caesar, who used it in his private correspondence, the Caesar cipher works by shifting each letter of the plaintext by a fixed number of positions down the alphabet. Despite its historical significance, the Caesar cipher is easy to break and primarily serves as an educational tool to introduce the concept of encryption.

This program is a simplified version of the Caesar cipher. It allows users to both encrypt and decrypt messages by shifting the letters by a user-defined number of positions.

## Prerequisites

- [Python 3.12](https://www.python.org/downloads/) installed on your system.

## Description

This program lets you encrypt or decrypt a message using the Caesar cipher technique. You can specify the direction (`encode` for encryption, `decode` for decryption), the text to be processed, and the shift number. The program supports repeated use, allowing you to continue encrypting or decrypting messages until you decide to exit.

## How the Code Works

1. **Input**: The user provides the direction (`encode` or `decode`), the message text, and the shift number.
1. **Processing**: The program processes each character in the text:
   - It shifts each letter by the specified number of positions in the alphabet.
   - Non-alphabetic characters remain unchanged.
1. **Output**: The encrypted or decrypted text is displayed.
1. **Repeat**: The user can choose to run the program again with new inputs.

## How to Run the Code

1. **Open Terminal**
1. **Navigate to the Directory**:

   - Use the `cd` command to navigate to the directory where you saved `main.py`. For example:

     ```sh
     cd path/to/your/directory
     ```

1. **Run the Program**:

     ```sh
     python3 main.py
     ```

1. **Follow the Prompts**:

   - The program will prompt you to enter the direction (`encode` to encrypt, `decode` to decrypt), your message text, and the shift number.
   - After processing the input, the program will display the encrypted or decrypted text.
   - You will be asked if you want to run the program again. Type `yes` to continue or `no` to exit.

## Example Usage

```sh
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello
Type the shift number:
3
The encoded text is khoor
Type 'yes' if you want to go again. Otherwise type 'no'.
yes
Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
khoor
Type the shift number:
3
The decoded text is hello
Type 'yes' if you want to go again. Otherwise type 'no'.
no
Goodbye!
```

Enjoy exploring this classic encryption technique!
