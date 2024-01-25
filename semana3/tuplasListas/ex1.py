#  Utilizando listas faça um programa que faça 5 perguntas para uma
# pessoa sobre um crime.
# As perguntas são:
    # ""Telefonou para a vítima?""
    # ""Esteve no local do crime?""
    # ""Mora perto da vítima?""
    # ""Devia para a vítima?""
    # ""Já trabalhou com a vítima?""
# O programa deve no final emitir uma classificação sobre a participação
# da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser
# classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como
# ""Assassino"".
# Caso contrário,ele será classificado como""Inocente"".

positive = 0
veredict = ''

dictionaryQuestions = {
    'Telefonou para a vítima?': '',
    "Esteve no local do crime?": '',
    "Mora perto da vítima?": '',
    "Devia para a vítima?": '',
    "Já trabalhou com a vítima?": ''
    }

for key in dictionaryQuestions:
    dictionaryQuestions[key] = input(key + '\n')
    
for value in dictionaryQuestions.values():
    if value.lower() == "sim":
        positive += 1
        
if positive == 2:
    veredict = 'Suspeito'
elif 4 <= positive:
    veredict = 'Cúmplice'
elif positive == 5:
    veredict = 'Assassino'
else:
    veredict = 'Inocente'
    
print(veredict)