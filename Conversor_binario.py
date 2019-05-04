#----------------------------------
#Criado por Rafael Augusto Hentz
#2019
#IFC Campus Concórdia
#----------------------------------
y = '' #Cria uma string vazia
x = float(input('DIgite um número: '))#Pede o número desejado
while x > 0: #Verifica se deve parar de rodar
  if x % 2 == 0:#Pega e adiciona o 0 na string caso o número for par naquele momento
    y = '0' + str(y)
    x = x / 2 #Troca o número
  else:
    y = '1' + str(y)#Adiciona um na string caso for ímpar
    x = x - 1#Diminuium para poder dividir por 2
    x = x / 2
print('O código em binário do número digitado é {}'.format(y))