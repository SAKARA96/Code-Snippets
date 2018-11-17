# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 19:32:21 2018

@author: Sarvesh
"""

def cossim_sparse(v1,v2):
    # Take two context-count dictionaries as input
    # and return the cosine similarity between the two vectors.
    # Should return a number beween 0 and 1
    ## TODO: delete this line and implement me
    v1_v2=0
    denv1=0
    denv2=0
    
    if len(v1)>=len(v2):
        for key,v_v1 in v1.items():
            v1_v2+=v_v1*v2.get(key,0)
            denv1+=v_v1*v_v1
        for v_v2 in v2.values():
            denv2+=v_v2*v_v2
        return v1_v2/math.sqrt(denv1*denv2)
    elif len(v2)>len(v1):
        for key,v_v2 in v2.items():
            v1_v2+=v_v2*v1.get(key,0)
            denv2+=v_v2*v_v2
        for v_v1 in v1.values():
            denv1+=v_v1*v_v1    
        return v1_v2/math.sqrt(denv1*denv2)    