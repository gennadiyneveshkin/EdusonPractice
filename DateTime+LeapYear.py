year = int(input ('Введите год: '))
month = input('Введите название месяца с мальенькой буквы: ')

while month not in ['январь',
                    'март',
                    'май',
                    'июль',
                    'август',
                    'октябрь',
                    'декабрь',
                    'апрель',
                    'июнь',
                    'сентябрь',
                    'ноябрь',
                    'февраль']:
    print('Месяц введен неверно!')
    month = input('Введите название месяца с маленькой буквы: ')

def days_per_month (year, month):


    if month in ['январь',
                 'март',
                 'май',
                 'июль',
                 'август',
                 'октябрь',
                 'декабрь']:
        return 31

    elif month in ['апрель',
                   'июнь'
                   'сентябрь'
                   'ноябрь']:
        return 30



    elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return 29

    return 28

print ('В {} году в месяце {} {} дней'.format(year, month, days_per_month (year, month)))

