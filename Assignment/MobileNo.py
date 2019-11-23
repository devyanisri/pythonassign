import re
a=str(input("enter your mobile no."))
pattern='^[0-9]{10}$'
match=re.search(pattern,a)

if match:
    print('validate no.')

else:
    print('invalid no.')