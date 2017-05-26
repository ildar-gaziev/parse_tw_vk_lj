# coding: utf-8
from __future__ import print_function
import urllib
import time
try:
    from xml.etree.cElementTree import ElementTree
except ImportError:
    from xml.etree.ElementTree import ElementTree
import vk

TOKEN = ' '  # ключ vk
session = vk.Session(access_token=TOKEN)  # авторизированя сессия
vk_api = vk.API(session)


def table_vk_builder(vk_root, sheet, gn):
    n = gn
    print('vk: ', end='')
    for item in vk_root.iter('item'):
        login = item.find('{urn:yandex-blogs}journal').attrib['url']
        vk_id = login[14:]
        if vk_id[0] == 'i':
            vk_id = vk_id[2:]
            try:
                foll = vk_api.users.get(user_id=vk_id, fields=['followers_count'])[0]['followers_count']
            except:
                time.sleep(1.6)
                continue
            sheet.write(n, 1, login)
            sheet.write(n, 2, foll)
            sheet.write(n, 3, item.find('description').text)
            sheet.write(n, 4, item.find('link').text)
            sheet.write(n, 0, 'vk')
            print(str(n) + ' ', end='')
            time.sleep(0.3)  # таймаут на 0.3 сек., чтобы не превышать лимит запросов vk api
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

    vk = urllib.urlopen("https://yandex.ru/blogs/rss/search?text=\"москва\"&numdoc=3&p=1&server=vk.com")
    vk_root = ElementTree(file=vk).getroot()
    wb, sheet1 = table_header()
    table_vk_builder(vk_root, sheet1, 1)
    wb.save('tests/vk_test.xls')
