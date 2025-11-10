
#ec2_ligado = True
#rds_ligado - False

#print(f'Estado do EC2: {ec2_ligado}  Estado do RDS: {rds_ligado}')

#print(not False)
# x y  and
# 0 0 0
# 0 1 0
# 1 0 0
# 1 1 1

#print(ec2_ligado not rds_ligado)

idade = 30
maior_de_idade = idade >= 18
profissao = 'Dev'
objetivo_cumprido = idade > 30 and profissao == 'Dev'

print(f"maior de idade: {maior_de_idade}")
print(f"objetivo cumprido: {objetivo_cumprido}")