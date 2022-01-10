import calendar
yrip=int(input("enter the year:"))
mnip=int(input("enter the month:"))
file_name=(f'{mnip} {yrip}.txt')
f=open(file_name,'w+')
y_n_m=(calendar.month(yrip,mnip))
f.write(y_n_m)
