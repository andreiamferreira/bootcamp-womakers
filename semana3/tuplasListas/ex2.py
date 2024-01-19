# Faça um Programa que peça as quatro notas de 5 alunos, calcule
# e armazene numa lista a média de cada aluno, imprima o número
# de alunos com média maior ou igual a 7.0.
n = 0
studentsGrades = {}

print("Enter values for the list, one per line. Press Enter on a blank line to finish:")
while(n < 4):
    values_list = []
    k = 0
    for student_id in range(n, n+1):
        while (k < 5):
            print(f'Digite {k +1}ª nota do aluno {student_id + 1}: \n')
            value = float(input())
            values_list.append(value)
            k += 1
        

    studentsGrades[student_id] = values_list.copy()
    n += 1
        
print(studentsGrades)


