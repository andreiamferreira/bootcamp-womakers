# Faça um Programa que pergunte quanto você ganha por hora e o
# número de horas trabalhadas no mês.Calcule e mostre o total do seu
# salário no referido mês.

salaryByHour = float(input('Quanto você ganha por hora? \n'))
workedHoursByMonth = float(input('Quantas horas você trabalhou no mês? \n'))

monthlySalary = salaryByHour*workedHoursByMonth

print('Total do salário no mês: R$', format(monthlySalary, ".2f"))