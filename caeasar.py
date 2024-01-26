#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 21:59:59 2024

@author: kaanuslu
"""

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caesar_cipher_encrypt(plaintext, key):
    ciphertext = ''

    for char in plaintext:
        index = alphabet.find(char)
        new_index = (index + key) % 26
        ciphertext += alphabet[new_index]

    return ciphertext

def caesar_cipher_decrypt(ciphertext, key):
    plaintext = ''

    for char in ciphertext:
        index = alphabet.find(char)
        new_index = (index - key) % 26
        plaintext += alphabet[new_index]

    return plaintext

# Example usage
plaintext = "TRABZON"
key = 3
encrypted_text = caesar_cipher_encrypt(plaintext, key)
decrypted_text = caesar_cipher_decrypt(encrypted_text, key)

print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)

