# importância da indentação
# é esse recurso que o interpretador do python usa pra saber quando começa e terminam blocos de código

print('Importância de indentar o código')
print('')

def sacar(valor: float) -> None: # início do bloco do método
    saldo = 1000
    if saldo >= valor: # início do bloco if
        saldo -= valor
        print(f'Valor sacado: {valor}')
        print(f'Novo saldo: {saldo}')
    else:
        print('Saldo insuficiente.')
    # fim do bloco if
# fim do bloco do método

sacar(2000)


# estrutura de decisão
# elas servem para desviar o fluxo padrão do código

print('Estruturas de decisão')
print('')

print('If simples: se <condição for verdadeira> faça isso -> código a ser feito')
print('')

saldo = 20000.0
saque = 0
# comentei a linha abaixo pra não atrapalhar a execução do resto do programa
# saque = float(input('Informe o valor do saque: '))

if saldo >= saque:
    print('Saque realizado com sucesso!')

if saldo < saque:
    print('Saldo insuficiente!')

print('If/ else: se <condição for verdadeira> faça isso -> código ')
print('se não for verdadeira faça isso -> código ')
print('')

saldo = 20000.0
saque = 0
# comentei a linha abaixo pra não atrapalhar a execução do resto do programa
# saque = float(input('Informe o valor do saque: '))

if saldo >= saque:
    print('Saque realizado com sucesso!')
else:
    print('Saldo insuficiente!')

print('If/ elif / else: se <condição 1 for verdadeira> faça isso -> código ')
print('se <condição 2 for verdadeira> faça isso -> código ')
print('se não for verdadeira faça isso -> código ')
print('')

# comentei a linha abaixo pra não atrapalhar a execução do resto do programa
# opcao = int(input('Informe uma opção: \n [1] Sacar \n [2] Extrato: \n'))
opcao = 1
if opcao == 1:
    # comentei a linha abaixo pra não atrapalhar a execução do resto do programa
    # valor = float(input('Informe o valor do saque:'))
    valor = 0
    # TODO: implementar lógica para o saque
elif opcao == 2:
    print('Exibindo extrato')
else:
    print('Opção inválida')

print('')

print('If aninhado: quando a verificação precisa entrar mais um nível no fluxo de tomada de decisão:')
print('')

saldo = 20000.0
saque = 0
cheque_especial = 200
conta_normal = True
conta_universitaria = ''

if conta_normal:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
        
    elif saque <= (saldo + cheque_especial):
        print('Saque realizado com uso do cheque especial!')
    else:
        print('Saldo insuciente')
    print('')
elif conta_universitaria:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    else:
        print('Saldo insuciente')
    print('')


print('If ternário: faz o if numa mesma linha')
print('')

status = 'Sucesso' if saldo >= saque else 'Falha'

print(f'{status} ao realizar o saque!')

# estrutura de repetição
# elas servem para executar uma instrução repetidas vezes sem precisar reescrever o código

print('Estruturas de repetição')
print('')

# exemplo sem usar estrutura de repetição
# recebe um número do teclado e exiba os 2 números seguintes

# a = int(input('Digite um número: '))
a = 0
print(f'Numero digitado: {a}')
a += 1
print(f'Numero digitado + 1: {a}')
a += 1
print(f'Numero digitado + 2: {a}')


# Estrutura For

# comentei a linha abaixo pra não atrapalhar a execução do resto do programa

# texto = input('Informe um texto: ')
texto = ''
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end='')
else: 
    print()
    print('Executa no fim do laço')

# console [0, 1, 2, 3]
# aqui nós convertemos um range object em lista
print(list(range(4)))

# console range(0, 4)
print(range(4))

# Range com for

for numero in range(0, 11):
    print(numero, end=' ')


print('')

# Tabuada do 5
for numero in range(0, 51, 5):
    print(numero, end=' ')


# comando while
print('')
opcao = -1

while opcao != 0:
    opcao = int(input('[1] Sacar \n[2] Extrato \n[0] Sair \n'))

    if opcao == 1:
        print('Realizando Saque')
        # TODO: necessário implementar lógica para sacar, aqui é só exemplo didático
    elif opcao == 2:
        print('Exibindo extrato')
else:
    print('Obrigado por usar o sistema bancário, até mais!')


# while com break

while True:
    # comentei a linha abaixo pra não atrapalhar a execução do resto do programa
    # numero = int(input('Digite um número: '))
    numero = 10
    if numero == 10:
        break

    print(numero)


# For e break juntos

for numero in range(100):
    if numero == 12:
        break
    
    print(numero, end=' ')

print('')

# For e continue juntos

for numero in range(100):
    if numero % 2 == 0:
        continue
    
    print(numero, end=' ')

# while com break e continue juntos
print('')
while True:
    
    numero = int(input('Digite um número: '))
    
    if numero == 10:
        break

    if numero % 2 == 0:
        continue

    print(numero)