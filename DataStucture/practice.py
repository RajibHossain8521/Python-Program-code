select_month = int(input('Select month :'))
days = int(input('enter the number of days:'))


if select_month == 1 and 3 and 5 and 7 and 8 and 10 and 12:
    month = days // 31
    new_days = days % 31
    print(days, 'days=', month, 'month and', new_days, 'days')

elif select_month == 4 and 6 and 9 and 11:
    month = days // 30
    new_days = days % 30
    print(days, 'days=', month, 'month and', new_days, 'days')

else:
    month = days // 28
    new_days = days % 28
    print(days, 'days=', month, 'month and', new_days, 'days')
