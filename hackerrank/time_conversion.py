def timeConversion(s):
    # Write your code here
    hours = int(s[:2])
    rest = s[2:-2]

    if s[-2:] == 'PM':
        if hours != 12:
            hours = hours + 12
    else:
        if hours == 12:
            hours = 0

    print(f'{hours:02d}{rest}')


timeConversion('07:05:45PM')
