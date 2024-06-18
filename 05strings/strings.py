# criando string propositalmente com mix de maiúsculas e minúsculas
curso = 'pYtHoN' 
print(curso)
print(curso.upper())
print(curso.lower())
print(curso.title())

# eliminando espaços em branco

curso = '      Python    '
print(curso)
print(curso.strip())
print(curso.lstrip())
print(curso.rstrip())

# Junções e centralização

curso = 'Python'
print(curso.center(10, '#'))
print('.'.join(curso))


# Interpolação de strings
# Old style

nome = 'Paulo'
idade = 34
profissao = 'Programador'
linguagem = 'JavaScript'

print('Olá, me chamo %s. Tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s.' %(nome, idade, profissao, linguagem))

# método format - 1
print('Olá, me chamo {}. Tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.'.format(nome, idade, profissao, linguagem))

# método format - 2
print('Olá, me chamo {3}. Tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.'.format(linguagem,profissao,idade,nome, ))

# método format - 3
print('Olá, me chamo {nome}. Tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.'.format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

pessoa = {'nome' : 'Paulo', 'idade': 34, 'profissao': 'programador', 'linguagem': 'JavaScript'}

# método format - 4
print('Olá, me chamo {nome}. Tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.'.format(**pessoa))


# f-string
print(f'Olá, me chamo {nome}. Tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.')

# Formatando com f-string
PI = 3.14159

print(f'Valor de PI: {PI:.2f}')
print(f'Valor de PI: {PI:10.2f}')

# Fatiamento
nome = 'Paulo ilarde Oliveira Nascimento'

# P
print(nome[0])

# Paulo
print(nome[:5])

# Oliveira Nascimento
print(nome[13:])

# ilarde
print(nome[6:12])

#  lreOier
print(nome[5:20:2])

# Paulo ilarde Oliveira Nascimento
print(nome[:])

# otnemicsaN arievilO edrali oluaP
print(nome[::-1])


# Múltiplas linhas
# Usando três pares de aspas (simples ou duplas) conseguimos 
# fazer strings com mais de uma linha

# Aspas simples
linguagem = 'Python'

mensagem = f'''
Estou estudando a linguagem {linguagem}
{linguagem} é muito usada para Inteligência artificial
'''

print(mensagem)


# Aspas dupals
linguagem = "Python"

mensagem = f"""
Estou estudando a linguagem {linguagem}
{linguagem} é muito usada para Inteligência artificial
"""



print(mensagem)