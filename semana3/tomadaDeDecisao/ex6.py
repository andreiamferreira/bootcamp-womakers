# 6. Crie um programa que solicite ao usuário um login e uma senha. O
# programa deve permitir o acesso apenas se o usuário for "admin" e a senha
# for "admin123", caso contrário imprima uma mensagem de erro.

userLogin = input('Digite seu login: \n')
userPassword = input('Digite sua senha: \n')

if userLogin == 'admin' and userPassword == 'admin123':
    print('Aceso permitido!')
else:
    print('ERRO! Acesso negado.')