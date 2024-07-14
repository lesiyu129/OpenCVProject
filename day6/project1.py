"""
    分词统计词频，取出高频词
"""

import jieba


def get_content(path):
    with open(path, "r", encoding="gbk") as f:
        content = ""
        for line in f.readlines():
            line = line.strip()
            content += line
        return content


def get_stop_words(path):
    with open(path, "r", encoding="utf-8") as f:
        res = [stop_word.strip() for stop_word in f.readlines()]
    return res


def filer_stop_words(content, stop_words):
    return [word for word in content if word not in stop_words]


def get_tf(words, topk=10):
    word_count = {}
    word_count.keys()
    for word in words:
        if word not in word_count:
            word_count[word] = 0
        word_count[word] += 1
    return sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:topk]


if __name__ == "__main__":
    contentData = get_content("../NLP_DATA/chap_3/news/C000008/11.txt")
    cutList = list(jieba.cut(contentData))
    print(cutList)
    stop_words = get_stop_words("../NLP_DATA/chap_3/stop_words.utf8")
    print(stop_words)

    cutList = filer_stop_words(cutList, stop_words)
    print(cutList)
    topLisTF = get_tf(cutList, 10)
    print(topLisTF)
