# coding: utf-8

from __future__ import print_function
import urllib
from bs4 import BeautifulSoup
try:
    from xml.etree.cElementTree import ElementTree
except ImportError:
    from xml.etree.ElementTree import ElementTree


def scrap_lj(l):
    html = BeautifulSoup(urllib.urlopen(l), 'html.parser')
    if html is None:
        sc = '0'
    else:
        sc = html.find('div', {'class': 'b-profile-stat-value'})
        if sc is None:
            sc = '0'
        else:
            sc = sc.text
    return sc


def table_lj_builder(lj_root, sheet, gn):
    n = gn
    print('lj: ', end='')
    for item in lj_root.iter('item'):
        if item.find('author') is None:
            print('(-1)', end=' ')  # не удалось получить автора
            continue
        sheet.write(n, 1, item.find('author').text)
        author = item.find('author').text + 'profile'
        foll = scrap_lj(author)
        sheet.write(n, 2, foll.rstrip())
        sheet.write(n, 3, item.find('description').text)
        sheet.write(n, 4, item.find('link').text)
        sheet.write(n, 0, 'livejournal')
        print(str(n) + ' ', end='')
        n += 1
    gn = n
    return gn


# for test
if __name__ == '__main__':
    from table_header import table_header

    try:
        from xml.etree.cElementTree import ElementTree
    except ImportError:
        from xml.etree.ElementTree import ElementTree
    lj = urllib.urlopen("https://yandex.ru/blogs/rss/search?text=\"Лондон\"&numdoc=3&p=1&server=livejournal.com")
    lj_root = ElementTree(file=lj).getroot()
    wb, sheet1 = table_header()
    table_lj_builder(lj_root, sheet1, 1)
    wb.save('tests/lj_test.xls')
