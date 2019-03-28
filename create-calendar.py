#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  create-calendar.py - Create khaarazmi calendar note-book, Version 1.0
#  Copyright 2019 ardeshirv@protonmail.com, Licensed Under GPLv3+


def main(args):
    file_path = '/home/asha/Documents/Desktop/1398.txt'
    day_pattern = ('تاریخ: {}/{}/{} {}\nعنوان: {}\nبرنامه: ' +
                   '\nگزارش: \nبرآیند: \nتوضیحات: \n\n')
    month_pattern = '\n\n    {} {}\n\n\n'
    month_names = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور',
                   'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']
    day_names = ['شنبه', 'یکشنبه', 'دوشنبه',
                 'سه‌شنبه', 'چهارشنبه', 'پنجشنبه', 'جمعه']
    print('Create khaarazmi calendar note-book, Version 1.0\n' + file_path)
    day = 1
    month = 1
    days = 365
    year = 1398
    index = 101
    day_name = 5
    with open(file_path, 'w') as f:
        for i in range(index, index + days):
            if day == 1:
                f.write(month_pattern.format(
                        month_names[month - 1],
                        convert_num_to_persian_str(year)))
            f.write(day_pattern.format(
                    convert_num_to_persian_str(year),
                    convert_num_to_persian_str(month),
                    convert_num_to_persian_str(day),
                    day_names[day_name],
                    convert_num_to_persian_str(i)))
            day += 1
            day_name += 1
            if day_name > 6:
                day_name = 0
            if (month < 7 and day > 31) or (month > 6 and day > 30):
                day = 1
                month += 1
                if month > 12:
                    month = 1
                    Year += 1
    return 0


def convert_num_to_persian_str(n):
    value = ''
    num_str = str(n)
    english_num = '0123456789'
    persian_num = '۰۱۲۳۴۵۶۷۸۹'
    for c in num_str:
        for i in range(0, 10):
            if c == english_num[i]:
                value += persian_num[i]
    if len(value) < 2:
        value = '۰' + value
    if len(value) < 2:
        value = '۰' + value
    return value


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
