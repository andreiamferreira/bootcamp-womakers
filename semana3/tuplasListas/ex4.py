# 4. Crie um dicionário representando contatos (nome, telefone).
# Permita ao usuário procurar por um contato pelo nome.

contactListDict = {
    'Ana Leticia': '91111-1111',
    'Manoela': '92222-2222',
    'Priscila': '92222-4444',
    'Andreia': '94444-2233',
    'Mileine': '91212-1212',
    'Naiane': '93535-9090',
    'Sara': '97777-9898',
    'Larissa': '91515-5757',
    'Jacqueline': '99898-2424'
}

name = input('Digite o nome a ser pesquisado: \n')
if name.capitalize() in contactListDict:
    print(f'Nome: {name} \nTelefone: {contactListDict[name.capitalize()]}')
    