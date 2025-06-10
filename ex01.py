# 
# autor: Michel
# data: 10/06/2025

# função somar
# a função 'somar' recebe dois valores e retorna a soma deles
#
def somar(valor1, valor2): 
  soma = valor1 + valor2 # soma é uma variável local
  return soma

# função / procedimento
# a função 'proc_somar' recebe dois valores e imprime a soma deles
# ela não retorna nada, apenas executa uma ação
def proc_somar(valor1, valor2):
  soma = valor1 + valor2
  print(f"soma = {soma}")


print("chamando a função")
# chamando a função somar
# a função 'somar' retorna um valor, que pode ser armazenado em uma variável
resultado = somar(5, 10)  
print(f"soma1 = {resultado}")

# ou pode ser usado diretamente
# sem armazenar o resultado em uma variável
print(f"soma2 = {somar(5, 10)}")

# chamando a função 'somar' de forma não comum, 
# porque o resultado não é armazenado
# isso não é uma boa prática, mas é possível
somar(5, 10) # não é comum

# armazenando o resultado em uma variável
recebe = somar(5, 10) # certo!
print()

# chamando o procedimento proc_somar
# o procedimento 'proc_somar' não retorna nada, apenas executa uma ação
print("chamando o procedimento / função")
proc_somar(5, 15) # certo!

# a pratica de não armazenar o resultado de uma função é comum
# mas não é comum para procedimentos, pois eles não retornam nada
# então, o procedimento é chamado apenas para executar uma ação
# e não para obter um resultado
receber = proc_somar(5, 15) # não é comum 
