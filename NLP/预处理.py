# -*- coding: utf-8 -*-
import re
import jieba

# 去除emoji，标点符号和停用词（文件）
def filter_emoji(desstr, restr=''):
    # 过滤表情
    try:
        co = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    return co.sub(restr, desstr)


def del_stop_words(review, stop_words_set):
    #   返回的是去除停用词后的剩余词
    # 去除emoji
    review = filter_emoji(review)
    # 去除标点符号
    words = re.sub('\W*', '', review)
    result_list = []
    result = jieba.cut(words)
    for r in result:
        # if r not in stop_words_set:
        result_list.append(r)
    return result_list
