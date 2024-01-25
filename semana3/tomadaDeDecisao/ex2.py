# 2. Faça um Programa que pergunte em que turno você estuda. Peça para
# digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom
# Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

studyShift = input('Em qual turno você estuda? \nDigite M para "matutino", V para "vespertino", ou N para "noturno"\n')

if studyShift.lower() == 'n' :
    print('Boa Noite')
elif studyShift.lower() == 'v':
    print('Boa Tarde!')
elif studyShift.lower() == 'm':
    print('Bom Dia!')
else:
    print('Valor Inválido!')