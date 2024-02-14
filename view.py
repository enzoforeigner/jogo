from controller import *
from time import sleep
from os import system
from random import randint
def main():
    matriz_jogadores = [
        
    ]
    asteristicos = '\033[1;33m=-\033[m' * 10

    print('\033[1;37mEste jogo foi feito por uma equipa, composta por:\033[m')
    print('\033[1;31mEnzo Manuel\033[m')
    sleep(1)
    print('\033[1;33mFabio Manuel\033[m')
    sleep(1)
    print('\033[1;35mJavan Afonso\033[m')
    sleep(1)
    print('\033[1;34mCláudio Cunha\033[m')
    sleep(1)
    print('\033[1;32mBreno Quitunga\033[m')
    sleep(1)
    system('cls')
    
    print(f'{asteristicos}\033[1;4;31mBEM VINDO AO MONOPOLY GAME\033[m🎩{asteristicos}')
    musicajogo = 'Theme.mp3'
    tocar_musica_2_plano(musicajogo)
    while True:
        print("""
        \033[1;32m****\033[m \033[1;4;32mOpções\033[m \033[1;32m****\033[m
        \033[1;32mRJ\033[m - \033[1;32mRegistar Jogador\033[m
        \033[1;36mIJ\033[m - \033[1;36mIniciar Jogo\033[m
        \033[1;33mVJ\033[m- \033[1;33mVisualizar Jogadores registados\033[m
        \033[1;31mS\033[m - \033[1;31mSair\033[m""")
        
        opçao = input('Qual é a sua opção(\033[1;32mRJ\033[m/\033[1;36mIJ\033[m/\033[1;31mS\033[m)🤔?: ').strip()
        if opçao.upper() == 'RJ':
            system('cls')
            print(f'{asteristicos}\033[1;4;32mRegistar Jogador\033[m{asteristicos}')
            print('Coloque \033[1;32mRJ\033[m no inicio e depois o \033[1;32mnome do jogador\033[m')
            while True: 

                comandos = input('\033[1;35mInsira:\033[m ').split()

                if comandos[0].upper() == 'RJ':
                # ['RJ', Nome]

                    resultado = registar_jogador(matriz_jogadores, comandos[1])
                    if resultado == 2:
                        print('\033[1;4;33mAtingiu o número máximo de jogadores registados!\033[m')
                        print('\033[1;36mVoltará ao menu inicial\033[m')
                        tempo_de_espera = animacao_carregar(duration=1)
                        print(tempo_de_espera)
                        system('cls')
                        break
                        
                    elif resultado == 1:
                        print('\033[1;33mJogador já registado!\033[m')
                        pretenção = str(input('\033[1;36mPretende adicionar mais jogadores?\033[m[\033[1;32ms\033[m/\033[1;31mn\033[m]: '))
                        system('cls')
                        adicionar = adicionar_jogador(pretenção)
                        if adicionar == True:
                            system('cls')
                            break
                        elif adicionar == False:
                            print('\033[1;31mComando inválido!!!\033[m')
                            system('cls')
                            break
                    else:
                        matriz_jogadores = resultado
                        tempo_de_espera = animacao_carregar(duration=1)
                        print(tempo_de_espera)
                        print('\033[1;32mJogador registado com sucesso!\033[m')
                        pretenção= str(input('\033[1;36mPretende adicionar mais jogadores?\033[m[\033[1;32ms\033[m/\033[1;31mn\033[m]: '))
                        system('cls')
                        adicionar = adicionar_jogador(pretenção)
                        if adicionar == True:
                            system('cls')
                            break
                        elif adicionar == False:
                            print('\033[1;31mComando inválido!!!\033[m')
                            system('cls')
                            break
                else:
                    print('\033[1;4;31mComando Inválido!\033[m\n\033[1;32mTente novamente\033[m')        
            
        elif opçao.upper() == 'IJ':

                verificacao = verificar_jogador_iniciar(matriz_jogadores)
                if verificacao == False:
                    tempo_de_espera = animacao_carregar(duration=1)
                    print(tempo_de_espera)
                    system('cls')
                    print('\033[1;33mJogo iniciado!!!\033[m')
                    while True:
                        for jogador_atual in matriz_jogadores:
                            for chave, valor in jogador_atual.items():
                                if chave == 'Propriedades' and valor == []:
                                    valor = 0
                                    sleep(0.5)
                                print(f'\033[1;36m{chave}: {valor}\033[m', end=' ')
                            print()
                            sleep(0.5)
                            print(f'\033[1;4;32m{jogador_atual["Nome"]}\033[m sua vez de jogar')
                            sleep(0.5)
                            while input('Prima \033[1;4;35menter\033[m para lançar o 🎲: ') != '':
                                pass
                                system('cls') 
                            sleep(0.5)
                            somdado = 'Dado.mp3'
                            tocar_musica_2_plano(somdado)
                            sleep(1)
                            musicajogo = 'Theme.mp3'
                            tocar_musica_2_plano(musicajogo)
                            dado = lancamento_dado()
                            print(f'O jogador \033[1;32m{jogador_atual["Nome"]}\033[m lançou o 🎲 e obteve o número \033[1;4;33m{dado}\033[m')
                            sleep(0.5)                            
                            movimento_do_jogador = movimentar_jogador(jogador_atual,dado)
                            posicao_do_jogador = jogador_atual['Posição']
                            casa_atual = localizar_casa(posicao_do_jogador,Propriedades)
                            print(f'\033[1;32m{jogador_atual["Nome"]}\033[m está na propriedade \033[1;4;33m{casa_atual["Nome"]}\033[m🏡 que vale \033[1;33m{casa_atual["Preço"]}$\033[m')
                            sleep(0.5) 
                            dono = verificar_dono(jogador_atual,casa_atual)
                            if dono == True:
                                print(
                                f'A propriedade \033[1;4;33m{casa_atual["Nome"]}\033[m🏡 possui proprietário\n\033[1;32m{jogador_atual["Nome"]}\033[m deverá pagar o valor do aluguel: \033[1;33m{casa_atual["Valor aluguel"]}$\033[m ao \033[1;32m{casa_atual["Proprietário"]}\033[m')
                                receptor = patrao(casa_atual,matriz_jogadores)                                                             
                                pa = pagar_aluguel(receptor,jogador_atual,casa_atual)
                                if pa == True:
                                    sompa = 'PA.mp3'
                                    tocar_musica_2_plano(sompa)
                                    print(f'\033[1;32mAluguer de \033[m\033[1;4;33m{casa_atual["Nome"]}\033[m🏡 \033[1;32mpago com sucesso✅.\033[m')
                                    sleep(1.5)
                                    musicajogo = 'Theme.mp3'
                                    tocar_musica_2_plano(musicajogo)
                                else:
                                    print(f'\033[1;31mSaldo insuficiente\033[m❗\n\033[1;4;31mTerá que hipotecar ou vender uma casa❗\033[m ')
                                    opcao = ''
                                    while True:
                                        print("""
                                    \033[1;32m**** Opções ****\033[m
                                    \033[1;33mVC\033[m- \033[1;33mVender Casa\033[m💰
                                    \033[1;36mHP\033[m- \033[1;36mHipotecar Propriedade\033[m💸
                                    \033[1;31mDF\033[m- \033[1;31mDeclarar Falência\033[m💸📉""")
                                        if jogador_atual['Propriedades'] == []:
                                            print('\033[1;31mVocê não tem propriedades para hipotecar ou vender\033[m❗')
                                            jogador_eliminado = eliminar_jogador(jogador_atual,matriz_jogadores)
                                            if jogador_eliminado == True:
                                                print(f'\033[1;4;32m{jogador_atual["Nome"]}\033[m \033[1;31mfoi a falência\033[m❗❗❗')

                                        opcao = str(input('Qual a sua opção?🤔: ')).strip()
                                        if opcao.upper() == 'HP':
                                            print('Coloque o nome da propriedade')
                                            comando = input('Insira: ').strip()
                                            casa = comando                                         
                                            hp = hipotecar_propriedade_0_dinheiro(jogador_atual,casa,Propriedades)
                                            if hp == True:
                                                som_hp = 'HC.mp3'
                                                tocar_musica_2_plano(musicajogo)
                                                print(f'\033[1;32m{casa} hipotecada com sucesso!\033[m✅')
                                                sleep(2.5)
                                                musicajogo = 'Theme.mp3'
                                                tocar_musica_2_plano(musicajogo)
                                                if jogador_atual['Dinheiro'] >= casa_atual['Valor aluguel']:
                                                    print(f'\033[1;32mAgora você tem dinheiro suficiente para pagar o aluguel de {casa_atual["Nome"]}🏡\033[m')
                                                    pa = pagar_aluguel(receptor, jogador_atual, casa_atual)
                                                    if pa == True:
                                                        sompa = 'PA.mp3'
                                                        tocar_musica_2_plano(sompa)
                                                        print(f'\033[1;32mAluguer de \033[m\033[1;4;33m{casa_atual["Nome"]}\033[m🏡 \033[1;32mpago com sucesso✅.\033[m')
                                                        sleep(1.5)
                                                        musicajogo = 'Theme.mp3'
                                                        tocar_musica_2_plano(musicajogo)
                                                        break                                               
                                            else:
                                                print(f'\033[1;4;33m{casa}\033[m \033[1;34mjá foi hipotecada!\033[m🏡🔓')
                                        elif opcao.upper() == 'VC':
                                            print('Coloque o nome da propriedade')
                                            comando = input('Propriedade:').strip()
                                            casa = comando       
                                            vc = vender_casa_0_dinheiro(jogador_atual,casa,Propriedades)
                                            if vc == True:
                                                som_vc = 'VC.mp3'
                                                tocar_musica_2_plano(musicajogo)
                                                print(f'\033[1;34mUma casa foi vendida!\033[m')
                                                sleep(1.25)
                                                musicajogo = 'Theme.mp3'
                                                tocar_musica_2_plano(musicajogo)
                                                if jogador_atual['Dinheiro'] >= casa_atual['Valor aluguel']:
                                                    print(f'\033[1;32mAgora você tem dinheiro suficiente para pagar o aluguel de {casa_atual["Nome"]}🏡\033[m')
                                                    pa = pagar_aluguel(receptor, jogador_atual, casa_atual)
                                                    if pa == True:
                                                        sompa = 'PA.mp3'
                                                        tocar_musica_2_plano(sompa)
                                                        print(f'\033[1;32mAluguer de \033[m\033[1;4;33m{casa_atual["Nome"]}\033[m🏡 \033[1;32mpago com sucesso✅.\033[m')
                                                        sleep(1.5)
                                                        musicajogo = 'Theme.mp3'
                                                        tocar_musica_2_plano(musicajogo)
                                                        break                                                        
                                            else:
                                                print(f'\033[1;31mNão há casas em {casa} para vender\033[m')                                       
                                        elif opcao.upper() == 'DF':
                                            print(f'\033[1;4;32m{jogador_atual["Nome"]}\033[m \033[1;31mDECLAROU FALÊNCIA\033[m❗❗❗')    
                                            jogador_eliminado = eliminar_jogador(jogador_atual,matriz_jogadores,Propriedades)
                                            if jogador_eliminado == True:
                                                print(f'\033[1;4;32m{jogador_atual["Nome"]}\033[m \033[1;31mESTÁ BASTANTE CALCINADO\033[m❗❗')
                                                break
                                                
                                        
                                    

                                sleep(0.5) 
                                opcao = ''
                                while True:
                                    print("""
                                \033[1;32m**** Opções ****\033[m
                                \033[1;36mIJ\033[m- \033[1;36mInformações Jogador\033[mℹ️
                                \033[1;37mPS\033[m- \033[1;37mPara Passar ao Próximo\033[m⏭️
                                \033[1;31mDF\033[m- \033[1;31mDeclarar Falência\033[m💸📉""")
                                    opcao = str(input('Qual a sua opção?🤔: ')).strip()
                                    if opcao.upper() == 'IJ':
                                        print(jogador_atual)
                                    elif opcao.upper() == 'DF':
                                        print(f'\033[1;4;32m{jogador_atual["Nome"]}\033[m \033[1;31mDECLAROU FALÊNCIA\033[m❗❗❗')
                                        jogador_eliminado = eliminar_jogador(jogador_atual,matriz_jogadores,Propriedades)
                                        if jogador_eliminado == True:
                                            print(f'\033[1;32m{jogador_atual["Nome"]}\033[m \033[1,33mestás mais que calcinado\033[m❗❗❗') 
                                        sleep(1.5)
                                        break                                               
                                    elif opcao.upper() == 'PS':
                                        break                                   
                                    else:
                                        print('\033[1;31mComando invalido\033[m❗\n\033[1;33mTente Novamente\033[m')
                                system('cls')  
                            else:
                                propriedade_vazia = sem_dono(casa_atual)
                                if propriedade_vazia == True:
                                    opcao = ''
                                    while True:
                                        print("""
                                        \033[1;32m**** Opções ****\033[m
                                        \033[1;33mCP\033[m- \033[1;33mComprar Propriedade\033[m🏡
                                        \033[1;36mIJ\033[m- \033[1;36mInformações Jogador\033[mℹ️
                                        \033[1;37mPS\033[m- \033[1;37mPara Passar ao Próximo\033[m⏭️
                                        \033[1;31mDF\033[m- \033[1;31mDeclarar Falência\033[m💸📉""")
                                        opcao = str(input('Qual a sua opção?: ')).strip()
                                        if opcao.upper() == 'CP':
                                            cp = comprar_propriedade(jogador_atual,casa_atual)
                                            if cp == 0:
                                                som_comprar_casa = 'CP.mp3'
                                                tocar_musica_2_plano(som_comprar_casa)
                                                print(f'\033[1;32mA propriedade\033[m \033[1;33m{casa_atual["Nome"]}🏡\033[m \033[1;32mfoi comprada com sucesso!\033[m✅')
                                                sleep(2)
                                                musicajogo = 'Theme.mp3'
                                                tocar_musica_2_plano(musicajogo)
                                            elif cp == 2:
                                                print(f'\033[1;31mNão possui dinheiro suficiente para comprar\033[m \033[1;4;33m{casa_atual["Nome"]}🏡\033[m❌💸')
                                            elif cp == 1:
                                                print(f'\033[1;31mJá comprou\033[m \033[1;4;33m{casa_atual["Nome"]}🏡\033[m❌💸')
                                            
                                        elif opcao.upper() == 'IJ':
                                            print(jogador_atual)
                                        
                                        elif opcao.upper() == 'DF': 
                                            print(f'\033[1;4;32m{jogador_atual["Nome"]}\033[m \033[1;31mDECLAROU FALÊNCIA\033[m❗❗❗')                                         
                                            jogador_eliminado = eliminar_jogador(jogador_atual,matriz_jogadores,Propriedades)
                                            if jogador_eliminado == True:
                                                print(f'\033[1;32m{jogador_atual["Nome"]}\033[m \033[1,33mestás mais que calcinado\033[m❗❗❗')
                                            sleep(1.5)
                                            break

                                        elif opcao.upper() == 'PS':
                                            break
                                        else:
                                            print('\033[1;31mComando invalido❗\nTente Novamente\033[m')
                                    system('cls')  
                                else:
                                    sleep(0.5) 
                                    opcao = ''
                                    while True: 
                                        print("""
                                        \033[1;32m**** Opções ****\033[m
                                        \033[1;32mCC\033[m- \033[1;32mConstruir Casa\033[m🏡
                                        \033[1;36mHP\033[m- \033[1;36mHipotecar Propriedade\033[m💸
                                        \033[1;35mDP\033[m- \033[1;35mDesipotecar Propriedade\033[m🏡🔓     
                                        \033[1;33mVC\033[m- \033[1;33mVender Casa\033[m💰
                                        \033[1;36mIJ\033[m- \033[1;36mInformações Jogador\033[mℹ️
                                        \033[1;37mPS\033[m- \033[1;37mPara Passar ao Próximo\033[m⏭️
                                        \033[1;31mDF\033[m- \033[1;31mDeclarar Falência\033[m💸📉""")
                                        sleep(0.5) 
                                        opcao = str(input('Qual a sua opção🤔?: '))
                                        
                                        if opcao.upper() == 'CC':
                                            cc = construir_casa(jogador_atual,casa_atual)
                                            if cc == 0:
                                                somcc = 'CC.mp3'
                                                tocar_musica_2_plano(somcc)
                                                print(
                                                f'\033[1;32mUma nova casa foi construida, resultando em um total de\033[m  \033[1;33m{casa_atual["Numero de casas"]}\033[m \033[1;32mpropriedade/s para \n{casa_atual["Nome"]}\033[m')
                                                sleep(2.5)
                                                musicajogo = 'Theme.mp3'
                                                tocar_musica_2_plano(musicajogo)
                                            elif cc == 1:
                                                print(f'\033[1;32mConstruiu o número máximo de casas🏡🏡🏡🏡🏡 para\033[m \033[1;4;33m{casa_atual["Nome"]}\033[m')                                              
                                            elif cc == 2:
                                                print(f'\033[1;31mNão possui dinheiro suficiente para construir casa\033[m \033[1;4;33m{casa_atual["Nome"]}🏡\033[m❌💸')            
                                        elif opcao.upper() == 'HP':                                         
                                            hp = hipotecar_propriedade(jogador_atual,casa_atual)
                                            if hp == True:
                                                som_hp = 'HC.mp3'
                                                tocar_musica_2_plano(som_hp)
                                                print(f'{casa_atual["Nome"]} \033[1;32mhipotecada com sucesso!\033[m✅ recebeu \033[1;33m{casa_atual["Hipoteca"]}$\033[m')
                                                sleep(2.5)
                                                musicajogo = 'Theme.mp3'
                                                tocar_musica_2_plano(musicajogo)
                                            else:
                                                print(f'\033[1;4;33m{casa_atual["Nome"]}\033[m \033[1;34mjá foi hipotecada!\033[m🏡🔓')
                                        elif opcao.upper() == 'DP':                                          
                                            dp = desihpotecar_propriedade(jogador_atual,casa_atual)
                                            if dp == 0:
                                                som_dp = 'DC.mp3'
                                                tocar_musica_2_plano(som_dp)
                                                print(f'\033[1;4;33m{casa_atual["Nome"]}\033[m \033[1;32mdeshipotecada com sucesso\033[m✅, pagou \033[1;33m{casa_atual["Desipotecar"]}$\033[m')
                                                sleep(1.25)
                                                musicajogo = 'Theme.mp3'
                                                tocar_musica_2_plano(musicajogo)
                                            elif dp == 2:
                                                print(f'\033[1;31mNão possui dinheiro suficiente para desipotecar\033[m \033[1;4;33m{casa_atual["Nome"]}\033[m')
                                            elif dp == 1:
                                                print(f'\033[1;4;33m{casa_atual["Nome"]}\033[m \033[1;36mNão está hipotecada!\033[m🏡🆓')
                                        elif opcao.upper() == 'VC':
                                            vc = vender_casa(jogador_atual,casa_atual)
                                            if vc == True:
                                                som_vc = 'VC.mp3'
                                                tocar_musica_2_plano(som_vc)
                                                print(
                                                    f'\033[1;34mUma casa foi vendida!\033[m\n\033[1;34mAgora,\033[m \033[1;4;32m{casa_atual["Nome"]}\033[m \033[1;34mpossui um total de\033[m \033[1;4;33m{casa_atual["Numero de casas"]}\033[m \033[1;34mcasas\033[m🏡')
                                                sleep(1.25)
                                                musicajogo = 'Theme.mp3'
                                                tocar_musica_2_plano(musicajogo)
                                            else:
                                                print(f'\033[1;37mNão há casas em\033[m \033[1;4;32m{casa_atual["Nome"]}\033[m \033[1;37m para vender\033[m🤷‍♀️')
                                        elif opcao.upper() == 'IJ':
                                            print(jogador_atual)
                                        elif opcao.upper() == 'PS':
                                            break  
                                        elif opcao.upper() == 'DF':
                                            print(f'\033[1;32m{jogador_atual["Nome"]}\033[m \033[1;37mdDeclarou falência❗❗❗\033[m')
                                            jogador_eliminado = eliminar_jogador(jogador_atual,matriz_jogadores,Propriedades)
                                            if jogador_eliminado == True:
                                                print(f'\033[1;32m{jogador_atual["Nome"]}\033[m \033[1,33mestás mais que calcinado\033[m❗❗❗')
                                                sleep(1.5)
                                                break                                                                                
                                        else:
                                            print('\033[1;31mComando invalido❗\nTente Novamente\033[m')
                                    system('cls')
                        jogador_eliminado_auto = eliminar_jogador_auto(jogador_atual,matriz_jogadores,Propriedades)
                        if jogador_eliminado_auto == True:
                            print(f'\033[1;32m{jogador_atual["Nome"]}\033[m \033[1;31mfoi a falência\033[m❗❗❗')
                            sleep(2) 
                            system('cls')
                        vencedor1 = vencedor(matriz_jogadores)
                        jogador_vencedor = matriz_jogadores[-1]                          
                        if vencedor1 == True:
                            somwin = 'Win.mp3'
                            tocar_musica_2_plano(somwin)
                            print(f'\033[1;33mO vencedor do jogo foi\033[m \033[1;4;32m{jogador_vencedor["Nome"]}\033[m\n\033[1;33mMuitos parabéns!!!\033[m🏆🎉👏✨')
                            sleep(2)
                            break

                else:
                    print('\033[1;34mRegistre no \033[4mmin 2\033[m jogadores para poder iniciar o jogo\033[m')
                    sleep(1) 
                    system('cls') 
        
        elif opçao.upper() == 'VJ':
            tabela = visualizar_jogadores(matriz_jogadores)
            if tabela == False:
                print('\033[1;4;31mNão possui jogadores registados\033[m❗')            
            else:
                print(tabela)
            sleep(1)
            system('cls') 

        elif opçao.upper() == 'S':
            animacao_pontos()
            if animacao_pontos == True:
                pass
            pygame.mixer.music.stop()
            print("\r\033[1;32mFechamento concluído.\033[m✅")
            sleep(0.5)
            break           
                    
Propriedades =[
    {'Nome': 'Go', 'Posição':1},
    {'Nome': 'CampoGrande', 'Preço': 60000, 'Hipotecada': False, 'Hipoteca': 30000, 'Desipotecar': 30000, 'Proprietário':None, 'Numero de casas': 0, 'Construir': 30000, 'Valor aluguel': 2000 , 'Posição':2},
    {'Nome': 'Ferrão', 'Preço': 60000, 'Hipotecada': False, 'Hipoteca': 30000 ,'Desipotecar': 30000, 'Proprietário':None, 'Numero de casas': 0, 'Construir': 30000, 'Valor aluguel': 2000 , 'Posição':3},
    {'Nome': 'Almirante', 'Preço': 100000, 'Hipotecada': False, 'Hipoteca': 30000 ,'Desipotecar': 30000, 'Proprietário':None, 'Numero de casas': 0, 'Construir': 50000, 'Valor aluguel': 10000 , 'Posição':4},
    {'Nome': 'Todi', 'Preço': 100000, 'Hipotecada': False, 'Hipoteca': 30000 , 'Desipotecar': 30000,'Proprietário':None, 'Numero de casas': 0, 'Construir': 50000, 'Valor aluguel': 10000 , 'Posição':5},
    {'Nome': 'Julho', 'Preço': 100000, 'Hipotecada': False, 'Hipoteca': 30000 , 'Desipotecar': 30000,'Proprietário':None, 'Numero de casas': 0, 'Construir': 50000, 'Valor aluguel': 10000 , 'Posição':6},
    {'Nome': 'Combatentes', 'Preço': 160000, 'Hipotecada': False, 'Hipoteca': 30000 ,'Desipotecar': 30000, 'Proprietário':None,'Numero de casas': 0,'Construir': 80000, 'Valor aluguel': 14000 , 'Posição':7},
    {'Nome': 'Borges', 'Preço': 160000, 'Hipotecada': False, 'Hipoteca': 30000 ,'Desipotecar': 30000, 'Proprietário':None,'Numero de casas': 0,'Construir': 80000, 'Valor aluguel': 14000 , 'Posição':8},
    {'Nome': 'Roma', 'Preço': 160000, 'Hipotecada': False, 'Hipoteca': 30000 ,'Desipotecar': 30000, 'Proprietário':None, 'Numero de casas': 0, 'Construir': 80000, 'Valor aluguel': 14000 , 'Posição':9},
    {'Nome': 'Boavista', 'Preço': 200000, 'Hipotecada': False, 'Hipoteca': 30000 ,'Desipotecar': 30000, 'Proprietário':None, 'Numero de casas': 0, 'Construir': 100000, 'Valor aluguel': 20000 , 'Posição':10},
    {'Nome': 'República', 'Preço': 200000, 'Hipotecada': False, 'Hipoteca': 30000 ,'Desipotecar': 30000, 'Proprietário':None, 'Numero de casas': 0, 'Construir': 100000, 'Valor aluguel': 20000 , 'Posição':11},
    {'Nome': 'Bandeira', 'Preço': 200000, 'Hipotecada': False, 'Hipoteca': 30000 ,'Desipotecar': 30000, 'Proprietário':None, 'Numero de casas': 0, 'Construir': 100000, 'Valor aluguel': 20000 , 'Posição':12},
    {'Nome': 'Rua de Santa Catarina','Preço': 240000, 'Hipotecada': False, 'Hipoteca': 30000 ,'Desipotecar': 30000,'Proprietário':None, 'Numero de casas': 0,'Construir': 120000, 'Valor aluguel': 24000 ,'Posição':13},
    {'Nome': 'Rua de Santo Javan','Preço': 240000, 'Hipotecada': False, 'Hipoteca': 30000 ,'Desipotecar': 30000,'Proprietário':None,'Numero de casas': 0,'Construir': 120000, 'Valor aluguel': 24000 ,'Posição':14},
    {'Nome': 'Rua de Santa Xofela','Preço': 240000, 'Hipotecada': False, 'Hipoteca': 30000 ,'Desipotecar': 30000,'Proprietário':None, 'Numero de casas': 0,'Construir': 120000, 'Valor aluguel': 24000 ,'Posição':15},
    {'Nome': 'Rua de Santo António','Preço': 260000, 'Hipotecada': False, 'Hipoteca': 30000 ,'Desipotecar': 30000,'Proprietário':None, 'Numero de casas': 0,'Construir': 130000, 'Valor aluguel': 26000 ,'Posição':16},
    {'Nome': 'Rua da Tolobona','Preço': 260000, 'Hipotecada': False, 'Hipoteca': 30000 ,'Desipotecar': 30000,'Proprietário':None, 'Numero de casas': 0,'Construir': 130000, 'Valor aluguel': 26000 ,'Posição':17},
    {'Nome': 'Rua de Marroly','Preço': 260000, 'Hipotecada': False, 'Hipoteca': 30000 ,'Desipotecar': 30000,'Proprietário':None, 'Numero de casas': 0,'Construir': 130000, 'Valor aluguel': 26000 ,'Posição':18},
    {'Nome': 'Av da Liberdade', 'Preço': 280000, 'Hipotecada': False, 'Hipoteca': 30000 ,'Desipotecar': 30000,'Proprietário':None, 'Numero de casas': 0,'Construir': 140000, 'Valor aluguel': 28000 ,'Posição':19},
    {'Nome': 'Av de Fabio Ap', 'Preço': 280000, 'Hipotecada': False, 'Hipoteca': 30000 ,'Desipotecar': 30000,'Proprietário':None, 'Numero de casas': 0,'Construir': 140000, 'Valor aluguel': 28000 ,'Posição':20},
    {'Nome': 'Av Bagas Grandes', 'Preço': 280000, 'Hipotecada': False, 'Hipoteca': 30000 ,'Desipotecar': 30000,'Proprietário':None, 'Numero de casas': 0,'Construir': 140000, 'Valor aluguel': 28000 ,'Posição':21},
    {'Nome': 'Rua Augusta', 'Preço': 300000, 'Hipotecada': False, 'Hipoteca': 30000 ,'Desipotecar': 30000,'Proprietário':None,' Numero de casas': 0,'Construir': 150000, 'Valor aluguel': 30000 ,'Posição':22},
    {'Nome': 'Rua Foreigner', 'Preço': 300000, 'Hipotecada': False, 'Hipoteca': 30000 ,'Desipotecar': 30000,'Proprietário':None, 'Numero de casas': 0,'Construir': 150000, 'Valor aluguel': 30000 ,'Posição':23},
    {'Nome': 'Rua Alexandra', 'Preço': 300000, 'Hipotecada': False, 'Hipoteca': 30000 ,'Desipotecar': 30000,'Proprietário':None, 'Numero de casas': 0,'Construir': 150000, 'Valor aluguel': 30000 ,'Posição':24},
]