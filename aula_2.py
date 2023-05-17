# Aula 2 - Mulheres em dados 
# O objetivo de controlar um fluxo pode variar bastante:

#"se a temperatura estiver acima de 30 graus Celsius, ligue o ar condicionado"
#"enquanto a temperatura estiver acima de 25 graus Celsius, ligue o ventilador"
#"para cada item na lista de compras, adicione o item ao carrinho de compras"
# E como seria no Python?


# se a temperatura estiver acima de 30 graus Celsius, ligue o ar condicionado"
x = 31
if x > 30:
  print("Ligue o ar condicionado")

#se a temperatura não estiver acima de 30 graus Celsius, não ligue o ar condicionado"
x = 29
if x > 30:
  print("Ligue o ar condicionado")
else:
  print("Não ligue o ar condicionado")
  
  
#se a temperatura estiver entre 25 e 30 graus Celsius, ligue o ventilador"
x = int(input("Digite a temperatura: "))
if 25 <= x <= 30:
    print("Ligue o ventilador")
elif x > 30:
    print("Ligue o ar condicionado")
else:
  print("Não ligue o ar condicionado")
  
# Digite a temperatura: 24
# Não ligue o ar condicionado
#"enquanto a temperatura estiver acima de 25 graus Celsius, ligue o ventilador"
x = 20
while x < 25:
  print("Não ligue o ventilador")
  print(x)
  x += 1  
print(x, "Agora podemos ligar o ventilador")

#"para cada item na lista de compras, adicione o item ao carrinho de compras"
lista = ['trigo','leite','ovos','manteiga']
carrinho = []
print("Itens no carrinho: ",carrinho)
for i in lista:
  carrinho.append(i)
  print(carrinho)
print("Compras feitas: ",carrinho)

## Apenasa um test

lista = ['trigo','leite','ovos','manteiga']
carrinho = []
print("Itens no carrinho: ",carrinho)
for i in lista:
  carrinho.append(i)
  print(carrinho)
print("Compras feitas: ",carrinho)

