# data capture
import os

keyword ="FightForHongKong OR HongKongProtest"  

wfile = open(os.getcwd()+"/protests.txt", 'w', -1, 'utf-8') 

# twitter 검색 cursor 선언

cursor = tweepy.Cursor(api.search, q=keyword,
                        #since="2019-12-1",
                        #until="2020-5-1",
                        count=1000,           # 페이지당 반환할 트위터 수 최대 1000
                        #geocode=location,   
                        len="en",
                        include_entities=True)
                        
for i, tweet in enumerate(cursor.items()):

    print("{}: {}".format(i, tweet.text))

    wfile.write(tweet.text + '\n')

wfile.close()

openFileName = 'protests.txt'

f = open(openFileName, 'r', encoding='utf-8')
P_data = f.readlines()
f.close()
P_data

# preprocessing
def clean_tweet(tweet):
    tweets = re.sub('rt[\s]+', '', tweet)
    tweets = re.sub('[0-9]+', ' ', tweets)
    tweets = re.sub('hong kong|Hong Kong|hk|HK|Hong kong', 'hongkong', tweets)
    return ' '.join(re.sub('(@[A-Za-z0-9]+)|([^A-Za-z \t])|(\w+:\/\/\S+)', ' ', tweets).split()) 

def cleaning(data):  
    clean_texts = []
    for text in data:
        word = text.lower()
        a = clean_tweet(word)
        clean_texts.append(a)
    return clean_texts

def erase_RT(data):
    cleaned=cleaning(data)
    texts = []
    for i in cleaned:
        if i not in texts:
            texts.append(i)
    return texts
    
stemmer = SnowballStemmer("english")
stop_words = stopwords.words('english')

def preprocess(data):
    tweets=erase_RT(data)
    cleaned_tokens=[]
    for words in tweets:
        tokens = word_tokenize(words)
        for i in tokens:
            if i not in stop_words:
                word = stemmer.stem(i)
                cleaned_tokens.append(word) 
    return cleaned_tokens
    
prepared_P=preprocess(P_data)

# wordcloud
protests_count = Counter(prepared_P)

wordcloud1 = WordCloud(
    width = 800,
    height = 800
)
wordcloud_P = wordcloud1.generate_from_frequencies(protests_count)
array1 = wordcloud_P.to_array()

def showWordCloud(array): 
    fig = plt.figure(figsize=(10, 10))
    plt.imshow(array, interpolation="bilinear")
    plt.show()
    #fig.savefig('WordCloud.png')
    
showWordCloud(array1)

# frequency graph
def showGraph(wordInfo):
    
    plt.xlabel('words')
    plt.ylabel('frequency')
    plt.grid(True)
    
    Sorted_Dict_Values = sorted(wordInfo.values(), reverse=True)
    Sorted_Dict_Keys = sorted(wordInfo, key=wordInfo.get, reverse=True)

    plt.bar(range(len(wordInfo)), Sorted_Dict_Values, align='center')
    plt.xticks(range(len(wordInfo)), list(Sorted_Dict_Keys), rotation='100')

    plt.show()
    
def bar(count):    
    wordInfo = dict()
    for tags, counts in count.most_common(20):
        if (len(str(tags)) > 1):
            wordInfo[tags] = counts
            print ("%s : %d" % (tags, counts))
    showGraph(wordInfo)    

bar(protests_count)

# Sentimental Analysis
def get_tweet_sentiment(tweet): 
    analysis = TextBlob(tweet) 
    if analysis.sentiment.polarity > 0: 
        return 'positive'
    elif analysis.sentiment.polarity < 0: 
        return 'negative'
        
from textblob import TextBlob
P_ptweets = [tweet for tweet in prepared_P if get_tweet_sentiment(tweet) == 'positive']
P_ntweets = [tweet for tweet in prepared_P if get_tweet_sentiment(tweet) == 'negative']

def drawBar(ptweets, ntweets):
    plt.title('Sentiment Analysis')
    plt.xlabel('Sentiment')
    plt.ylabel('frequency')
    plt.grid(True)

    Sorted_Dict_Values = [len(ptweets), len(ntweets)]
    Sorted_Dict_Keys = ['positive', 'negative']

    plt.bar(range(2), Sorted_Dict_Values, align='center')
    plt.xticks(range(2), list(Sorted_Dict_Keys), rotation='70')

    plt.show()
    
drawBar(P_ptweets, P_ntweets)

# Association Analysis
def countData(data):    
    count = {}   #동시출현 빈도가 저장될 dict
    for words in data:
        tokens = tokenizer.tokenize(words)
        stopped_tokens = [i for i in list(set(tokens)) if not i in stop_words+["br"]]
        stopped_tokens2 = [stemmer.stem(i) for i in stopped_tokens if len(i)>1]
        for i, a in enumerate(stopped_tokens2):
            for b in stopped_tokens2[i+1:]:
                if a>b: 
                    count[b, a] = count.get((b, a),0) + 1  
                else :
                    count[a, b] = count.get((a, b),0) + 1     
    return count
    
Pcount=countData(erase_RT(P_data))

def makeDf(count):    
    df=pd.DataFrame.from_dict(count, orient='index')

    list1=[]
    for i in range(len(df)):
        list1.append([df.index[i][0],df.index[i][1],df[0][i]])

    df2=pd.DataFrame(list1, columns=["term1","term2","freq"])
    print(df2)
    df3=df2.sort_values(by=['freq'],ascending=False)
    df3_pos=df3.reset_index(drop=True)
    return df3_pos
    
P=makeDf(Pcount)

class MakeGraphml:

    def make_graphml(self, pair_file, graphml_file):
        out = open(graphml_file, 'w', encoding = 'utf-8')

        entity = []
        e_dict = {}
        count = []
        for i in range(len(pair_file)):
            e1 = pair_file.iloc[i,0]
            e2 = pair_file.iloc[i,1]
            #frq = ((word_dict[e1], word_dict[e2]),  pair.split('\t')[2])
            frq = ((e1, e2), pair_file.iloc[i,2])
            if frq not in count: count.append(frq)   # ((a, b), frq)
            if e1 not in entity: entity.append(e1)
            if e2 not in entity: entity.append(e2)
        print('# terms: %s'% len(entity))

      
        for i, w in enumerate(entity):
            e_dict[w] = i + 1 # {word: id}

        out.write(
            "<?xml version=\"1.0\" encoding=\"UTF-8\"?><graphml xmlns=\"http://graphml.graphdrawing.org/xmlns\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://graphml.graphdrawing.org/xmlnshttp://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd\">" +
            "<key id=\"d1\" for=\"edge\" attr.name=\"weight\" attr.type=\"double\"/>" +
            "<key id=\"d0\" for=\"node\" attr.name=\"label\" attr.type=\"string\"/>" +
            "<graph id=\"Entity\" edgedefault=\"undirected\">" + "\n")

        # nodes
        for i in entity:
            out.write("<node id=\"" + str(e_dict[i]) +"\">" + "\n")
            out.write("<data key=\"d0\">" + i + "</data>" + "\n")
            out.write("</node>")

        # edges
        for y in range(len(count)):
            out.write("<edge source=\"" + str(e_dict[count[y][0][0]]) + "\" target=\"" + str(e_dict[count[y][0][1]]) + "\">" + "\n")
            out.write("<data key=\"d1\">" + str(count[y][1]) + "</data>" + "\n")
            out.write("</edge>")

        out.write("</graph> </graphml>")
        print('now you can see %s' % graphml_file)

        out.close()

gm = MakeGraphml()

graphml_file = 'HK_P.graphml'
gm.make_graphml(P.iloc[0:(len(np.where(P['freq']>10)[0])),:], graphml_file)
