import random 


def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt","r")
    palavras = []
    
    for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
    
    arquivo.close()
    
    aleatoria = random.randrange(0, len(palavras))
    palavra_secreta = palavras[aleatoria].upper()


    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou =  False
    erros = 0


    while(not enforcou and not acertou):
        chute = input("Qual é a letra?")
        chute = chute.strip().upper()
        
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
   
                index = index + 1
        else:
            erros = erros + 1
        enforcou = erros == 10
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        if(acertou):
            print("Você ganhou!")
        else:
            print("Você perdeu")
    
    

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
