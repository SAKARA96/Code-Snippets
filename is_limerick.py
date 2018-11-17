# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 19:26:50 2018

@author: Sarvesh
"""

def is_limerick (self,text):
    
        """Given an input text, check if the constrained rhyming scheme 
        followed by the text is: ABABA
        """
        text=text.lower()
        text=text.strip()
        text=''.join(ch for ch in text if ch not in self._punctuations)
        print(text)

        lines=text.split('\n')
        print (lines)
        
        
        if(len(lines)<5):
            print ('False')
            return False
            

        Tword=['']*len(lines)
        Lword=['']*len(Tword)
        for i in range(len(lines)):
            Tword[i]=word_tokenize(lines[i])
            Lword[i]=Tword[i][len(Tword[i])-1]

        print (Tword)
        print(Lword)
        
        NumS=[0]*len(Lword)
        
        for i in range(len(Tword)):   ##count the syllables in each line
            for j in range(len(Tword[i])):
                NumS[i]=NumS[i]+self.num_syllables(Tword[i][j])
        print(NumS)        

        for i in range(len(NumS)):
            if (NumS[i]<4):
                print('No Limerick')
                break
                return False
                
            
        if(((abs(NumS[0]-NumS[1])>2) or (abs(NumS[1]-NumS[4])>2) or (abs(NumS[0]-NumS[4])>2)) or (abs(NumS[2]-NumS[3])>2) or (NumS[2]-min(NumS[0],NumS[1],NumS[4])>0) or (NumS[3]-min(NumS[0],NumS[1],NumS[4])>0)):
             
             return False
            

        if((self.rhymes(Lword[0],Lword[1])) and (self.rhymes(Lword[1],Lword[4])) and (self.rhymes(Lword[0],Lword[4])) and (self.rhymes(Lword[2],Lword[3]))): 
            if( (self.rhymes(Lword[0],Lword[2])) or (self.rhymes(Lword[1],Lword[2])) or (self.rhymes(Lword[4],Lword[2])) or (self.rhymes(Lword[0],Lword[3])) or (self.rhymes(Lword[1],Lword[3])) or (self.rhymes(Lword[4],Lword[3]))):
                print('No Limerick')
                
                return False
                
            else:
                print('Yes Limerick')
                
                return True
                
        else:
            
            return False