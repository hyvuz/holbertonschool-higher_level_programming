#!/usr/bin/python3
def multiple_returns(sentence):
    sen_length = len(sentence)
    
    if sen_length == 0:
        my_tuple = (sen_length, None)  
    else:
        my_tuple = (sen_length, sentence[0])
        
    return my_tuple
