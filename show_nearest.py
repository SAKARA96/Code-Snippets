# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 19:32:58 2018

@author: Sarvesh
"""

def show_nearest(word_2_vec, w_vec, exclude_w, sim_metric):
    #word_2_vec: a dictionary of word-context vectors. The vector could be a sparse (dictionary) or dense (numpy array).
    #w_vec: the context vector of a particular query word `w`. It could be a sparse vector (dictionary) or dense vector (numpy array).
    #exclude_w: the words you want to exclude in the responses. It is a set in python.
    #sim_metric: the similarity metric you want to use. It is a python function
    # which takes two word vectors as arguments.

    # return: an iterable (e.g. a list) of up to 10 tuples of the form (word, score) where the nth tuple indicates the nth most similar word to the input word and the similarity score of that word and the input word
    # if fewer than 10 words are available the function should return a shorter iterable
    #
    # example:
    #[(cat, 0.827517295965), (university, -0.190753135501)]
    #dictionary as first input
    
    ## TODO: delete this line and implement me
    sim=0
    ans=[]
    final=[]
    for key,value in word_2_vec.items():
        t_dict={}
        t_dict=word_2_vec[key]
        sim=sim_metric(w_vec,t_dict)
        ans.append([key,sim])
    for w in ans:
        if w[0] not in exclude_w:
            final.append(w)
    final.sort(key=lambda x: x[1], reverse=True)
    if len(final)>10:
        return final[0:10]
    else:
        return final