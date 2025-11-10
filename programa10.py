# dict:> dicionarios.
#ato = dict(nome='obi-wan', idade=2)
gato = {'nome': 'obi-wan',
        
        'idade': 2
}
print(type(gato))
print(gato)

carro_1 = {
    'cor': 'vermelho',
    'ano': 2020,
    'marca': 'fiat',
    'ipva': True
}
print(carro_1)
print(carro_1['cor'])
print('tanque' in carro_1)  
del carro_1['marca']
#rint(carro_1['marca'])  # KeyError
print(len(carro_1))
print(list(carro_1))

carro_1['ano']  = 2007
print(carro_1['ano'])