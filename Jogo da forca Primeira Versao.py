from random import choice


def jogo(palavra):   

    chances = 6
    alfabeto = list("abdcefghijklmnopqrstuvwxyz")
    tentativas = []

    while True:
        for letra in palavra:
            if letra in tentativas:
                print(letra, end=' ')
            else:
                print('_', end=' ')

        palpite = input(
            "\nDigite uma letra ou digite 'SAIR' para sair do programa!\n").lower()
        if palpite == "sair":
            break
        elif palpite not in alfabeto or palpite == '':
            print("Digite uma letra.\n")
            continue
        elif palpite in tentativas:
            print("\nVocê já disse essa letra antes. Tente novamente.\n")
            print(tentativas)
            print("Chances: ", chances)
            continue
        tentativas.append(palpite)
        if palpite in palavra:
            print("\nVocê acertou a letra.\n")            
        else:
            print("\nA palavra não possui essa letra. Tente novamente.")
            print(tentativas)
            print("Chances: ", chances)        
        chances -= 1
        if chances == -1:
            print("\nSuas chances acabaram. \n Game over.\n")
            print("A palavra era: ", palavra)
            break
        elif set(palavra).issubset(set(tentativas)):
            print("\nParabéns!!! Você descobriu a palavra.\n")
            break



vocabulario_Facil = ["livro", "celular", "doce", "musica", "copo", "agua"]
vocabulario_Intermediario = ["abacaxi", "parede",
                             "televisao", "tomada", "geladeira", "brinco"]
vocabulario_Dificil = ["grampeador", "naftalina",
                       "braguilha", "idiossincratico", "zigoto", "quinquagesimo"]

player= input("Insira o nome do seu player: \n").upper()
print(f"\nBEM-VIND {player} AO JOGO DA FORCA.\nBOA SORTE!\n")
print("\nREGRAS DO JOGO:\n 1. NÃO USAR ACENTO NAS PALAVRAS\n 2. NÃO USAR A LETRA 'Ç' \n ")

escolha_usuario = input("Selecione o nível de dificuldade: \nDigite 'Easy' para nível fácil \nDigite 'Medium' para nível médio \nDigite 'Hard' para nível difícil \nSua escolha: ").lower()
print("\n ")
print("------------------------------\n")
print("QUE COMECEM OS JOGOS!\n")
print("------------------------------\n")

if escolha_usuario == "easy":
    palavra = choice(vocabulario_Facil)
    jogo(palavra)
elif escolha_usuario == "medium":
    palavra = choice(vocabulario_Intermediario)
    jogo(palavra)
else:
    escolha_usuario == "hard"
    palavra = choice(vocabulario_Dificil)
    jogo(palavra)
