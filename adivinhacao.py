import random

# Função principal que executa o código por inteiro.
def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

# Algumas variáveis são declaradas: O número secreto, variando de 1 até 100 (o 101 é considerado o máximo não podendo
# ser o número em si) o total de tentativas é definido, para ser mudado dependendo da escolha do jogador, e o total
# máximo de pontos também, para ser diminuído dependendo das ações do jogador durante o jogo.
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

# O programa questiona qual será o nível de dificuldade, e uma simples sequência de if's determina o valor da
# variável tentativas.
    print("Qual nível de dificuldade?")
    print(numero_secreto)
    print("(1) Fácil (2) Médio (3) Difícil")

# O número digitado pelo jogador deve receber int() para deixar de ser uma string, sendo este o elemento retornado do imput().
    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

# O jogo em si utiliza do "for" para funcionar. O total de tentativas é utilizado para determinar quantas vezes o jogador
# o usuário poderá chutar um número, e é somado com 1, já que caso isso não acontecesse, o programa pararia antes de chegar
# no 1 em si.
    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

# Assim como a variável "nível", o chute também deve ser transformado de um valor string para int, e este valor chega
# a ser guardado em uma nova variável.
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)

# Um lembrete para o jogador, caso o número seja menor que 1 ou maior que 100, de que ele deve digitar o valor delimitado.
        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

# Comparação da variável para determinar o resultado.
        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

# Caso o jogador acerte, sua pontuação é informado e ele pode jogar novamente, caso queira. A função no início do
# código é utilizada para executá-lo caso a resposta seja sim. Para determinar a resposta do jogador, o valor inserido
# é guardado dentro de uma variável e então comparado com 1.
        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            denovo = int(input('Você deseja jogar novamente? (1) Sim (2) Não'))
            if (denovo == 1):
                jogar()
            else:
                total_de_tentativas = 0
                print("Fim do jogo")
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
# O else só é aplicado caso a variável "acertou" não seja comparável, ou seja, caso o jogador erre. Dessa forma, o
# programa procede testando se o número inserido foi maior ou menor (com os símbolos > e <) e a diferença é subtraída
# dos pontos, que passam pelo abs() para eliminar o sinal negativo, caso aplicável.

# Essa condição testa se o jogador chegou no final de suas tentativas, ou seja, se o total de tentativas é igual a 1.
# Caso aplicável, o jogador é informado de sua derrota e pode jogar novamente caso queira.
    if(rodada == total_de_tentativas):
        print('Você perdeu.')
        denovo = int(input('Você deseja jogar novamente? (1) Sim (2) Não'))
        if (denovo == 1):
            jogar()
        else:
            total_de_tentativas = 0
            print("Fim do jogo")

# Essa condição testa se o arquivo está sendo executado como principal ou não. Caso ele seja importado para outros
# arquivos, o mesmo não irá executar a não ser que seja chamado (pois está por inteiro dentro de uma função)
# Mas caso ele seja executado diretamente, então a função jogar() é chamada, e consequentemente, o código será executado.
if(__name__ == "__main__"):
    jogar()
