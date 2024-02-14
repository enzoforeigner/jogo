import random
from view import *
import time
import sys
import pygame
import threading
#lista jogador
jogador = {'Nome': '', 'Dinheiro': 800000, 'Propriedades': [], 'Posição': 1}

#funções criadas para apoio:
#def para movimentar o jogador pelas casas
def movimentar_jogador(jogador, d):
    jogador['Posição'] += d
    if jogador["Posição"] > 24:
        jogador['Posição'] -= 23 
        jogador['Dinheiro'] += 100000
#def para lançar o dado
def lancamento_dado():
    lista = [1,2, 3, 4, 5, 6] 
    numer_dado = random.choice(lista)
    return numer_dado
#def para perguntar se quer adicionar ou não
def adicionar_jogador(a):
     if a.upper() == 'N':
         return True
     elif a.upper() != 'S':
         return False

#função para retornar ou localizar:
#def utilizada para localizar uma casa atravès da posição  
def localizar_casa(posicao_do_jogador,Propriedades):
    for propriedade in Propriedades:
        if posicao_do_jogador == propriedade['Posição']:
            return propriedade

def retornar_propriedade(nome_p, Propriedades):
    for propriedade in Propriedades:
        if nome_p == propriedade['Nome']:
            return propriedade

#funções utilizadas paradefenir o menu que irá aparecer:
#def para caso haja dono na propriedade
def verificar_dono(jogador,nome_p):
    if nome_p['Proprietário'] != None and nome_p['Proprietário'] != jogador['Nome'] and jogador['Posição'] == nome_p['Posição']:
        return True
    else:
        return False
#def para caso não haja dono
def sem_dono(nome_p):
    if nome_p['Proprietário'] == None:
        return True

#função registar jogador:
#def utilizada para registar jogadores        
def registar_jogador(matriz_jogadores, nome):
    #Verificar se o jogador existe
    if verificar_jogador(matriz_jogadores, nome) == True:
        return 1
    #verificar se passou do limite de jogadores registados
    elif len(matriz_jogadores) >= 4:
        return 2
    else:
        jogador = jogador = {'Nome': nome , 'Dinheiro': 800000, 'Propriedades': [], 'Posição': 1}
        matriz_jogadores.append(jogador)
        return matriz_jogadores
#def de verificação do jogador
def verificar_jogador(matriz_jogadores, nome):
    # jogador = [nome, pontuação]
    for jogador in matriz_jogadores:
        if jogador['Nome'] == nome:
            return True
    return False

#função iniciar jogo:
#def para verificar se possui o número minimo de jogadores para jogar
def verificar_jogador_iniciar(matriz_jogadores):
    if len(matriz_jogadores) < 2:
        return True
    else:
        return False

#função comprar casa:
#def para comprar propriedade
def comprar_propriedade(jogador,propriedade):   
    # Verificar se tem dinheiro suficiente
    if jogador['Dinheiro'] < propriedade.get('Preço', 0):
        return 2
    # Ver se a propriedade tem dono
    elif propriedade['Proprietário'] != None:
        return 1
    else:
        jogador['Dinheiro'] -= propriedade.get('Preço', 0)
        jogador['Propriedades'].append(propriedade['Nome'])
        propriedade['Proprietário'] = jogador['Nome']
        return 0

#função construir casa CC:
#def para construir casa
def construir_casa(jogador,propriedade): 
    #verificar se tem o númer max de casas permitido  
    if propriedade['Numero de casas'] > 5:
        return 1
    #verificar se tem dinheiro suficiente para construir
    elif jogador['Dinheiro'] < propriedade.get('Construir', 0):
        return 2
    else:
        jogador['Dinheiro'] -= propriedade.get('Construir', 0)
        propriedade['Numero de casas'] += 1
        propriedade['Construir'] *= 2
        propriedade['Valor aluguel'] *= 2
        return 0 

#função pagar aluguel PA:
#def para pagar aluguel
def pagar_aluguel(jogador_1,jogador_2,propiedade):
    #verificar se o dinheiro do jogador é suficiente para pagar aluguel   
    if jogador_2['Dinheiro'] < propiedade.get('Valor aluguel', 0):
        return False
    else:
        valor_aluguel = propiedade.get('Valor aluguel', 0)
        jogador_2['Dinheiro'] -= valor_aluguel
        jogador_1['Dinheiro'] += valor_aluguel
        return True
#def para retornar o proprietário que irá receber o pagamento do aluguel
def patrao(propriedade, matriz_jogadores):
    for jogador in matriz_jogadores:
        if propriedade['Proprietário'] == jogador['Nome']:
            return jogador 

#função hipotecar propriedade HP:
#def para hipotecar propriedade
def hipotecar_propriedade(jogador,propriedade):
    #verificar se a propriedade já foi hipotecada   
    if propriedade['Hipotecada'] == True:
        return False
    else:
        valor_hipoteca = propriedade['Hipoteca']
        jogador['Dinheiro'] += valor_hipoteca
        propriedade['Hipotecada'] = True
        return True

#função para desihpotecar propriedade DP:
#def para desihpotecar propriedade
def desihpotecar_propriedade(jogador,propriedade):
    #verificar se a propriedade está hipotecada para desipotecar
    if propriedade['Hipotecada'] == False:
        return 1
    #veerificar se o jogador tem dinheiro para desipotecar
    elif jogador['Dinheiro'] < propriedade['Desipotecar']:
        return 2
    else:
        valor_deshipotecar = propriedade['Desipotecar']
        jogador['Dinheiro'] -= valor_deshipotecar
        propriedade['Hipotecada'] = False
        return 0

#função para vender casa VC:
#def para vender casa
def vender_casa(jogador,propriedade):
    #verificar se a propriedade já tem o número mínimo de casas
    if propriedade['Numero de casas'] == 0:
        return False
    else:
        valor_casa = propriedade['Construir']
        propriedade['Numero de casas'] -= 1
        propriedade['Construir'] /= 2
        propriedade['Valor aluguel'] /= 2
        jogador['Dinheiro'] += valor_casa
        return True

#função para visualizar jogadores registados VJ:
def visualizar_jogadores(matriz_jogadores):
    if len(matriz_jogadores) <= 0:
        return False
    else:
        nomes_jogadores = []
        for jogador in matriz_jogadores:
            nomes_jogadores.append(jogador['Nome'])
        return nomes_jogadores

#função para declarar falência DF:
def eliminar_jogador(jogador,matriz_jogadores,Propriedades):
    for propriedade in Propriedades:
        if jogador['Nome'] == propriedade.get('Proprietário'):
            propriedade['Proprietário'] = None
            propriedade['Numero de casas'] = 0
    matriz_jogadores.remove(jogador)
    return True
       

#função para quando o jogador chega a falencia:
def eliminar_jogador_auto(jogador,matriz_jogadores,Propriedades):
    if jogador['Dinheiro'] <= 0:
        for propriedade in Propriedades:
            if jogador['Nome'] == propriedade.get('Proprietário'):
                propriedade['Proprietário'] = None
                propriedade['Numero de casas'] = 0
        matriz_jogadores.remove(jogador)
        return True

#função para achar o vencedor:
def vencedor(matriz_jogadores):
    if len(matriz_jogadores) == 1:
        return True
    
#funções gráficas:
#def para animação de carregando
def animacao_carregar(duration=1):
    end_time = time.time() + duration
    while time.time() < end_time:
        for cursor in '|/-\\':
            sys.stdout.write('\r' + '\033[1;37mProcessando\033[m ' + cursor)
            sys.stdout.flush()
            time.sleep(0.1)
    return ''

#def que cria um loop de três vezes, mas o valor da variável _ não é usado no  loop.
def animacao_pontos():
    for _ in range(3):
        sys.stdout.write("\r\033[1;33mFechando o jogo\033[m" + "\033[1;32m.\033[m" * (_ + 1))#Nessa parte do " "." * (_ + 1)" "se _ for 0, será um ponto; se _ for 1, serão dois pontos, e assim por diante.
        sys.stdout.flush()
        time.sleep(1)
    return True 

#Funções sonoras:
#def para tocar a música   
pygame.mixer.init()
def tocar_musica(som):
    pygame.mixer.init()
    pygame.mixer.music.load(som)
    pygame.mixer.music.play()

#def pata tocar a musica em segundo plano 
def tocar_musica_2_plano(arquivo_musica):
    thread = threading.Thread(target=tocar_musica, args=(arquivo_musica,))
    thread.start()
    return thread

#Funções para retornar a propriedade de acordo com o nome, utilizamos para o caso de ter que vender casa para pagar o aluguel
#def para hipotecar
def hipotecar_propriedade_0_dinheiro(jogador,nome_p,Propriedades):
    propriedade = retornar_propriedade(nome_p, Propriedades)   
    if propriedade['Hipotecada'] == True:
        return False
    
    elif propriedade['Proprietário'] != jogador['Nome']:
        return False
    
    else:
        valor_hipoteca = propriedade['Hipoteca']
        jogador['Dinheiro'] += valor_hipoteca
        propriedade['Hipotecada'] = True
        return True
    
#def para vender
def vender_casa_0_dinheiro(jogador,nome_p,Propriedades):
    propriedade = retornar_propriedade(nome_p, Propriedades)
    if propriedade['Numero de casas'] == 0:
        return False
    
    elif propriedade['Proprietário'] != jogador['Nome']:
        return False
    
    else:
        valor_casa = propriedade['Construir']
        propriedade['Numero de casas'] -= 1
        jogador['Dinheiro'] += valor_casa
        return True