# Solicite ao usuário o número de horas de exercício físico por semana.
# Calcule o total de calorias queimadas em um mês, considerando uma
# média de 5 calorias por minuto de exercício.


weeklyExerciceHours = float(input('Por quantas horas você praticou exercício física por semana? \n'))

weeklyExerciceInMinutes = weeklyExerciceHours*60
burnedCaloriesInaMonth = (weeklyExerciceInMinutes*5)*4

print(f'Calorias queimadas no mês: {format(burnedCaloriesInaMonth, ".2f")}')