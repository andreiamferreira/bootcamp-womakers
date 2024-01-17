# Escreva um programa que calcule o salário líquido. Lembrando de
# declarar o salário bruto e o percentual de desconto do Imposto de
# Renda.
    # ● Renda até R$ 1.903,98: isento de imposto de renda;
    # ● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
    # ● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
    # ● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
    # ● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.
    

inputSalary = float(input('Digite o salário: \n'))

if inputSalary <= 1903.98:
    grossSalary = inputSalary
    discount = 'Isento'
    discounted = 0.00
elif 1903.98 < inputSalary < 2826.65:
    discounted = inputSalary*(7.5/100)
    grossSalary = inputSalary - discounted
    discount = '7,5%'
elif 2826.66 < inputSalary < 3751.05:
    discounted = inputSalary*(15/100)
    grossSalary = inputSalary - discounted
    discount = '15%'
elif 3751.06 < inputSalary < 4664.68:
    discounted = inputSalary*(22.5/100)
    grossSalary = inputSalary - discounted
    discount = '22,5%'
else:
    discounted = inputSalary*(27.5/100)
    grossSalary = inputSalary - discounted
    discount = '27,5%'

print(f'Salário: {inputSalary}\nAlíquota: {discount}\nValor descontado: {format(discounted, ".2f")}\nSalário bruto: {format(grossSalary, ".2f")} ')