from nltk.book import *
text1
text2
text1.concordance("monstrous")
text1.similar("monstrous")
text2.common_contexts(["monstrous","very"])
text4.dispersion_plot(["citzens","democracy","freedom","duties","America"])
text1.concordance("monstrous")
len(text1)
len(text3)
sorted(set(text3))
len(set(text3))
len(text3)/len(set(text3))
text3.count("smote")
100*text4.count("a")/len(text4)
def lexical_diversity(text):
    return len(text)/len(set(text))

def percentage(count, total):
    return 100 * count / total

lexical_diversity(text3)
lexical_diversity(text5)
percentage(text4.count("a"), len(text4))
###
### BKL 1.2 p10 skip to 
### BKL 1.3 p 16
##
saying = ['After','all','is', 'said', 'and', 'done',
'more', 'is', 'sai', 'than', 'done']
tokens = set(saying)
### set() is not a list - make into list to index
list(tokens)
###
### BKL 1.3 p17
###
fdist = FreqDist(text1)
fdist
fdist1 = FreqDist(text1)
vocabulary1 = fdist.keys()
### vocabulary1 not a list - make it into one
list(vocabulary1)
vocabulary1[:50]
fdist1['whale']
fdist1.plot(50, cumulative=True)
###
### BKL 1.3 p20
###
text4.collocations()
text8.collocations()
###
### BKL now considers gooping, fdist.keys, fdist.items(), fdist.freq(n)
### BKL 1.4 p 22 conditinals (.is...), nested code blocks
### BKL 1.5 p 27 disambiguation, pronoun resolution, language output,
### machine translation, spoken dialog, entialment, limitation
###
