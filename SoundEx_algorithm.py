# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 19:30:44 2018

@author: Sarvesh
"""

from fst import FST
import string, sys
from fsmutils import composechars, trace

def letters_to_numbers():
    """
    Returns an FST that converts letters to numbers as specified by
    the soundex algorithm
    """
    
    # Let's define our first FST
    f1 = FST('soundex-generate')
    char_removal=['a','e','h','i','o','u','w','y','A','E','I','O','U','W','Y']
    char_replace1=['b','f','p','v','B','F','P','V']
    char_replace2=['c','g','j','k','q','s','x','z','C','G','J','K','Q','S','X','Z']
    char_replace3=['d','t','D','T']
    char_replace4=['l','L']
    char_replace5=['m','n','M','N']
    char_replace6=['r','R']

    #indicate all the states
    f1.add_state('start')
    f1.add_state('next')
    f1.add_state('rp1')
    f1.add_state('rp2')
    f1.add_state('rp3')
    f1.add_state('rp4')
    f1.add_state('rp5')
    f1.add_state('rp6')

    #indicate the initial and final state
    f1.initial_state='start'
    f1.set_final('next')
    f1.set_final('rp1')
    f1.set_final('rp2')
    f1.set_final('rp3')
    f1.set_final('rp4')
    f1.set_final('rp5')
    f1.set_final('rp6')

    #Add the arcs    
    for letter in char_removal:
        f1.add_arc('start','next',(letter),(letter))
        f1.add_arc('next','next',(letter),())
        
    for letter in char_replace1:
        f1.add_arc('start','rp1',(letter),(letter))
        f1.add_arc('next','rp1',(letter),('1'))
        f1.add_arc('rp1','rp1',(letter),())
        for letter in char_removal:
            f1.add_arc('rp1','rp1',(letter),())
        for letter in char_replace2:
            f1.add_arc('rp1','rp2',(letter),('2'))
        for letter in char_replace3:
            f1.add_arc('rp1','rp3',(letter),('3'))
        for letter in char_replace4:
            f1.add_arc('rp1','rp4',(letter),('4'))
        for letter in char_replace5:
            f1.add_arc('rp1','rp5',(letter),('5'))
        for letter in char_replace6:
            f1.add_arc('rp1','rp6',(letter),('6'))
        ##end of rp1 to all rp6 connections
            
    for letter in char_replace2:
        f1.add_arc('start','rp2',(letter),(letter))
        f1.add_arc('next','rp2',(letter),('2'))
        f1.add_arc('rp2','rp2',(letter),())
        for letter in char_removal:
            f1.add_arc('rp2','rp2',(letter),())
        for letter in char_replace1:
            f1.add_arc('rp2','rp1',(letter),('1'))
        for letter in char_replace3:
            f1.add_arc('rp2','rp3',(letter),('3'))
        for letter in char_replace4:
            f1.add_arc('rp2','rp4',(letter),('4'))
        for letter in char_replace5:
            f1.add_arc('rp2','rp5',(letter),('5'))
        for letter in char_replace6:
            f1.add_arc('rp2','rp6',(letter),('6'))
        ##end of rp2 to all rp6 connections

    for letter in char_replace3:
        f1.add_arc('start','rp3',(letter),(letter))
        f1.add_arc('next','rp3',(letter),('3'))
        f1.add_arc('rp3','rp3',(letter),())
        for letter in char_removal:
            f1.add_arc('rp3','rp3',(letter),())
        for letter in char_replace1:
            f1.add_arc('rp3','rp1',(letter),('1'))
        for letter in char_replace2:
            f1.add_arc('rp3','rp2',(letter),('2'))
        for letter in char_replace4:
            f1.add_arc('rp3','rp4',(letter),('4'))
        for letter in char_replace5:
            f1.add_arc('rp3','rp5',(letter),('5'))
        for letter in char_replace6:
            f1.add_arc('rp3','rp6',(letter),('6'))
        ##end of rp3 to all rp6 connections    

    for letter in char_replace4:
         f1.add_arc('start','rp4',(letter),(letter))
         f1.add_arc('next','rp4',(letter),('4'))
         f1.add_arc('rp4','rp4',(letter),())
         for letter in char_removal:
            f1.add_arc('rp4','rp4',(letter),())
         for letter in char_replace1:
            f1.add_arc('rp4','rp1',(letter),('1'))
         for letter in char_replace2:
            f1.add_arc('rp4','rp2',(letter),('2'))
         for letter in char_replace3:
            f1.add_arc('rp4','rp3',(letter),('3'))
         for letter in char_replace5:
            f1.add_arc('rp4','rp5',(letter),('5'))
         for letter in char_replace6:
            f1.add_arc('rp4','rp6',(letter),('6'))
        ##end of rp4 to all rp6 connections

    for letter in char_replace5:
        f1.add_arc('start','rp5',(letter),(letter))
        f1.add_arc('next','rp5',(letter),('5'))
        f1.add_arc('rp5','rp5',(letter),())
        for letter in char_removal:
            f1.add_arc('rp5','rp5',(letter),())
        for letter in char_replace1:
            f1.add_arc('rp5','rp1',(letter),('1'))
        for letter in char_replace2:
            f1.add_arc('rp5','rp2',(letter),('2'))
        for letter in char_replace3:
            f1.add_arc('rp5','rp3',(letter),('3'))
        for letter in char_replace4:
            f1.add_arc('rp5','rp4',(letter),('4'))
        for letter in char_replace6:
            f1.add_arc('rp5','rp6',(letter),('6'))
        ##end of rp5 to all rp6 connections

    for letter in char_replace6:
        f1.add_arc('start','rp6',(letter),(letter))
        f1.add_arc('next','rp6',(letter),('6'))
        f1.add_arc('rp6','rp6',(letter),())
        for letter in char_removal:
            f1.add_arc('rp6','rp6',(letter),())
        for letter in char_replace1:
            f1.add_arc('rp6','rp1',(letter),('1'))
        for letter in char_replace2:
            f1.add_arc('rp6','rp2',(letter),('2'))
        for letter in char_replace3:
            f1.add_arc('rp6','rp3',(letter),('3'))
        for letter in char_replace4:
            f1.add_arc('rp6','rp4',(letter),('4'))
        for letter in char_replace5:
            f1.add_arc('rp6','rp5',(letter),('5'))

        ##end of rp6 to all rp6 connections
    
    
                    
        
    return f1


def truncate_to_three_digits():
    """
    Create an FST that will truncate a soundex string to three digits
    """

    # Ok so now let's do the second FST, the one that will truncate
    # the number of digits to 3
    f2 = FST('soundex-truncate')

    # Indicate initial and final states
    f2.add_state('1')
    f2.add_state('2')
    f2.add_state('3')
    f2.add_state('4')
    f2.initial_state = '1'
    f2.set_final('1')
    f2.set_final('2')
    f2.set_final('3')
    f2.set_final('4')

    # Add the arcs
    for letter in string.letters:
        f2.add_arc('1', '1', (letter), (letter))

    for n in range(10):
        f2.add_arc('1','2', (str(n)),(str(n)))
        f2.add_arc('2','3',(str(n)),(str(n)))
        f2.add_arc('3','4',(str(n)),(str(n)))
        f2.add_arc('4','4',(str(n)),())
        
        
        

    return f2

    # The above stub code doesn't do any truncating at all -- it passes letter and number input through
    # what changes would make it truncate digits to 3?


def add_zero_padding():
    # Now, the third fst - the zero-padding fst
    f3 = FST('soundex-padzero')

    f3.add_state('1')
    f3.add_state('1a')
    f3.add_state('1b')
    f3.add_state('2')
    
    f3.initial_state = '1'
    f3.set_final('2')

    for letter in string.letters:
        f3.add_arc('1', '1', (letter), (letter))
    for number in xrange(10):
        f3.add_arc('1', '1a', (str(number)), (str(number)))
        f3.add_arc('1a', '1b', (str(number)), (str(number)))
        f3.add_arc('1b', '2', (str(number)), (str(number)))
        
    f3.add_arc('1','2',(),('000'))
    f3.add_arc('1a','2',(),('00'))
    f3.add_arc('1b','2',(),('0'))

    
    return f3

    # The above code adds zeroes but doesn't have any padding logic. Add some!


if __name__ == '__main__':
    user_input = raw_input().strip()
    f1 = letters_to_numbers()
    f2 = truncate_to_three_digits()
    f3 = add_zero_padding()

    if user_input:
        print("%s -> %s" % (user_input, composechars(tuple(user_input),f1,f2,f3)))
