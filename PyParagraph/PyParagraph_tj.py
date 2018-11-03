#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 22:32:18 2018

@author: Tao Jin
"""
import numpy as np
import re


def paragraph_analysis(text_para):
    
    waste_char = '()><1234567890!/\?.'
    Sentences = re.split("(?<=[.!?]) +", text_para)
    Sentence_count = len(Sentences)
    
    #Remove the special characters from words:
    for i in range(len(Sentences)):
        for j in range(len(waste_char)):
            Sentences[i] = Sentences[i].replace(waste_char[j],'')
            
            # Words Count and sentence length count:
    words_count = 0
    Sentence_len = []
    words_list = []
    full_words_list = []

  
    for i in range(len(Sentences)):
        for j in range(len(Sentences[i])):
            words_list = Sentences[i].split(' ')
        words_count = words_count + len(words_list)
        Sentence_len.append(len(words_list))
        full_words_list.append(words_list)
        words_list = []
   
    
    Average_Sen_len = round(np.mean(Sentence_len),1)                                 
    
    # Count Letters...
    letter_len = 0 
    for i in range(len(full_words_list)):
        for j in range(len(full_words_list[i])):
            letter_len = letter_len + len(full_words_list[i][j])

    Average_Letter_Count = round(letter_len/words_count,1)
    print('Paragraph Analysis\n-----------------\n')
    print(f'Approximate Word Count: {words_count}')
    print(f'Approximate Sentence Count: {Sentence_count}')
    print(f'Average Letter Count: {Average_Letter_Count}')
    print(f'Average Sentence Length: {Average_Sen_len}')

    return



textfile1 = 'raw_data/paragraph_1.txt'
textfile2 = 'raw_data/paragraph_2.txt'
textfile3 = 'raw_data/test.txt'

paragraph1 = open(textfile1,'r')
paragraph2 = open(textfile2,'r')
paragraph3 = open(textfile3,'r')

text_para1 = paragraph1.read()
text_para2 = paragraph2.read()
text_para3 = paragraph3.read()

print(f'{textfile1}')
paragraph_analysis(text_para1)

print(f'{textfile2}')
paragraph_analysis(text_para2)

print(f'{textfile3}')
paragraph_analysis(text_para3)



    
 











    