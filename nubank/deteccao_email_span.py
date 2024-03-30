#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getSpamEmails' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY subjects
#  2. STRING_ARRAY spam_words
#

def getSpamEmails(subjects, spam_words):
    # Escreva seu código aqui
    
    #O(n) 
    arr_spans = []
    spam_words_set = set([word.lower() for word in spam_words]) # Converte spam_words para set para busca O(1)
    
    for subject in subjects:
        subject_words = subject.lower().split()
        spam_count = sum([1 for word in subject_words if word in spam_words_set]) # Conta palavras de spam no assunto
        
        # É spam se tiver pelo menos duas palavras de spam ou uma palavra de spam aparecer mais de uma vez
        if spam_count >= 2:
            arr_spans.append('spam')
        else:
            arr_spans.append('not_spam')
    
    return arr_spans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    subjects_count = int(input().strip())

    subjects = []

    for _ in range(subjects_count):
        subjects_item = input()
        subjects.append(subjects_item)

    spam_words_count = int(input().strip())

    spam_words = []

    for _ in range(spam_words_count):
        spam_words_item = input()
        spam_words.append(spam_words_item)

    result = getSpamEmails(subjects, spam_words)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
