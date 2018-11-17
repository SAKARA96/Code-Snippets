# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 19:25:25 2018

@author: Sarvesh
"""

def rhymes(self,a,b):
        
    """Check if two given words rhyme with each other based on syllables extracted using
    NLTK library"""
    
    a=a.lower()
    b=b.lower()
    if(a in self._words): ##check if A is in the dict
        checkA=1
        soundA=self._pronun[a]
        lenA=len(soundA)
        #print(soundA)
    else :
        return False
    if(b in self._words): ##check if B is in dict
        checkB=1
        soundB=self._pronun[b]
        lenB=len(soundB)
        #print(soundB)
    else:
        return False
        
    if((checkA==1) and (checkB==1)): ##if both in dict then move ahead
        #print(lenA,lenB)
        
        for countA in range(lenA):
            if soundA[countA][0][0] not in ['A','E','I','O','U']:
                soundA[countA]=soundA[countA][1:]

        for countA in range(lenA):
            soundA[countA]=''.join(soundA[countA])
            
       # print(soundA)
        

        for countB in range(lenB):
            if soundB[countB][0][0] not in ['A','E','I','O','U']:
                soundB[countB]=soundB[countB][1:]

        for countB in range(lenB):
            soundB[countB]=''.join(soundB[countB])

        #print(soundB)
        
    else:
        return False

    rhyme_count=0
    
    for countA in range(lenA):
        for countB in range(lenB):
            if((soundA[countA].endswith(soundB[countB]))==True):
                #print('substring matched')
                rhyme_count=rhyme_count+1

    for countB in range(lenB):
        for countA in range(lenA):
            if((soundB[countB].endswith(soundA[countA]))==True):
                #print('substring matched')
                rhyme_count=rhyme_count+1
               
    if(rhyme_count>0):
               #print('True') 
               return True
    else:
           # print('False')
            return False