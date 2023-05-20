idade_monica =int(input())
idade_filho1 =int(input())
idade_filho2 =int(input())
'''a idade do terceiro filho é a idade de monica menos a idade dos dois
filhos'''
for i in range(3):
    if idade_monica > 0:
        idade_filho3 = idade_monica - (idade_filho1 + idade_filho2)
if idade_filho1 > idade_filho2 and idade_filho1 > idade_filho3: 
    print(idade_filho1)
elif idade_filho2 > idade_filho1 and idade_filho2 > idade_filho3:
    print(idade_filho2)
elif idade_filho3 > idade_filho2 and idade_filho3 > idade_filho1:
    print(idade_filho3)
