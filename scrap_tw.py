# coding: utf-8
from __future__ import print_function
import urllib
from bs4 import BeautifulSoup


def scrap_tw(l):
    html = BeautifulSoup(urllib.urlopen(l), 'html.parser')
    if html is None:
        followers = '0'
    else:
        if html.find('a', {'data-nav': 'followers'}) is None:
            followers = '0'
        else:
            followers = html.find('a', {'data-nav': 'followers'}).find('span', {'class': 'ProfileNav-value'}).text
    return followers


def table_tw_builder(tw_root, sheet, gn):
    n = gn
    print('tw: ', end='')
    for item in tw_root.iter('item'):
        if item.find('author') is None:
            print('(-1)', end=' ')  # не удалось получить автора
            continue
        sheet.write(n, 1, item.find('author').text[19:])
        foll = scrap_tw(item.find('author').text)
        sheet.write(n, 2, foll.rstrip())
        sheet.write(n, 3, item.find('description').text)
        sheet.write(n, 4, item.find('link').text)
        sheet.write(n, 0, 'twitter')
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

    tw = urllib.urlopen("https://yandex.ru/blogs/rss/search?text=\"москва\"&numdoc=20&p=1&server=twitter.com")
    tw_root = ElementTree(file=tw).getroot()
    wb, sheet1 = table_header()
    table_tw_builder(tw_root, sheet1, 1)
    wb.save('tests/tw_test.xls')
