# coding: utf-8
from __future__ import print_function
import urllib

import time

from api_vk import table_vk_builder
from get_expression import get_expression
from req_builder import req_builder
from scrap_lj import table_lj_builder
from scrap_tw import table_tw_builder
from table_header import table_header
try:
    from xml.etree.cElementTree import ElementTree
except ImportError:
    from xml.etree.ElementTree import ElementTree


SN_L = ['twitter.com', 'vk.com', 'livejournal.com']

print('Выберите язык:')
print('1 - русский;  2 - украинский; 3 - арабский;')
l = str(input())

print('Выберите соц. сеть:')
print('1 - twitter.com;  2 - vk.com;')
print('3 - lj.com;  4 - все;')
sn = str(input())
num = str(input('Введите количество запросов: '))
f_name = input('Введите имя файла (" "): ')
dir_file_name = 'results/' + f_name + '.xls'

words_list = get_expression(str(l))

wb, sheet1 = table_header()

gn = 1
if sn == '1':
    for string_words in words_list:
        print('\n' + string_words)
        tw = urllib.urlopen(req_builder(string_words, SN_L[0], num))
        tw_root = ElementTree(file=tw).getroot()
        gn = table_tw_builder(tw_root, sheet1, gn)
elif sn == '2':
    for string_words in words_list:
        print('\n' + string_words)
        vk = urllib.urlopen(req_builder(string_words, SN_L[1], num))
        vk_root = ElementTree(file=vk).getroot()
        gn = table_vk_builder(vk_root, sheet1, gn)
elif sn == '3':
    for string_words in words_list:
        print('\n' + string_words)
        lj = urllib.urlopen(req_builder(string_words, SN_L[2], num))
        lj_root = ElementTree(file=lj).getroot()
        gn = table_lj_builder(lj_root, sheet1, gn)
elif sn == '4':
    for string_words in words_list:
        print('\n' + string_words)
        tw = urllib.urlopen(req_builder(string_words, SN_L[0], num))
        tw_root = ElementTree(file=tw).getroot()
        gn = table_tw_builder(tw_root, sheet1, gn)
        time.sleep(1)  # таймаут на 1 сек., чтобы не превышать лимит запросов yandex
    for string_words in words_list:
        print('\n' + string_words)
        vk = urllib.urlopen(req_builder(string_words, SN_L[1], num))
        vk_root = ElementTree(file=vk).getroot()
        gn = table_vk_builder(vk_root, sheet1, gn)
        time.sleep(1)
    for string_words in words_list:
        print('\n' + string_words)
        lj = urllib.urlopen(req_builder(string_words, SN_L[2], num))
        lj_root = ElementTree(file=lj).getroot()
        gn = table_lj_builder(lj_root, sheet1, gn)
        time.sleep(1)
else:
    print('Нет сети - ', end='')
    print(sn)

wb.save(dir_file_name)



