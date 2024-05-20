# 导包
import re
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# 读取文学作品的文本数据：
def read_text(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    return text


file_path = './庆余年.txt'
text = read_text(file_path)


# 进行文本数据的处理和词频统计
def preprocess_text(text):
    # 去除标点符号和特殊字符
    text = re.sub(r'[^\w\s]', '', text)
    # 转换为小写
    text = text.lower()
    return text


processed_text = preprocess_text(text)


def calculate_word_frequency(text):
    words = text.split()
    word_count = Counter(words)
    return word_count


word_count = calculate_word_frequency(processed_text)


# 生成词云图
def generate_word_cloud(word_count):
    font = './SIMLI.TTF'  # 设置中文字体，否则词云图可能不显示中文（最容易出错的步骤）
    wordcloud = WordCloud(width=800, height=400, background_color='white', font_path=font).generate_from_frequencies(word_count)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    generate_word_cloud(word_count)
