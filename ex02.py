# 
# autor: Michel
# data: 10/06/2025

# dada a função:
# y = x^2 + 3 * x + 8

# x é um parametro da função e y uma variável local
def funcao01(x):
  y = x ** 2 + 3 * x + 8 
  return y

# a função bhaskar01 recebe os coeficientes a, b e c
# da equação do segundo grau e retorna as raízes
def bhaskar01(a, b, c):
  delta = b**2 - 4*a*c # cálculo do delta
  # delta é o discriminante da equação do segundo grau
  # se delta for igual a zero, há uma raiz real
  # se delta for maior que zero, há duas raízes reais 
  if delta == 0:
    x1 = (-b + (delta)**(1/2)) / (2*a)
    x2 = x1  # se delta for igual a zero, as raízes são iguais
    # retorna apenas uma raiz, pois são iguais
    return x1, x2
  elif delta > 0:
    x1 = (-b + (delta)**(1/2)) / (2*a)
    x2 = (-b - (delta)**(1/2)) / (2*a)
    return x1, x2
  else:
    # se delta for menor que zero, não há raízes reais
    return f"não existe raiz, delta = {delta}"


# chamando a função funcao01
# valor = funcao01(2) # chamando a função com o valor 2
valor = funcao01(2)
# ou chamando a função com o valor informado pelo usuário
# o valor informado pelo usuário é convertido para inteiro
valor = funcao01(int(input("informe o valor de X: ")))

# imprimindo o resultado
print(f"Y = F(2) = {valor}")

# chamando a função bhaskar01
# a função bhaskar01 recebe os coeficientes a, b e c
# e retorna as raízes da equação do segundo grau
x1, x2 = bhaskar01(1, 5, 3)
print(f"Para os valores 1, 5 e 3")
print(f"X1 = {x1:.1f}") # formatando o resultado para uma casa decimal
print(f"X2 = {x2:.1f}") # variável x2 é a segunda raiz