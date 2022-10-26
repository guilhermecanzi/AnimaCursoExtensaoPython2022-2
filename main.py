# Aula Dia 26/10/2022
# comando input(): quero permitir que
# o usuário digite algo
nome = input("Digite seu nome: ")
# peça a idade do usuário
idade = int(input("Qual sua idade? "))


# comando de saída... exibir na tela
print(f"Boa noite, {nome}")
print("Sua idade é {}".format(idade))

# e se eu quisesse mostrar o DOBRO da idade informada?
dobro =  idade * 2
print("O dobro da sua idade é {}".format(dobro))