nome = 'ulisses'
sobrenome = 'de almeida'
idade = 'tem 35 anos'
dados_pessoais = nome + ' ' + sobrenome + ' ' + idade #concatenação
print(dados_pessoais)   
congratulacao = 'feliz'
situacao1 = 'natal'
situacao2 = 'ano novo'
mensagem1 = f"Tenha um {congratulacao} dia de {situacao1}" #f string
messagem2 = f"Tenha um {congratulacao} dia de {situacao2}"#f string
print(mensagem1)
print(messagem2)
versao = 'ABCD'
print
versao +='-10' #VERSÃO = VERSÃO + '-10'   
print(versao)
exite_feliz = 'feliz' in mensagem1 #verifica se a palavra feliz está na mensagem1
existe_infeliz = 'infeliz' in messagem2 #verifica se a palavra infeliz está na messagem2
print(exite_feliz)
print(existe_infeliz)
print(mensagem1[2:10])

print('Abcd')
print('Abcd'.lower())#converter para minusculo
print('Abcd'.upper())#converter para maiusculo

print('Abc'.find('b'))#encontra a posição da letra b 
print('Abc'.replace('b','X'))#substitui a letra A por X   