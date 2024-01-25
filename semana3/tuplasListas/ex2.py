# Faça um Programa que peça as quatro notas de 5 alunos, calcule
# e armazene numa lista a média de cada aluno, imprima o número
# de alunos com média maior ou igual a 7.0.
numberOfStudents = 0
studentsGrades = {}
averages = {}

print("Adicione os valores (separação via tecla 'Enter'):")
while(numberOfStudents < 4):
    gradesByStudent = []
    numberOfGrades = 0
    for student in range(numberOfStudents, numberOfStudents+1):
        while (numberOfGrades < 5):
            print(f'Digite {numberOfGrades +1}ª nota do aluno {student + 1}: \n')
            grade = float(input())
            gradesByStudent.append(grade)
            numberOfGrades += 1
        
    studentsGrades[student] = gradesByStudent.copy()
    numberOfStudents += 1

count = 0
for student, grades in studentsGrades.items():
    avgGrades = sum(grades) / len(grades)
    averages[student] = avgGrades
    if avgGrades >= 7.0:
        count += 1

print('Quantidade de alunos com média maior ou igual à 7.0:\n', count)



