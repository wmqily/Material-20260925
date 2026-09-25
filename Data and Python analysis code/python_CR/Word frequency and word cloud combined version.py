import matplotlib.pyplot as plt
import jieba
from collections import Counter

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

stopwords = {'的', '了', '在', '是', '我', '有', '都', '和', '就', '不', '一个', '上', '也', '很', '说', '要', '去',
             '着', '到', '吧', '人', '看', '会', '大', '好', '过', '还', '没', '小', '吗', '下', '都', '点', '太',
             '自己', '再', '这', '那', '个', '些', '里', '得', '把', '从', '很', '最', '但', '又', '么', '之', '去',
             '把', '去', '等', '如果', '可以', '因为', '所以', '什么', '怎么', '为什么', '这样', '只有', '但是', '还是',
             '一样', '什么时候', '怎么样', '不过', '然后', '那么', '哪些', '哪里', '怎样', '现在', '哪些', '哪里',
             '怎样', '其实', '什么', '啦', '应该', '好像', '这么', '起来', '一样', '如果', '只是', '可是', '只有',
             '就是', '已经', '很', '非常', '一些', '有', '没有', '其他', '自己', '，', '。', '你', ' ', '不是', '的',
             '被', '与', '让', '不会', '给', '·', ',', '.', '!', '?', '（', '）', '：', '；', '"', "'", '“', '”', '、', '《',
             '》', ' ', '\n', '\t', '—', '-', '_', '…','买','用','哭','惹','才','啊','他','沈阳','流畅','小院','颖姐','送出','十二','琪琪','黑哥','四叔','其琛'}

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return content

def tokenize(content):
    tokens = jieba.cut(content)
    return [word for word in tokens if word not in stopwords and len(word) == 2]

def word_frequency(tokens):
    return Counter(tokens)

def plot_word_bar_chart(word_freq):
    words = [item[0] for item in word_freq]
    frequencies = [item[1] for item in word_freq]
    plt.figure(figsize=(10, 6))
    plt.bar(words, frequencies, color='skyblue', edgecolor='black', linewidth=1.2)
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Bar chart of word frequency distribution')
    plt.xticks(rotation=45, fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig('Bar chart of word frequency distribution.png')
    plt.show()

def plot_word_pie_chart(word_freq):
    words = [item[0] for item in word_freq]
    frequencies = [item[1] for item in word_freq]
    colors = plt.cm.tab20c(range(len(words)))  
    explode = [0.1 if i == 0 else 0 for i in range(len(words))]  
    plt.figure(figsize=(8, 6))
    plt.pie(frequencies, labels=words, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode)
    plt.title('Pie chart of word frequency distribution')
    plt.savefig('Pie chart of word frequency distribution.png')
    plt.show()

def plot_word_cloud(word_freq):
    from wordcloud import WordCloud
    wordcloud = WordCloud(font_path='simhei.ttf', background_color='white', width=800, height=400).generate_from_frequencies(dict(word_freq))
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud Map')
    plt.savefig('Word Cloud Map.png')
    plt.show()

def main(file_path):
    content = read_file(file_path)
    tokens = tokenize(content)
    word_freq = word_frequency(tokens)
    top_words = word_freq.most_common(10)

    print("Top 10 words by frequency:")
    for word, freq in top_words:
        print(f'{word}: {freq}')

    plot_word_bar_chart(top_words)
    plot_word_pie_chart(top_words)
    plot_word_cloud(word_freq)

if __name__ == '__main__':
    file_path = 'output.txt'  
    main(file_path)