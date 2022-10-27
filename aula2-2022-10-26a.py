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

# estrutura condicional - o famoso IF
# se a pessoa for maior de idade, mostre "Você é maior de idade, ótimo! Já pode beber ou dirigir"
if (idade >= 18):
  print("Você é maior de idade, ótimo! Já pode beber ou dirigir")
else:
  print("Oh não, você ainda não pode beber ou dirigir")

# e se eu quisesse perguntar o gênero (M == masculino e F == feminino)
# mostre (... e você também precisa prestar o serviço militar obrigatório)
genero = input("Qual seu gênero? M = Masculino, F = Feminino. ")
if (idade >= 18 and genero == "M"):
  print("... e você também precisa/precisou prestar o serviço militar obrigatório")