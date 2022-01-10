usrip=input('enter file name:')
start =int(input('enter the start tabel:'))
end=int(input('enter the end tabel:'))
file_name=(f'{usrip}{start}{end}_tabel.txt')
f=open(file_name,'w+')
for i in range (start,end+1):
    

    for j in range(1,11):
        
     f.write(f'{i} x {j} = {i*j}\n') 
      
