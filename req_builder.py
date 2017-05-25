# coding: utf-8
# Формируем строку запроса

from __future__ import print_function


def req_builder(words, server, num, page='1'):
    base = 'https://yandex.ru/blogs/rss/search?text='
    w = '"' + words + '"'
    n = '&numdoc=' + num
    p = '&p=' + page
    s = '&server=' + server
    return base + w + n + p + s

# for test
if __name__ == '__main__':
    l_words = ['новости из москвы', 'новости из воронежа', 'омские новости']
    for i in l_words:
        print(req_builder(i, 'twitter.com', '20'))
