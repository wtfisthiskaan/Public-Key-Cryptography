#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 03:08:26 2024

@author: kaanuslu
"""

import random
from sympy import isprime, gcd, mod_inverse

def generate_rsa_keys():
    p, q = 0, 0
    while not (isprime(p) and isprime(q)):
        p, q = random.getrandbits(10), random.getrandbits(10)

    n = p * q

    phi = (p - 1) * (q - 1)

    pk = random.randint(2, phi - 1)
    while gcd(pk, phi) != 1:
        pk = random.randint(2, phi - 1)

    sk = mod_inverse(pk, phi)

    return n,sk, pk

def rsa_encrypt(plaintext, public_key, n):
    ciphertext = []
    for char in plaintext:
        cipher_char = pow(ord(char), public_key, n)
        ciphertext.append(cipher_char)
    return ciphertext

def rsa_decrypt(ciphertext, secret_key, n):
    plaintext = ''
    for cipher_char in ciphertext:
        plain_char = pow(cipher_char, secret_key, n)
        plaintext += chr(plain_char)
    return plaintext


plaintext = "TRABZON"

n, sk, pk = generate_rsa_keys()
print(f"Public Key: {pk}, Secret Key: {sk}, n: {n}")

ciphertext = rsa_encrypt(plaintext, pk, n)
print(f"Ciphertext: {ciphertext}")

decrypted_text = rsa_decrypt(ciphertext, sk, n)
print(f"Decrypted Text: {decrypted_text}")



