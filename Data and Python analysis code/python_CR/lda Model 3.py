import os
import pyLDAvis.gensim
from gensim.models import LdaModel
from gensim.corpora import Dictionary
from gensim import corpora
import pyLDAvis
from tabulate import tabulate

os.environ['JOBLIB_TEMP_FOLDER'] = 'C:/temp'


def load_data(file_path):
    with open(file_path, encoding='utf-8', errors='ignore') as f:
        return [line.split() for line in f.read().split('\n') if line.strip()]


def train_lda(data, num_topics=2):
    dictionary = Dictionary(data)
    corpus = [dictionary.doc2bow(text) for text in data]

    lda_model = LdaModel(
        corpus=corpus,
        id2word=dictionary,
        num_topics=num_topics,
        passes=30,
        random_state=1,
        alpha='auto',
        eta='auto'
    )
    return lda_model, corpus, dictionary


def generate_three_line_table(model, num_words=10):
    topics = model.show_topics(num_words=num_words, formatted=True)

    table_data = []
    for topic_id, topic in topics:
        word_list = []
        for item in topic.split(" + "):
            prob, word = item.split("*")
            word_list.append(word.strip('"'))
        table_data.append(word_list[:num_words])

    transposed = list(map(list, zip(*table_data)))

    headers = [f"Theme {i + 1}" for i in range(len(table_data))]
    return tabulate(transposed, headers=headers, tablefmt="github")


if __name__ == "__main__":
    input_file = "Clean up comments.txt"  
    output_md = "Topic analysis results.md"
    output_html = "topic.html"

    dataset = load_data(input_file)

    lda_model, corpus, dictionary = train_lda(dataset, num_topics=2)

    table_str = generate_three_line_table(lda_model)

    with open(output_md, "w", encoding="utf-8") as f:
        f.write("# LDA topic analysis results\n\n")
        f.write(table_str)

    vis_data = pyLDAvis.gensim.prepare(lda_model, corpus, dictionary)
    pyLDAvis.save_html(vis_data, output_html)

    print("Execution completed：")
    print(f"- The topic analysis results have been saved to {output_md}")
    print(f"- The visualization results have been saved to {output_html}")
    print("\nPreview of the generated table：")
    print(table_str)