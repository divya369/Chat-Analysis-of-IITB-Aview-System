import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import re
from nltk.corpus import stopwords
#from collections import defaultdict

'''def word_extraction(sentence):
    ignore = ['a', "the", "is"]
    words = re.sub("[^\w]", " ",  sentence).split()
    cleaned_text = [w.lower() for w in words if w not in ignore]
    return cleaned_text'''



import csv
f = open('new3.txt', 'r+')


filewrite = open("newfile.txt", "w")
filewrite2=open("stopwords.txt","w")

lines = [line for line in f.readlines()]

f.close()
#print(lines)
frequency={}
for data in lines:
     #?words = word_extraction(i)
     #phrases = sent_tokenize(data)

     punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
     data=data.strip("\n")
     words=[]
     words=word_tokenize(data)

     #print(words)
     #print(phrases)

     stopWords = set(stopwords.words('english'))
     filteredWords = []
     stopw=[]

     for i in words:
         i=i.lower()
         for ch in punctuations:
             i.strip(ch)
         if i not in stopWords:
             if i not in punctuations:
                 filteredWords.append(i)
             else:
                 stopw.append(i)
         else:
             stopw.append(i)

     #print(filteredWords)
     abc = " ".join(filteredWords)

     filewrite.write(abc + "\n")

     deg=" ".join(stopw)
     filewrite2.write(deg + "\n")

     # frequency
     for j in filteredWords:
         if j not in frequency:
             frequency[j]=1
         else:
             frequency[j]=frequency[j]+1

'''for i in sorted (frequency) :
    print ((i, frequency[i]), end =" ")
    print("\n")'''

print(sorted(frequency.items(), key=
lambda kv: (kv[1], kv[0])))













