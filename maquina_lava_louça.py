import time

ligado = False
tempo = 0
temperatura = 0

def ligar(novo_tempo,nova_temperatura):
    global ligado, tempo, temperatura
    if not ligado:
        ligado = True
        tempo = novo_tempo
        temperatura=  nova_temperatura
        print(f'maquina de lavar louças ligado por {tempo} segundos na temperatura {temperatura} ')
        iniciar_cronometro(tempo)
        desligar()
    else:
        print('a maquina de lavar louças ja esta ligado')

def desligar():
    global ligado
    if ligado:
        ligado = False
        print('a maquina de lavar louças esta desligado')
    else:
        print('a maquina de lavar louças esta desligado')

def status():
    if ligado:
        print(f'tempo: {tempo} segundos s/n temperatura {temperatura}')
    else:
        print('a maquina de lavar louças esta desligado')

def iniciar_cronometro(segundos):
    while segundos>0:
        print(f'tempo restante : {segundos} segundos',  end="\r")
       
        time.sleep(1)
        segundos -=  1 
    print(' \n tempo esgotado')

escolha = int(input(" oque você deseja lavar: vidro(1), plastico(2) e metal(3)"))

if escolha==1:
    def vidro():
        ligar(120, 100)

    vidro()

elif escolha==2:
    def plastico():
       ligar(60, 21)

    plastico()

elif escolha==3:
    def metal():
        ligar(120, 30)

    metal()