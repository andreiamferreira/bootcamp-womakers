# 7. Desenvolver um programa que solicite a idade do usuário e identifique se
# ele é uma criança, um adolescente, adulto ou idoso

userAge = int(input('Qual sua idade? \n'))

if userAge <= 13:
    print('Criança')
elif userAge <= 18:
    print('Adolescente')
elif userAge <= 65:
    print('Adulto')
else:
    print('Idoso')