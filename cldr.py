import calendar
usrip=int(input('enter the year:'))
file_name=(f'{usrip}.txt')
f=open(file_name,'w+')
cldr=calendar.calendar(usrip)
f.write(cldr)
