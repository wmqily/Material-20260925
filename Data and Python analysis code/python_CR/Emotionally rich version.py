import numpy as np
import matplotlib.pyplot as plt
from snownlp import SnowNLP


def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines if line.strip()]  
    return lines


def analyze_sentiments(source):
    sentimentslist = []
    for content in source:
        s = SnowNLP(content)
        sentimentslist.append(s.sentiments)
    return sentimentslist


def plot_sentiment_line_chart(results):
    plt.figure(figsize=(12, 6))
    plt.plot(np.arange(len(results)), results, marker='o', color='dodgerblue', label='Changes in mood index')
    plt.axhline(y=0, color='gray', linestyle='--', linewidth=1, label='Emotional baseline')
    plt.fill_between(np.arange(len(results)), results, 0, where=(np.array(results) > 0.1), color='lightgreen',
                     alpha=0.5,
                     label='Positive emotion')
    plt.fill_between(np.arange(len(results)), results, 0, where=(np.array(results) < -0.1), color='lightcoral',
                     alpha=0.5,
                     label='Negative emotions')
    plt.fill_between(np.arange(len(results)), results, 0,
                     where=(np.array(results) >= -0.1) & (np.array(results) <= 0.1), color='lightyellow', alpha=0.5,
                     label='Neutral emotion')
    plt.xlabel('Entry number')
    plt.ylabel('Emotion Index [-0.5, 0.5]')
    plt.title('Emotion Analysis line graph - Emotion Fluctuations')
    plt.legend()
    plt.grid(alpha=0.3)
    plt.savefig('Emotion Analysis Line Graph - Rich Version.png')
    plt.show()


def plot_sentiment_pie_chart(positive_count, negative_count, neutral_count):
    labels = ['Positive emotions', 'Negative emotions', 'Neutral emotions']
    sizes = [positive_count, negative_count, neutral_count]
    colors = ['limegreen', 'tomato', 'lemonchiffon']
    explode = (0.1, 0, 0)  

    plt.figure(figsize=(8, 4))
    wedges, texts, autotexts = plt.pie(
        sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=140, textprops={'fontsize': 12}, pctdistance=0.7
    )
    plt.setp(autotexts, size=10, weight='bold', color='black')
    plt.title('Emotion Analysis pie Chart - Emotion Distribution')
    plt.savefig('Emotional Analysis Pie Chart - Rich Version.png')
    plt.show()


def plot_bar_chart(positive_count, negative_count, neutral_count):
    categories = ['Positive emotion', 'Negative emotions', 'Neutral emotion']
    values = [positive_count, negative_count, neutral_count]
    colors = ['mediumseagreen', 'salmon', 'khaki']

    plt.figure(figsize=(8, 5))
    plt.bar(categories, values, color=colors, alpha=0.8)
    plt.xlabel('Emotion category')
    plt.ylabel('Quantity')
    plt.title('Emotion Analysis Bar Chart - Comparison of Emotion Quantity')
    plt.grid(axis='y', alpha=0.3)
    plt.savefig('Emotion analysis bar chart.png')
    plt.show()


def plot_density_chart(sentimentslist):
    from scipy.stats import gaussian_kde

    density = gaussian_kde(sentimentslist)
    x = np.linspace(0, 1, 1000)
    y = density(x)

    plt.figure(figsize=(10, 5))
    plt.plot(x, y, color='royalblue', label='Emotional density distribution')
    plt.fill_between(x, y, color='lightblue', alpha=0.5)
    plt.xlabel('Emotion Index')
    plt.ylabel('Density')
    plt.title('Emotional density distribution map')
    plt.legend()
    plt.grid(alpha=0.3)
    plt.savefig('Emotional density distribution map.png')
    plt.show()


def main(file_path):
    source = read_text_file(file_path)
    sentimentslist = analyze_sentiments(source)

     positive_sentiments = [x for x in sentimentslist if x > 0.6]
    negative_sentiments = [x for x in sentimentslist if x < 0.4]
    neutral_sentiments = [x for x in sentimentslist if 0.4 <= x <= 0.6]

    if positive_sentiments:
        positive_coefficient = np.mean(positive_sentiments)
    else:
        positive_coefficient = 0

    if negative_sentiments:
        negative_coefficient = np.mean(negative_sentiments)
    else:
        negative_coefficient = 0

    if neutral_sentiments:
        neutral_coefficient = np.mean(neutral_sentiments)
    else:
        neutral_coefficient = 0

    print(f"Positive emotion coefficient: {positive_coefficient}")
    print(f"Negative emotion coefficient: {negative_coefficient}")
    print(f"Neutral sentiment coefficient: {neutral_coefficient}")

       results = [x - 0.5 for x in sentimentslist]

        plot_sentiment_line_chart(results)
    positive_count = len(positive_sentiments)
    negative_count = len(negative_sentiments)
    neutral_count = len(neutral_sentiments)
    plot_sentiment_pie_chart(positive_count, negative_count, neutral_count)
    plot_bar_chart(positive_count, negative_count, neutral_count)
    plot_density_chart(sentimentslist)


if __name__ == '__main__':
    plt.rcParams['font.sans-serif'] = ['SimHei']  
    plt.rcParams['axes.unicode_minus'] = False  
    main('output.txt')
