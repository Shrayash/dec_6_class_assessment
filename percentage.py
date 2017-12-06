a = [50, 70, 40, 10, 30]
b = 0
for i in range(0,len(a)):
    b = a[i] + b

total = b
percentage = (total/5)*100

if percentage > 40:
    print('Student is in pass grade')
elif percentage>=70:
    print('Grade=B')
elif percentage>=80:
    print('Grade=A')
elif percentage>=95:
    print('Grade=A+')
else:
    print('Fail')

