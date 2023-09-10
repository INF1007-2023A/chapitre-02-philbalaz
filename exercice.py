#!/usr/bin/env python
# -*- coding: utf-8 -*-

def majuscule(mot):
    j = 0
    nouveau_mot = str("")
    while j < len(mot):
        le = chr(ord(mot[j])-32)
        nouveau_mot += le
        j += 1
    mot = nouveau_mot
    return mot


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
