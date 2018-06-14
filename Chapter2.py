# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(jurkat)s
"""
### BKL 2.1 p 40
###
import nltk
from nltk.corpus import gutenberg
gutenberg.fileids()
emma = nltk.corpus.gutenberg.words('austen-emma.txt')
len(emma)
gutenberg.fileids()
###
### print replaced by pring() function
### .words counts spaces after each word as a character
### pint() statement from updated for Python 3 www.nlt,.org/book/Ch02.html
###
for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
    print(num_chars, num_words, num_sents, num_vocab, round(num_chars/num_words),int(num_words/num_sents),int(num_words/num_vocab),fileid)