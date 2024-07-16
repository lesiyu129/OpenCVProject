import re
import string
import jieba
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import text
from sklearn.naive_bayes import MultinomialNB

# 分类报告
from sklearn.metrics import classification_report


def get_data(data_list):
    corpus = []
    labels = []
    for data in data_list:
        with open(data["path"], "r", encoding="utf-8") as f:
            f_data = f.readlines()
            corpus += f_data
            labels += [data["label"]] * len(f_data)

    return corpus, labels
    pass


def remove_empty_docs(corpus, labels):
    filter_corpus = []
    filter_labels = []
    for doc, label in zip(corpus, labels):
        if doc.strip():
            filter_corpus.append(doc)
            filter_labels.append(label)
    return filter_corpus, filter_labels


def token_size_doc(doc):
    tokens = jieba.cut(doc)
    return [token.strip() for token in tokens]


# 去除特殊字符
def remove_sepcial_char(doc):
    # 分词
    tokens = token_size_doc(doc)
    reg = re.compile("[{}]".format(re.escape(string.punctuation)))
    return " ".join(filter(None, [reg.sub("", token) for token in tokens]))


# 去除停用词
def remove_stop_words(doc):
    # 分词
    tokens = token_size_doc(doc)
    with open("../NLP_DATA/chap_3/stop_words.utf8", "r", encoding="utf-8") as f:
        stop_words = f.readlines()
    return " ".join(
        filter(None, [token for token in tokens if token not in stop_words])
    )


def normalize_corpus(corpus):
    result = []
    for doc in corpus:
        doc = remove_sepcial_char(doc)
        doc = remove_stop_words(doc)
        result.append(doc)
    return result


def tfidf_extractor(train_x, text_x):
    vectorizer = text.TfidfVectorizer()
    return vectorizer.fit_transform(train_x), vectorizer.transform(text_x)


def get_model(model, train_x, train_y, test_x, test_y):
    model.fit(train_x, train_y)
    pred_test_y = model.predict(test_x)
    return classification_report(test_y, pred_test_y)


if __name__ == "__main__":
    # 读取数据
    data_list = [
        {"path": "../email_data/data/ham_data.txt", "label": 1},
        {"path": "../email_data/data/spam_data.txt", "label": 0},
    ]
    corpus, labels = get_data(data_list)

    # 移除空文档
    corpus, labels = remove_empty_docs(corpus, labels)

    # 切分训练集和测试集
    train_x, test_x, train_y, test_y = train_test_split(
        corpus, labels, test_size=0.3, random_state=42, stratify=labels
    )

    # 规范化处理(去除符号，去除停用词)
    train_x = normalize_corpus(train_x)
    test_x = normalize_corpus(test_x)
    # 计算TF-IDF
    train_x, test_x = tfidf_extractor(train_x, test_x)
    print(train_x.shape, test_x.shape)

    model_dict = {
        "朴素贝叶斯": MultinomialNB(),
    }
    cla = get_model(model_dict["朴素贝叶斯"], train_x, train_y, test_x, test_y)
    print(cla)
