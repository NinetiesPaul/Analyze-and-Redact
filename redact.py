# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 14:08:13 2018

@author: Paul Richard
"""

def redact():
    text = "Lorem ipsum elit quam semper potenti eleifend dapibus magna feugiat, fames amet vestibulum interdum gravida praesent porta nec, sem mattis consectetur per senectus vestibulum curae iaculis. sodales etiam leo volutpat id bibendum varius senectus cubilia, id rutrum taciti class placerat praesent augue, fusce sit eleifend non blandit aenean scelerisque. ultricies risus augue libero sollicitudin donec enim ipsum sollicitudin quis urna, duis habitasse sociosqu feugiat mi ac porta congue massa etiam maecenas, curae turpis mattis nibh hendrerit iaculis platea elit feugiat. donec curabitur quam maecenas cubilia dictumst nec bibendum, a gravida odio gravida nisl integer, curabitur tincidunt nisl aptent donec sapien."
    
    print("Original size: "+str(len(text)))
    
    signs = [',', '.', '\n']
    
    for sign in signs:
        text = text.replace(sign, "")
    
    print("Sanitized size: "+str(len(text)))
    
    text = text.lower()
    
    original_text = text
    
    text2 = text.replace(' ', '')
    
    letters_dict = {}
    
    for char in text2:
        if char not in letters_dict.keys():
            letters_dict[char]=0
        letters_dict[char]+=1
    
    text = text.split(" ")
    
    words_dict = {}
    
    for word in text:
        if word not in words_dict.keys():
            words_dict[word]=0
        words_dict[word]+=1
        
    print("Number of single words: "+str(len(words_dict.keys())))
    print("Total number of words: "+str(sum(words_dict.values())))
        
    print("Number of single letters: "+str(len(letters_dict.keys())))
    print("Total number of letters: "+str(sum(letters_dict.values())))
    
    print("Current list of words:\n")
    print(list(words_dict.keys()))
    
    redact_words = []
    
    redact = ''
    
    print("Type words to be redacted: ")
    
    while redact != "ok":
        redact = input()
        redact = redact.lower()
        if redact == "ok":
            print("Got it!")
        elif redact not in words_dict:
            print("That word is not on the dictionary!")
            pass
        else:
            redact_words.append(redact)
    
    redacted_text = ''
    
    for word in text:
        if word in redact_words:
            redacted_text += "[REDACTED]"
        else:
            redacted_text += word
        redacted_text += " "
        
    print("Original version:")
    print(original_text)
    print()
    print("Redacted version:")
    print(redacted_text)