# ---- Aula 01 tipos de dados

print(1 + 10)
print(1.5 + 2)
print(True)
print(False)
print('Palmeiras eu te amo.')

# ---- Aula 02 modo interativo e funções 'dir' e 'help'
# permite editar o código direto no terminal, sem mexer no arquivo
# não consigo formular algo para o dir , vou ler o slide depois e ver se escrevo algo
# já o help mostra uma documentação básica do que tem disponível na linguagem


# ---- Aula 03 variáveis e constantes
# variáveis armazenam valores que podem mudar durante a execução do programa
# constantes guardam valores que não podem mudar 

# formas de declarar variáveis

idade = 34
nome = 'Paulo'
print(f'Meu nome é {nome} e eu tenho {idade} anos')

# ele colocou parênteses, mas é opcional. funciona com ou sem

nome1, idade1 = ('Pedro', 29)
print(f'Meu nome é {nome1} eu tenho {idade1} anos' )

# python permite mudar p valor de variáveis

idade = 35

print(idade)

# nome auto-explicativo, isso é boa prática
# nome composto segue a convenão sanke case

limite_saque_diario = 5000

# nomes abaixo são ruins, pois não epxlicam o que a variável faz / pra que serve
a = 10
x = 'Palmeiras'
lim_saq_di = 1000

# constantes são escritas com letra maiúscula

BRAZILIAN_STATES = ['SP', 'RJ', 'MG']
print(BRAZILIAN_STATES)

# ---- Aula 04 Conversão de tipos

# em geral precisamos mudar o tipo de dados para fazer operações
# exemplo comum: quando o usuário digita na tela uma quantidade (de produto por exemplol.)
# o valor digitado é lido como string. e aí precisamos conerter para o tipo número para fazer contas

# convertendo do tipo inteiro para float (número com casa decimal, ou ponto flutuante) 

preco = 10 
print('Preço no fotmato inteiro')
print(preco)
# saída acima = 10


preco = float(preco)
print('Preço no fotmato float')
print(preco)
# saída acima = 10.0

# outra forma de converter para float
# basta fazer uma conta de divisão que converte já
# funciona também se dividir por um, eu testei

preco =  10 / 2
print('Preço no fotmato float')
print(preco)
# saída acima = 5.0



# convertendo do float (número com casa decimal, ou ponto flutuante) para tipo inteiro 

preco = 10.3 
print('Preço no fotmato float')
print(preco)
# saída acima = 10.3


preco = int(preco)
print('Preço no fotmato inteiro')
print(preco)
# saída acima = 10.3

# assim como converte de int pra float dividindo, o contrário tbm acontece
# converter para int dividindo tem que usar duas barras

preco = 20
print('Preço no fotmato inteiro')
print(preco)

# conversão para o tipo float usando divisão

print('Preço no fotmato float, covertido ao fazer uma divisão')
print(preco / 2)
# saída no formato float, independente do valor do preço antes da divisão

print('Preço no fotmato inteiro, também covertido ao fazer uma divisão')
print(preco // 2)
# pega a parte inteira da vivisão
# obs: vou pesquisar a definição certinha na documentação da linguagem

# convertendo de númerico pra string
# útil quando queremos exibir mensagens

preco = 10.5
idade = 30

# saída abaixo = o valor do preço mas no formato string
print(str(preco))

# saída abaixo = o valor do idade mas no formato string
print(str(idade))

# precisamos deixar mensagens no tipo string para conseguir formatar o que queremos exibir na tela
# o nome dado a essa operação de juntar strings é: concatenar

# outro jeito de formatar abaixo
texto = f'Idade: {idade}; Preço: {preco}'

print(texto)

# conversão de string para número
# mencionado no começo da explicação sobre conversão

preco = '10.5'
idade = '30'

preco = float(preco)
idade = int(idade)


# pode ocorrer erros de conversão por motivos diversos
# o exemplo utilizado no vídeo
# ele tenta converter a palavra python para float
# o erro aparece no terminal

# dá pra saber o tipo de uma variável usando o operador type

preco  = 20
# saída abaixo  = <class 'int'>
print(type(preco))

preco_str = str(preco)
# saída abaixo  = <class 'str'>
print(type(preco_str))

# ---- Aula 05 funções de entrada e saída

# pra quando o usuário vai digitar as informações necessárias para o funcionamento do programa
# acho difícil um programa não usar isso
# mas enfim
# qq programa onde vc vai comprar algo, 
# ou utilizar GPS, e pesquisa o endereço
# isso foram só exemplos que vieram na mente mais rápido

# obs:
# aqui estou usando apenas python, o input é digitado no terminal
# no curso da hashtag é usado o jupyter, o input aparece na parte de cima da tela
# acho interessante pontuar isso aqui
# pois na primeira vez que usei o jupyter eu não olhei pra parte de cima, e fiquei uns bons minutos travado

nome = input('Digite seu nome:')
print(nome)