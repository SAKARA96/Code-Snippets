# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 19:24:03 2018

@author: Sarvesh
"""

 def num_syllables(self,word):
     
     """Function implemented to get the syllables of a given word using NLTK
        library"""
    
    if(word in self._words):
            #print(self._pronun[word])
            count=[0]*len(self._pronun[word])
            #print(count)
            pos=0  
            for w in (self._pronun[word]):
                      #print(w)
                      for i in w :
                          for char in i:
                              if(char.isdigit()):
                                  count[pos]=count[pos]+1
                      #print(count[pos])
                      pos=pos+1

            #print(count)
            #print(min(count))
            return(min(count))
 
    else :
        #print('1')
        return 1