import numeroEscolhido

def jogar():
    print("*********************************")
    print("Bem-vindo ao jogo de Adivinhação!")
    print("*********************************")

    n = numeroEscolhido.numeroEscolhido()
    
    while not n.ja_ganhou():
        chute_str = input("Digite um número entre 1 e 100: ")
        
        try:
            chute = int(chute_str)
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        resultado = n.verificar_numero(chute)
        print(resultado)
    
    print(" ")
    print(" ")
    print("Quer jogar novamente? (s/n)")
    resposta = input().strip().lower()
    if resposta == 's':
        jogar()
    
    print(" ")
    print("Obrigado por jogar! Até a próxima.")
    print("Fim do jogo.")
    

if __name__ == "__main__":
    jogar()