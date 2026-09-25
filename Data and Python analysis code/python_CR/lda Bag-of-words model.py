import gensim
from gensim import corpora
import matplotlib.pyplot as plt
import matplotlib
import warnings
warnings.filterwarnings('ignore')  

from gensim.models.coherencemodel import CoherenceModel
from gensim.models.ldamodel import LdaModel


def prepare_data(path):
    with open(path, encoding='utf-8', errors='ignore') as file:
        file_object2 = file.read().split('\n')  

    data_set = []  
    for line in file_object2:
        result = []
        seg_list = line.split()  
        for word in seg_list:  
            result.append(word)
        data_set.append(result)
    return data_set

def perplexity(num_topics, corpus, dictionary):
    ldamodel = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=30)
    print(ldamodel.print_topics(num_topics=num_topics, num_words=15))
    print(ldamodel.log_perplexity(corpus))
    return ldamodel.log_perplexity(corpus)

def coherence(num_topics, corpus, dictionary, data_set):
    ldamodel = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=30, random_state=1)
    print(ldamodel.print_topics(num_topics=num_topics, num_words=10))
    ldacm = CoherenceModel(model=ldamodel, texts=data_set, dictionary=dictionary, coherence='c_v')
    print(ldacm.get_coherence())
    return ldacm.get_coherence()

if __name__ == '__main__':
    PATH = 'Clean up comments.txt'  
    data_set = prepare_data(PATH)

   
    dictionary = corpora.Dictionary(data_set)  
    corpus = [dictionary.doc2bow(text) for text in data_set]

    
    x = range(1, 15)
    z=[perplexity(i, corpus, dictionary) for i in x]
    #y = [coherence(i, corpus, dictionary, data_set) for i in x]
    plt.plot(x, z)
    plt.xlabel('Number of themes')
    plt.ylabel('Degree of confusion (perplexity)')
    plt.rcParams['font.sans-serif'] = ['SimHei']  
    matplotlib.rcParams['axes.unicode_minus'] = False
    plt.title('The number of topics and the degree of confusion (perplexity) Change relationship')
    plt.show()