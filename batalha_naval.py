Python

import random

#CONFIGURACOES
TAMANHO = 5
QUANTIDADE_NAVIOS = 3
TENTATIVAS = 10

#CRIAR TABULEIRO VAZIO
tabuleiro = []
for i in ranger(TAMANHO):
    Linha = []
    for j in ranger(TAMANHO):
        Linha.append("-")
    tabuleiro.append(linha)

#posicionar navios aleatoriamente
navios = []
while len (navios) < QUANTIDADE_NAVIOS:
     linha = random.randint(0, TAMANHO - 1)
     coluna = random.randint(0, TAMANHO -1)
     if (linha, coluna) not in navios:
        navios.append((linha, coluna))

#Funcao para mostrar o tabuleiro 
def mostrar_tabuleiro():
    print("\n 0 1 2 3 4")
    for i in range(TAMANHO):
        print(i, end=" ")
        for j in range(TAMANHO):
            print(tabulero[i][j], end=" ")
        print()


# JOGO
print(":ship: BATALHA NAVAL :ship:")
print(f"voce tem (TENTATIVAS) tentativas para afundar {QUANTIDADE_NAVIOS}
navios!")

acertos = 0
tentativas_restantes = TENTATIVAS

while tentativas_restantes > 0 and acertos <QUANTIDADES_NAVIOS:
   mostrar_tabuleiro()

try:
   linho = int(imput("Digite a linha (0-4): "))
   coluna = int(input("Digite a coluna (0-4): "))
except ValueError:
   print("Digite apenas numeros!")
   continue

if Linha < 0 or linha >= TAMANHO or coluna <0 or coluna >= TAMANHO:
   print("posicao invalida!")
  continue

if tabuleiro[linha][coluna] != "-":
   print("voce ja tentou essa posicao!")
  continue

if (linha, coluna) in navios:
   print(":boom: acertou um navio!")
   tabuleiro[linha][coluna] = "X"
   acertos += 1
else:
   print(":ocean: Errou!")
   tabuleiro[linha][coluna] = "0"

 tentativas restantes -=1
 print(f"tentativas restantes: {tentativas_restantes}")

#Resultado final
if acertos ==  QUANTIDADE_NAVIOS:
   print(":trophy: PARABENS! Voce venceu!")
  else
 print(":skull: Fim de jogo! Voce perdeu,")
 print("Os navios estavam em:", navios)
