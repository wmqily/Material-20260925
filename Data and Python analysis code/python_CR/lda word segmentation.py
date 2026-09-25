import jieba
import re

def stopwordslist():
    stopwords = [line.strip() for line in open('stop_words.txt', encoding='UTF-8').readlines()]
    return stopwords

def processing(text):
    text = re.sub("@.+?( |$)", "", text)
    text = re.sub("【.+?】", "", text)
    text = re.sub(".*?:", "", text)
    text = re.sub("#.*#", "", text)
    text = re.sub("\n", "", text)
    return text

def seg_depart(sentence):
    sentence_depart = jieba.cut(sentence.strip())  
    stopwords = stopwordslist()        
    outstr = ''        
    for word in sentence_depart:          
        if word not in stopwords and len(word) == 2 and not word.isdigit() and word != '\t':
            outstr += word
            outstr += " "
    return outstr.strip()  

input_filename = "output.txt"   
output_filename = "Clean up comments.txt"  

with open(output_filename, 'w', encoding='UTF-8') as output_file:
    with open(input_filename, 'r', encoding='UTF-8') as input_file:
        for line in input_file:
            print(line.strip())     
            line = processing(line)  
            line_seg = seg_depart(line)  
            output_file.write(line_seg + '\n')  

print("Successful word segmentation！！！")