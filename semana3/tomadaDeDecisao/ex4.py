# 4. Implemente um programa que classifique um aluno com base em sua
# pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se
# a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é
# reprovado.

studentGrade = float(input('Digite a nota do aluno: \n'))

if studentGrade >= 7:
    print('Aprovado')
else:
    print('Reprovado')