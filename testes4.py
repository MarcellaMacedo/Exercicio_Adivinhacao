""""
for contador in range(1, 11):
    print(contador)
"""

#A função range possui os seguintes parâmetros:
#range(start, stop, [step])
#for contador in range(1,11,3):
#    print(contador)

"""
i = 1;
while(i <= 7):
    print(i)
    i = i + 1
    if(i == 5):
        break
"""

"""""
for i in range(1,8):
    if(i == 5):
        continue
    print(i)
"""

print("Ola, Sr.{1} {0}!".format("Cordeiro","Leonardo"))

nome = 'Matheus'
print(f'Meu nome é {nome}')

nome = 'Matheus'
print(f'Meu nome é {nome.lower()}')