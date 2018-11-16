# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 17:24:06 2018

@author: Sarvesh
"""
import numpy as np

def viterbi_seq_score(Em,Tran,S,E):
    """Function to implement Viterbi algorithm which returns the max score of the
    highest possible sequence along with the sequence
    N: Number of the inputs
    L: Number of the states
    
    Em: emission scores N*L matrix
    Tran: Transisition scores L*L matrix
    S:  Start scores of all the states 1*L matrix
    E: End scores of all the states 1*L matrix  
    """
    
    N=Em.shape[0]
    L=S.shape[0]
    table=np.zeros((N+1,L))
    back=np.zeros((N+1,L))
    for i in range(N+1):
        for j in range(L):
            if i==0:
                table[i,j]=S[j]+Em[i,j]
                back[i,j]=j
            if i>=1 and i<N:
                table[i,j]=Em[i][j]+max(Tran[:,j]+table[i-1,:])
                back[i,j]=(Tran[:,j]+table[i-1,:]).argmax()
            if i==N:
                table[i,j]=table[i-1,j]+E[j]
                
    seq=[]           
    seq.append(table[N].argmax())
    prev=int(table[N].argmax())    
    for i in reversed(range(N)):
        seq.append(int(back[i,prev]))
        prev=int(back[i,prev])
    
    seq=seq[:len(seq)-1]
    seq.reverse()
    
    return(max(table[N,:]),seq)