#!/usr/bin/env python
"""mapper.py"""
import pip
import sys
import re
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    #remove urls
    line = re.sub(r'http\S+', '', line)
    # replace 't  by t
    line = re.sub(r"'t",'t',line)
    #remove puntuation
    line = re.sub(r'[^\w\s]',' ',line)
    # split the line into words
    words = line.split()

    stopwords = ['about', 'all', 'along', 'also', 'an', 'any', 'and', 'are', 'around', 'after', 'according', 'another',
                'already', 'because', 'been', 'being', 'but', 'become', 'can', 'could', 'called',
                'during', 'do', 'dont', 'does', 'doesn', 'did', 'didnt', 'etc', 'for', 'from', 'far',
                'get', 'going', 'had', 'has', 'have', 'he', 'her', 'here', 'him', 'his', 'how',
                'into', 'isnt', 'its', 'just', 'let', 'like', 'may', 'more', 'must', 'most', 
                'not', 'now', 'new', 'next', 'one', 'other', 'our', 'out', 'over', 'own', 'put', 'right', 
                'say', 'said', 'should', 'she', 'since', 'some', 'still', 'such', 
                'take', 'that', 'than', 'the', 'their', 'them', 'then', 'there', 'these',
                'they', 'this', 'those', 'through', 'time', 'told', 'thing', 
                'use' ,'until', 'via', 'very', 'under',
                'was', 'way', 'were', 'what', 'which', 'when', 'where', 'who', 'why', 'will', 'with', 'would', 'wouldnt', 
                'yes', 'you', 'your', 'file', 'files','pdf', 'bedroom', 'replied',  'ago', 'home', 'report', 'doc', 'day',
                'com', 'comment', 'comments', 'reply', 'people', 'says', 'ceo', 'glass', 'ideas', 'year', 'years', 'fri',
                'furniture', 'smartphone','media', 'email', 'manual', 'short', 'description','bed', 'service', 'guide', 
                'repair', 'book', 'edit', 'free', 'money', 'top', 'share', 'thu', 'video', 'only', 'read', 'post', 'local',
                'iphones', 'many', 'edition', 'study', 'first', 'life', 'work', 'school', 
                'series',  'two','des' ,'owners' ,'les' , 'online' ,'system', 'know', 'english', 
                'see', 'available' ,'even' ,'well' ,'workshop' ,'center' ,'women' ,'part' ,'good' ,'family' ,'kitchen' ,
                'science' ,'last' ,'back' ,'office' ,'services' ,'health']
    # increase counters
    for word in words:
        word = word.strip().lower();
        # Stemming
        #word = ps.stem(word)
        if (word.isdigit() or len(word)<=2 or word in stopwords):
            continue
        print '%s\t%s' % (word, 1)