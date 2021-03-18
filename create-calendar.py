#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  create-calendar.py - Creates Persian calendar note-book template, Version 1.0
#  Copyright (c) 2019 ArdeshirV@protonmail.com, Licensed under GPLv3+
from title import print_title


def main(args):
    print_title("create-calendar", "Creates Persian calendar note-book template",
                "1.0", "2019", "ArdeshirV@protonmail.com", "GPLv3+", True)
    day_pattern = ('تاریخ: {}/{}/{} {}\nعنوان: {}\nبرنامه: ' +
                   '\nگزارش: \nبرآیند: \nتوضیحات: \n\n')
    month_pattern = '\n\n    {} {}\n\n\n'
    month_names = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور',
                   'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']
    day_names = ['شنبه', 'یکشنبه', 'دوشنبه',
                 'سه‌شنبه', 'چهارشنبه', 'پنجشنبه', 'جمعه']
    day = 1
    month = 1
    days = 365
    year = 1400
    index = 1
    day_name = 1
    file_path = '{}.txt'.format(year)

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
    print('\033[1mOutput: \033[1;35m{}\033[0m'.format(file_path))
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
    from sys import exit, argv
    exit(main(argv))
