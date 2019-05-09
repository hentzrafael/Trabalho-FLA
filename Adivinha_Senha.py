
#Criado por Rafael Augusto Hentz
#2019
#IFC Campus Concórdia
#----------------------------------
#Jogo da mega senha. Com 5 dígitos
import random #Importa  a biblioteca random para gerar números aleatórios
import sys #Importa para sair do programa
#Variáveis
r1=random.randint(0,9);r2=random.randint(0,9);r3=random.randint(0,9);r4=random.randint(0,9);r5=random.randint(0,9)
comp='{}{}{}{}{}'.format(r1,r2,r3,r4,r5)
tentativas=0
numeros=0
usr=''
teste=0
global jogada
global expoente
global mostra
mostra=''
expoente=0
print('-=-'*10)
print('Vamos começar com o jogo')
print('-=-'*10)
while tentativas<10: #Para definir quantas chances ele terá, repetindo até acabarem
    usr=input('Digite a senha de 5 números: ')#Pede a senha com 5 dígitos, se for menor ou maior, repete
    if len(usr)>5 or len(usr)<5:
        print('Senha Inválida')
        continue
    while teste<5:#Testa os números digitados um a um para ver se estão na senha e em qual posição
        if usr[expoente]==comp[expoente] or usr[expoente]==comp[expoente] or usr[expoente]==comp[expoente] or usr[expoente]==comp[expoente] or usr[expoente]==comp[expoente] :
            mostra+=' +1 '#Adiciona quando o número estiver no local certo
        elif usr[expoente]== comp[0] or usr[expoente] == comp[1] or usr[expoente]==comp[2] or usr[expoente]==comp[3] or usr[expoente]==comp[4]:
            mostra+=' 0 '#Quando o número aparece na senha
        else:
            mostra+=' -1 '#Quando não aparece na senha
        expoente+=1
        teste+=1
    if usr==comp:#Verifica se o usuário ganhou
        print('Parabéns, você conseguiu em {} tentativas'.format(tentativas))
        sys.exit()#Sai do programa
    print('As dicas são:', mostra)#Mostra as dicas
    print('-=-'*10)
    tentativas+=1
    print('Já foram {} tentativas'.format(tentativas))#Mostra quantas tentativas foram
    print()
    #Zera as variáveis que terão que ter novos valores
    numeros=0
    mostra=''
    usr=''
    teste=0
    expoente=0
if tentativas >=10:#Mostra quando acabarem as chances
    print('Suas tentativas acabaram!')
