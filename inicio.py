# teste estrutura de construção da sala, necessário determinar que o professor
# irá ficar em um dos lados do comprimento
print('Defina a distancia minima entre pessoas em metros:')
distancia_minima =  float(input())
print('Defina o numero de salas que estarão disponíveis:')
numero_sala = int(input())
matriz_lugares = []
matriz_salas = []
while numero_sala > 0:
    print('Defina a lagura da sala', numero_sala, 'em metros:')
    sala_largura =  float(input())
    while sala_largura <= distancia_minima :
        print ('Largura em metros menor que a minima! Insira novamente:')
        sala_largura =  float(input())
    print('Defina o comprimento da sala', numero_sala, 'em metros:')
    sala_comprimento =  float(input())
    while sala_comprimento <= distancia_minima :
        print ('Comprimento em metros menor que a minima! Insira novamente:')
        sala_comprimento =  float(input())
        while sala_comprimento <= distancia_minima *2 :
            print('Comprimento menor do que o possivel para inserir duas pessoas na sala')
            print('Distancia minima em metros', distancia_minima*2)
            sala_comprimento =  float(input())
    area_sala = sala_largura * sala_comprimento
    print('A área da sala é igual a:', area_sala, 'm²')
    #fim teste de construcao

    # inicio processo de distribuição da sala
    # O professor irá ocupar toda a area inicial à um minimo de distancia_minima
    # e a um maximo de 20% do tamanho total da sala sempre permitindo a inclusão
    # minima de 1 aluno
    print('determine um comprimento para a área do professor em metros:')
    comprimento_professor =  float(input())
    while comprimento_professor <= distancia_minima:
        print('Area do professor menor que a minima, insira novamente:')
        comprimento_professor =  float(input())
        while comprimento_professor > sala_comprimento*0.2 or (sala_comprimento - comprimento_professor) > distancia_minima:
            print('Area do professor excede limite maximo')
            comprimento_professor =  float(input())
    area_sala = area_sala - (comprimento_professor * sala_largura)
    sala_comprimento = sala_comprimento - comprimento_professor
    print('Area util disponivel restante:', area_sala)
    print('Largura restante:', sala_largura)
    print('Comprimento restante:', sala_comprimento)
    comprimento_disponivel = sala_comprimento
    largura_disponivel = sala_largura
    carteira_comprimento = 1.2
    carteira_largura = 0.8
    lugares_disp_c = 0
    lugares_disp_l = 0
    while sala_comprimento > carteira_comprimento:
        sala_largura = largura_disponivel
        print (lugares_disp_l)
        while sala_largura > carteira_largura:
            if sala_largura ==  largura_disponivel:
                sala_largura = sala_largura - carteira_largura
                lugares_disp_l = lugares_disp_l + 1
            else:
                sala_largura = (sala_largura-(carteira_largura+distancia_minima))
                lugares_disp_l = lugares_disp_l + 1
        if sala_comprimento == comprimento_disponivel:
            sala_comprimento = (sala_comprimento - carteira_comprimento)
            lugares_disp_c = lugares_disp_c + 1
        else:
            sala_comprimento = (sala_comprimento-(carteira_comprimento+distancia_minima))
            lugares_disp_c = lugares_disp_c + 1
    print('Largura restante:', sala_largura)
    print('Comprimento restante:', sala_comprimento)
    print('Lugares Disponíveis:', lugares_disp_l)
    numero_sala = numero_sala-1
    matriz_lugares.append(lugares_disp_l)
    matriz_salas.append(numero_sala)
print(matriz_lugares)

