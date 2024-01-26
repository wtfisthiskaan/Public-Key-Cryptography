#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 03:17:48 2024

@author: kaanuslu
"""

import math
import random
from sympy import mod_inverse

def lambdaGenerator(p1,q1,p2,q2,a,b,p):
    if(p1==p2 and q1==q2):
        l=((3*(p1**2)+a)*mod_inverse(2*q1,p))%p #derivative of the elliptic curve equation to draw line. Derivative = 3x^2 + a
    else:
        l=((q2-q1)*mod_inverse(p2-p1,p))%p  # slope's formula = (q₂ - q₁)/(p₂ - p₁). The (1 / (p₂ - p₁)) = modulo inverse of point).
    return l

def pointAddition(p1,q1,p2,q2,a,b,p):
    if(p1==0 and q1==0):         #when one point is 0,0
        return p2,q2
    if(p2==0 and q2==0):         #when one point is 0,0
        return p1,q1
    if((q1+q2)%p==0 and p1==p2): #the additive inverse case  P + (−P) = Identity Element (0,0), generally defined as infinite.
        return 0,0
    l=lambdaGenerator(p1,q1,p2,q2,a,b,p)
    p3=(l**2-p1-p2)%p
    q3=(l*(p1-p3)-q1)%p
    return p3,q3


def pointMultiplication(p1,q1,a,b,p,n):
    n = n - 1
    inip1=p1
    iniq1=q1
    while(n>0):
        if(n%2==1):
            p1,q1=pointAddition(p1,q1,inip1,iniq1,a,b,p)
        inip1,iniq1=pointAddition(inip1,iniq1,inip1,iniq1,a,b,p)
        n=n//2
    return p1,q1

def negativeOfPoint(p1,q1,p):
    return p1,-q1%p 

def findPoints(a,b,p):
    points=[]
    for i in range(p):
        for j in range(p):
            if((j**2)%p==((i**3+a*i+b)%p)):
                points.append((i,j))
    return points



def encrypt(plaintext,a,b,p,order,gen,publicKey0,publicKey1,letterToPoint):
    point = letterToPoint[plaintext]
    
    k=random.randint(1,order-1)

    c1 = pointMultiplication(gen[0],gen[1], a, b, p, k)

    p2, q2 = pointMultiplication(publicKey0,publicKey1,a,b,p,k)
    c2 = pointAddition(point[0],point[1],p2,q2,a,b,p)
    
    return c1,c2



def decrypt(c1,c2,p,a,b,order,secretKey, pointToLetter):
    p2,q2 = pointMultiplication(c1[0],c1[1],a,b,p,secretKey)
    p2,q2 = negativeOfPoint(p2,q2,p)

    M = pointAddition(c2[0],c2[1],p2,q2,a,b,p)

    m = pointToLetter[M]

    return m

def keyGenerator(a,b,p,order,gen):
    secretKey=random.randint(1,order-1)
    print("The secret key is ",secretKey)
    publicKey0,publicKey1=pointMultiplication(gen[0],gen[1],a,b,p,secretKey)
    print("The public key is ",publicKey0,publicKey1)
    return (publicKey0,publicKey1), secretKey



# Elliptic curve parameters
a = 101
b = 177
p = 269  # A small prime for demonstration purposes

# Generate a list of points on this curve
points = findPoints(a, b, p)

# Create a mapping between letters and points
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letterToPoint = {alphabet[i]: points[i] for i in range(len(alphabet))}
pointToLetter = {points[i]: alphabet[i] for i in range(len(alphabet))}

# Define a generator point (assuming one of the points on the curve is suitable)
gen = points[0]  # Using the first point as the generator

# Elliptic curve order (a small number for demonstration; not secure)
order = len(points)

# Generate keys (public and private)
public_key, private_key = keyGenerator(a, b, p, order, gen)

public_key, private_key, letterToPoint, pointToLetter, points 




