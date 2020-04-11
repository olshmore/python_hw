n=int(input('Type in number'))
max=0
while (n%10>=1) and (n%10<=9):
    if n%10>max:
        max=n%10
    n = n//10
print('max= ',max)