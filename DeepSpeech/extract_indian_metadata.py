import pandas as pd

sentences = []
df = pd.read_csv('dev.tsv',sep='\t')
for index,row in df.iterrows():
    if(row['accent']=='indian'):
        sentences.append(str(row['sentence']) +","+ str(row['path']))
       

print("dev.tsv")

sentences_invalidated=[]
df_invalidated = pd.read_csv('invalidated.tsv',sep='\t')
for index,row in df_invalidated.iterrows():
    if(row['accent']=='indian'):
        sentences_invalidated.append(str(row['sentence']) +","+ str(row['path']))
 
print("invalidated.tsv")

sentences_other=[]

df_other = pd.read_csv('other.tsv',sep='\t')
for index,row in df_other.iterrows():
    if(row['accent']=='indian'):
        sentences_other.append(str(row['sentence']) +","+ str(row['path']))

print("other.tsv")


sentences_test=[]

df_test = pd.read_csv('test.tsv',sep='\t')
for index,row in df_test.iterrows():
    if(row['accent']=='indian'):
        sentences_test.append(str(row['sentence']) +","+ str(row['path']))

print("test.tsv")



sentences_train=[]

df_train = pd.read_csv('train.tsv',sep='\t')
for index,row in df_train.iterrows():
    if(row['accent']=='indian'):
        sentences_train.append(str(row['sentence']) +","+ str(row['path']))

print("train.tsv")

sentences_validated=[]

df_validated = pd.read_csv('validated.tsv',sep='\t')
for index,row in df_validated.iterrows():
    if(row['accent']=='indian'):
        sentences_validated.append(str(row['sentence']) +","+ str(row['path']))

print("validated.tsv")
# print(sentences_validated)


sentences_indian = set(sentences).union(set(sentences_invalidated),set(sentences_other),set(sentences_test),set(sentences_train),set(sentences_validated))



# import os
# import shutil
with open("indiandata.csv", "a") as writefile:
	for i in sentences_indian:
		writefile.write(i + "\n")

