def emailvalid (email):
    f=open('13.txt','r')

    username,domain=email.split('@')
    domain_name,domain_ext=domain.split('.')

    if len(username)>3 and len(domain_name)>=3 and len(domain_ext)>=2:
        print(f'email id:{email} is valid')
        f = open('13.txt', 'a')
        a=[]
        a.append(f.write(email))
    else:
        print(f'email id:{email}is not valid')
        f=open('13.txt','a')
        b=[]
        b.append(f.write(email))

email=input('enter your mail id:')
emailvalid(email)



