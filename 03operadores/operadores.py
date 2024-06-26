# operadores aritméticos

print('Operadores aritméticos')
print('')

# adição

print('Adição:')
print('')

# 5
print(f'2 + 3: {2+3}')

# 9
print(f'6 + 3: {6+3}')

# 15
print(f'7 + 8: {7+8}')

# 57
print(f'25 + 32: {25+32}')
print('')

# subtração

print('Subtração')
print('')

# 6
print(f'10 - 4: {10 - 4}')

# 9
print(f'15 - 6: {15 - 6}')

# 18
print(f'20 - 2: {20 - 2}')

# 5
print(f'22 - 17: {22 - 17}')
print('')

#multiplicação

print('Multiplicação:')
print('')

# 48
print(f'12 * 4: {12 * 4}')

# 36
print(f'6 * 6: {6 * 6}')

# 200
print(f'10 * 20: {10 * 20}')

# 100
print(f'10 * 10: {10 * 10}')
print('')

#divisão - comum e inteira

print('Divisão "comum": - gera um número float')
print('')

# 6.0
print(f'48 / 8: {48 / 8}')

# 4.0
print(f'12 / 3: {12 / 3}')

# 10.0
print(f'20 / 2: {20 / 2}')

# 3.0
print(f'21 / 7: {21 / 7}')
print('')

print('Divisão "inteira": - gera um número int e usa duas barras como operador')
print('')

# 5
print(f'45 // 9: {45 // 9}')

# 6
print(f'18 // 3: {18 // 3}')

# 7
print(f'14 // 2: {14 // 2}')

# 3
print(f'21 // 7: {21 // 7}')
print('')

# módulo - devolve o resto da divisão

print('Módulo, operador percentual % nos devolve o resto da divisão ')
print('')

# 1
print(f'10 % 3: {10 % 3}')

# 2
print(f'22 % 4: {22 % 4}')

# 4
print(f'34 % 5: {34 % 5}')

# 5
print(f'17 % 6: {17 % 6}')
print('')

# exponenciação

print('Exponenciação: operador **')
print('')

# 8
print(f'2 ** 3: {2 ** 3}')

# 16
print(f'2 ** 4: {2 ** 4}')

# 32
print(f'2 ** 5: {2 ** 5}')

# 64
print(f'2 ** 6: {2 ** 6}')
print('')

# precedência de operadores
# mesma coisa da matemática: 
# primeiro o que está entre parênteses, 
# depois exponenciação 
# multiplicação e divisão (conforme aparecer, da esquerda pra direita)
# adição e subtração (conforme aparecer, da esquerda pra direita)
# expressão com os mesmos números e operadores, mas com resultado
# exemplos abaixo

# 0
print(10 - 5 * 2)

# 10
print((10 - 5) * 2)

# 200
print(10 ** 2 * 2)

# 10000
print(10 ** (2 * 2))

# 20.0 - quando envolve divisão, vira float
print(10 / 2 * 4)
print('')

# operadores de comparação

print('Operadores de comparação')
print('')

saldo = 500
saque = 200

print(f'Saldo: {saldo}')
print(f'Saque: {saque}')

# Operador de igualdade ==, resultado da expressão abaixo: False
print(f'Saldo é  igual ao saque? {saldo == saque}')

# Operador de diferença !=, resultado da expressão abaixo: True
print(f'Saldo é  diferente do saque? {saldo != saque}')

# maior que > e Maior ou igual >=
# sempre verifica se o que está do lado esquerdo é maior (ou igual) o que está na direita
# resultado da expressão abaixo: True
print(f'Saldo é maior que saque? {saldo > saque}')

# resultado da expressão abaixo: True
print(f'Saldo é maior ou igual ao saque? {saldo >= saque}')


# menor que > e menor ou igual >=
# sempre verifica se o que está do lado esquerdo é menor (ou igual) o que está na direita
# resultado da expressão abaixo: False
print(f'Saldo é menor que saque? {saldo < saque}')

# resultado da expressão abaixo: False
print(f'Saldo é menor ou igual ao saque? {saldo <= saque}')
print('')

# operadores de atribuição

print('Operadores de atribuição')
print('')

# a variável saldo foi criada algumas linhas acima, aqui ela tá recebendo outro valor (sobrescrever)
saldo = 700
print(f'Saldo: {saldo}')

# atribuição com adição
saldo += 300
print(f'Novo Saldo - adicionou 300: {saldo}')

# atribuição com subtração
saldo -= 500
print(f'Novo Saldo - subtraiu 350: {saldo}')

# atribuição com multiplicação
saldo *= 3
print(f'Novo Saldo - multiplicou por 3: {saldo}')


# atribuição com divisão inteira e comum
saldo //= 5
print(f'Novo Saldo - dividiu por 5 - parte inteira: {saldo}')

saldo /= 2
print(f'Novo Saldo - dividiu por 2: {saldo}')

# atribuição com módulo
saldo %= 4
print(f'Novo Saldo - dividiu por 4 - pegou o resto: {saldo}')
print('')

# operadores lógicos

print('Operadores lógicos')
print('')

# relembrando operadores de atribuição pra contextualizar

saldo = 1000
saque = 200
limite = 100

print(f'Saldo: {saldo}')
print(f'Saque: {saque}')
print(f'Limite: {limite}')
print('')

# True
print(f'Saldo maior ou igual a saque? {saldo >= saque}')

# False
print(f'Saque menor ou igual a limite? {saque <= limite}')

# operador E
# juntamos as 2 perguntas acima numa mesma expressão com o operador E
# resultado False, pois os dois (ou mais) lados precisam ser verdadeiros 
# para o resultado ser verdadeiro
print('Saldo maior ou igual a saque E Saque menor ou igual a limite?')
print(saldo >= saque and saque <= limite)

# operador OU
# juntamos as 2 perguntas acima numa mesma expressão com o operador OU
# resultado True, pois apenas um dos lados precisa ser verdadeir
# para o resultado ser verdadeiro
print('Saldo maior ou igual a saque OU Saque menor ou igual a limite?')
print(saldo >= saque or saque <= limite)

# operador negação NOT

contatos_emergencia = []

# Saída abaixo True
# ele 'pergunta' mil é maior que mil e quinhentos
# resposta é Não (False)
# E aí ele nega, portanto Vira True
print(not 1000 > 1500)

# Saída abaixo True
# a variável foi inicializada como lista vazia
# lista vazia, string vazia são avaliados como False
# negação de False é True
print(not contatos_emergencia)

# Saída abaixo False
# String com conteúdo é True
# a negação vira False
print(not 'saque 1500;')

# Saída abaixo True
# a variável foi inicializada como string vazia
# # como já dito acima sobre lista ou string vazia: são avaliados como False
# negação de False é True 
print(not '')

# parênteses ajuda na legibilidade
saldo = 1000
saque = 250
limite = 200
conta_especial = True

# tudo sem parênteses, difícil de ler
# saída = True
print(saldo >= saque and saque <= limite or conta_especial and saldo >= saque)

# agora com parênteses, fica mais fácil de ler
# saída = True
print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))
print('')

# operadores de identidade

print('Operadores de identidade')
print('')

curso = 'Curso de Python'
nome_curso = curso

saldo, limite = 200, 200

# True
print(curso is nome_curso)

# False
print(curso is not nome_curso)

# True = não entendi pq, na minha mente seria False
# mas ok, agora não vou parar por isso
# vou continuar sabendo disso e pesquisar
print(saldo is limite)
print('')

# operadores de associação

print('Operadores de associação')
print('')

curso = 'Curso de Python'
frutas = ['Uva', 'Pera', 'Limão', 'Melão']
saques = [1500, 100]
carros = ['Gol', 'Uno', 'Up', 'Fox', 'Ka', 'Celta']
times = ['Palmeiras', 'Real Madrid', 'Bayern de Munique', 'Milan']

# True
print('Python' in curso)

# True
print('maçã' not in frutas)

# False
print(200 in saques)





