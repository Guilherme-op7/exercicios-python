salario = float(input('qual é o salario do funcionario? R$'))
novo = salario + (salario * 15 / 100)
print('um funcionario que ganhava R${:.2f}, com uma aumento de 15%, passa a receber R${:.2f}'.format(salario, novo))
