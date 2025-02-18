import random
print("#######################################")
print("##### Bem-vindo ao Jogo da Forca! #####")
print("#######################################")
print("Você possui 10 tentativas\n você perde 1 delas caso chute uma letra e 2 caso chute a palavra")
print("Chutes certeiros de letra e palavras não gastam tentativas")
print("Chute a palavra corretamente para acertar")

def palavra_sorteio():
    with open("palavras.txt", "r", encoding= "utf-8") as lista_palavras:
        palavras = lista_palavras.readlines()
        palavra_aleatoria = random.choice(palavras).strip()
        return palavra_aleatoria
    
    
def dados_jogo():
    palavra_secreta = palavra_sorteio()
    letra_correta = ["_"] *len(palavra_secreta)
    letra_incorreta = []
    tentativas_sobrando = 10
    letra_digitada= ""
    palavra_chute= ""
    pergunta = ""
    
    return palavra_secreta, letra_correta, letra_incorreta, tentativas_sobrando, letra_digitada, palavra_chute,pergunta

def pergunta_resposta(pergunta):
    while True:
        pergunta = input("Quer tentar chutar a palavra? S/N").strip().lower()
        
        if pergunta == "s":
            return pergunta
        elif pergunta == "n":
            return pergunta
        else:
            continue
    
                    

def jogar_novamente(tentar,palavra_secreta):
    while True:
            print(f"A palavra era {palavra_secreta}!")
            print("S para tentar novamente e N para encerrar o jogo")
            tentar = input("S/N").lower().strip()
            if tentar == "s" or tentar == "n":
                return tentar
                
            else:
                print("resposta inválida")
                continue
def letra_verificar(letra):
    while True:
        letra =input("Digite uma letra").lower().strip()
        if len(letra) != 1 or letra.isalpha()== False:
            print("Não é letra ou mais de uma letra digitada")
            continue
        else:
            return letra

def chute_letra(palavra, lista_correta, lista_incorreta, tentativas,letra):
        while True:
                
                letra = letra_verificar(letra)
                
                if letra in lista_correta or letra in lista_incorreta:
                    print(f"A letra {letra} já foi digitada. Tente outra.")
                    print(f"Palavra atual: {' '.join(lista_correta)}")
                    print(f"Lista de letras incorretas: {', '.join(lista_incorreta)}")
                    continue
                    
                    
                elif letra in palavra:
                    print(f"A letra digitada está na palavra")
                    for indice,letra_palavra in enumerate (palavra) :
                        if letra_palavra == letra:
                            lista_correta[indice] = letra
                    print(f"Palavra atual: {' '.join(lista_correta)}")
                                
                else:
                    tentativas-=1
                    lista_incorreta.append(letra)
                    print(f"A letra {letra} não está na palavra secreta" )    
                    print(f"Tentativas restantes: {tentativas}")
                    print(f"Lista de letras incorretas: {', '.join(lista_incorreta)}")
                return tentativas  
                    
def chute_palavra(palavra,tentativas,lista_correta,lista_incorreta,chute,letra,pergunta):
    while chute_palavra != palavra:
        while True:
            if tentativas <= 0:
                return False
            tentativas=chute_letra(palavra, lista_correta, lista_incorreta, tentativas,letra)
            pergunta = pergunta_resposta(pergunta)
            if pergunta == "s":
                    chute=input("Insira seu chute aqui:").lower().strip()
                    if chute==palavra:
                        print("Parabéns Você ganhou o jogo da forca!!!!!")
                        print(f"Tentativas erradas até o acerto: {abs(tentativas-10)}")
                        print("       ___________      ")
                        print("      '._==_==_=_.'     ")
                        print("      .-\\:      /-.    ")
                        print("     | (|:.     |) |    ")
                        print("      '-|:.     |-'     ")
                        print("        \\::.    /      ")
                        print("         '::. .'        ")
                        print("           ) (          ")
                        print("         _.' '._        ")
                        print("        '-------'       ")
                        return chute
                    else:
                        
                        tentativas -=2
                        print(f"Você errou!")
                        print(f"Tentativas restantes:{tentativas}")
                        
            elif pergunta == "n":
                    print(f"Palavra atual: {' '.join(lista_correta)}")
                    print(f"Lista de letras incorretas: {' ,'.join(lista_incorreta)}")
                    
            
    
                
                
        
def sistema_jogo():
    while True:
        palavra_secreta,letra_correta,letra_incorreta,tentativas_sobrando,letra_digitada,palavra_chute,pergunta =dados_jogo()
        chute_palavra(palavra_secreta, tentativas_sobrando,letra_correta,letra_incorreta,palavra_chute,letra_digitada,pergunta)
        return palavra_secreta

def jogo_forca():
    tentar = "s"
    while tentar != "n":             
        palavra_secreta=sistema_jogo()
        tentar = jogar_novamente(tentar,palavra_secreta)
        
        
            
jogo_forca()
print("obrigado por jogar!")