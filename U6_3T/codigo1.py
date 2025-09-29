# Código 1
print("I Competição de Programação da Start")

# Código 2
ano = "II"
print(ano, "Competição de Programação da Start")

# Código 3
print(f"{ano} Competição de Programação da Start")

# Aula 2
# Código 1
livro_ficcao = 10
livro_nficcao = 8
livro_infantil = 6

pontos_rodrigo = livro_ficcao + livro_nficcao + livro_infantil

print(f"Os pontos totais do Rodrigo são: {pontos_rodrigo}")

# Aula 3
# Código 1
total_figurinhas = int(input("Digite o total de figurinhas: "))
numero_amigos = int(input("Digite o número de amigos: "))

figurinhas_amigos = total_figurinhas // (numero_amigos + 2)
figurinhas_joao = 2 * figurinhas_amigos

print(f"João recebeu {figurinhas_joao} figurinhas.")

# Aula 4
# Código 1
numero_alunos = int(input("Digite a quantidade de alunos: "))
numero_monitores = int(input("Digite a quantidade de monitores: "))

resposta_positiva = "Pode ir"
resposta_negativa = "Não pode ir"

if numero_alunos + numero_monitores <= 50:
print(resposta_positiva)
else:
print(resposta_negativa)
