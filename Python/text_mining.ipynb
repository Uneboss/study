import pandas as pd
from konlpy.tag import Komoran
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from pyclustering.cluster import kmedoids
import numpy as np
import re
from gensim import corpora, models
import gensim

komo = Komoran()
Data = pd.read_excel('corona19.xlsx')

Data.tail()

contents = []
for i in Data['contents']:
    contents.append(i)
contents

def cleansing(text):
    pattern = '([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)' # E-mail주소제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '(http|ftp|https)://(?:[-\w.]|(?:%[\da-fA-F]{2}))+' # URL제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '([ㄱ-ㅎㅏ-ㅣ]+)' # 한글 자음, 모음 제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '<[^>]*>'         # HTML 태그 제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '[^\w\s]' # 특수기호제거
    text = re.sub(pattern=pattern, repl='', string=text)
    return text  
    
clean_contents = []
for text in contents:
    a = cleansing(str(text))
    clean_contents.append(a)
clean_contents

dictionary = corpora.Dictionary(nouns)

print(dictionary)

corpus = [dictionary.doc2bow(text) for text in nouns]

print(corpus)

ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=3, id2word = dictionary)

ldamodel.print_topics(num_words=10)

NUM_TOPICS = 3 #3개의 토픽, k=3
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = NUM_TOPICS, id2word=dictionary, passes=15)
topics = ldamodel.print_topics(num_words=5)
for topic in topics:
    print(topic)
    
for idx, topic in ldamodel.show_topics(formatted=False, num_words= 10):
    print('Topic: {} \nWords: {}'.format(idx, [w[0] for w in topic]))
    
ldamodel.get_document_topics(corpus)[5]

from gensim.models import CoherenceModel

print('\nPerplexity: ', ldamodel.log_perplexity(corpus))
coherence_model_lda = CoherenceModel(model=ldamodel, texts=nouns, dictionary=dictionary,topn=10)
coherence_lda = coherence_model_lda.get_coherence()
print('\nCoherence Score: ', coherence_lda)

import matplotlib.pyplot as plt

perplexity_values = []
for i in range(2,10):
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=i, id2word = dictionary)
    perplexity_values.append(ldamodel.log_perplexity(corpus))
    
x = range(2,10)
plt.plot(x, perplexity_values)
plt.xlabel("Number of topics")
plt.ylabel("Perplexity score")
plt.show()

coherence_values = []
for i in range(2,10):
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=i, id2word = dictionary)
    coherence_model_lda = CoherenceModel(model=ldamodel, texts=nouns, dictionary=dictionary,topn=10)
    coherence_lda = coherence_model_lda.get_coherence()
    coherence_values.append(coherence_lda)
    
x = range(2,10)
plt.plot(x, coherence_values)
plt.xlabel("Number of topics")
plt.ylabel("coherence score")
plt.show()

import pyLDAvis.gensim as gensimvis

ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=6, id2word = dictionary)
prepared_data = gensimvis.prepare(ldamodel, corpus, dictionary)

import pyLDAvis
import pyLDAvis.gensim  # don't skip this

pyLDAvis.display(prepared_data)

import matplotlib.pyplot as plt
%matplotlib inline
import pandas as pd
import seaborn as sns

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

fiz=plt.figure(figsize=(12,24))
for i in range(6):
    df=pd.DataFrame(ldamodel.show_topic(i), columns=['term','prob']).set_index('term')
#     df=df.sort_values('prob')
    
    plt.subplot(5,2,i+1)
    plt.title('topic '+str(i+1))
    sns.barplot(x='prob', y=df.index, data=df, label='Cities', palette='Reds_d')
    plt.xlabel('probability')
    
plt.show()
