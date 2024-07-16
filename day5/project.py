"""
    分词
"""

import jieba

# 待分词的文本
text = "吉林市长春药店"


#  分词精确模式
strListData = list(jieba.cut(text, cut_all=False))
print("分词精确模式", strListData)


#  分词全模式
strListData = list(jieba.cut(text, cut_all=True))
print("分词全模式", strListData)


#  分词搜索引擎模式
strListData = list(jieba.cut_for_search(text))
print("分词搜索引擎模式", strListData)
