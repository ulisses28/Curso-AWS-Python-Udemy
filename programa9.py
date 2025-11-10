# listas em python
ec2_ids = []
print(type(ec2_ids))

datas = [3, 14, 9, 22,7]
mamiferos =[
    'cachorro',
    'gato'
    'coelho'
]
aves = ['pardal', 'tucano', 'arara']
dados = ['anakin', 79, True]

animais = [mamiferos, aves]

#print(datas)
#print(mamiferos)
#print(aves)
#print(dados)
#print(animais)
partes_datas = datas
print(datas[1:4])
print(partes_datas)
print(partes_datas[-1])

print(animais[0][1])
print(animais[1][1] )
print('cachorro' in mamiferos)
print('jacare' in mamiferos)
print('jacare' not in mamiferos)
print([2, 4 ,6] + [9, 8,7])
print(len(mamiferos))
print(max(datas))
print(min(datas))

datas.append(31)
datas.append(1)
del datas[2]
print(datas)
datas.clear()
print(datas)    