# coding: utf-8
# получаем список фраз для поиска

from __future__ import print_function


def get_expression(lang):
    global f
    if lang == '1':
        f = open('expression/ru.txt', 'r')
    elif lang == '2':
        f = open('expression/ua.txt', 'r')
    elif lang == '3':
        f = open('expression/ar.txt', 'r')
    else:
        print('такой выбор не доступен')
    gwl = f.read().split('\n')
    f.close()
    return gwl

if __name__ == '__main__':
    w = get_expression('1')
    for i in w:
        print(i)
