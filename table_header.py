# coding: utf-8
import xlwt


def table_header():
    wb = xlwt.Workbook(encoding='utf-8')
    sheet1 = wb.add_sheet('Sheet 1')
    sheet1.write(0, 1, 'Логин')
    sheet1.write(0, 2, 'Количество подписчиков')
    sheet1.write(0, 3, 'Текст сообщения')
    sheet1.write(0, 4, 'Ссылка')
    sheet1.write(0, 0, 'Сеть')
    return wb, sheet1


if __name__ == '__main__':
    wb, sheet1 = table_header()
    wb.save('tests/head_test.xls')

