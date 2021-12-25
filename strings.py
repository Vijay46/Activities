########################################
#                                      #
# STRING FUNCTION IN PYTHON            #
#                                      #
# AUTHOR:Vijay                         #
# Email:vijumeti1882001@gmail.com      #
# Licence:                             #
#                                      #
########################################       
# 1st:To check if a certain char is present in string or not :
a='python is easy'  
print('p' in a)
print('z' not in a)

#slicing:
a='python is easy'
print(a[0:5]) 

# Negative indexing upper,lower and split :
a='python is easy'
print(a[-1])
a1=a.upper()
print(a1)
a1=a.lower()
print(a)
a1=a.split()
print(a1)

# Concatenation of  strings and converting:
a=('i am learnig python ')
b=('at skill disk')
c=str(3.97)
print(a+' '+c+' '+b)
