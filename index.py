import numpy as np

# Dicionário com os valores das cartas. 'A' (Ás) vale 11 inicialmente.
valores = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

# Cria e embaralha o baralho:
naipes = ['Copas', 'Ouros', 'Paus', 'Espadas']
ranks = list(valores.keys())
baralho = [f'{r} de {n}' for n in naipes for r in ranks]
np.random.shuffle(baralho)

# Distribui as cartas iniciais:
mao_jogador = [baralho.pop(), baralho.pop()]
mao_dealer = [baralho.pop(), baralho.pop()]

def calcular_pontos(mao):
    pontos = sum(valores[carta.split()[0]] for carta in mao)
    # Se estourar 21 e tiver um Ás, muda o valor do Ás de 11 para 1
    if pontos > 21 and any('A' in carta for carta in mao):
        # Procura por Ases e subtrai 10 para cada um até a pontuação ficar abaixo de 21
        num_ases = sum(1 for carta in mao if 'A' in carta)
        while pontos > 21 and num_ases > 0:
            pontos -= 10
            num_ases -= 1
    return pontos

# Turno do Jogador:
jogador_ativo = True
while jogador_ativo:
    pontos_jogador = calcular_pontos(mao_jogador)
    print(f"\nSua mão: {mao_jogador} (Pontos: {pontos_jogador})")
    print(f"Dealer mostra: [{mao_dealer[0]}]")

    # Verifica se o jogador já perdeu ou ganhou:
    if pontos_jogador > 21:
        print("Vc estourou!")
        jogador_ativo = False # Encerra o turno do jogador
        continue # Pula para a próxima iteração, que vai sair do loop
    elif pontos_jogador == 21:
        print("Blackjack (ou 21...)!")
        jogador_ativo = False
        continue

    # Pede a ação do jogador:
    escolha = input("Quer (C)omprar ou (P)arar? ").strip().upper()

    if escolha == 'C':
        mao_jogador.append(baralho.pop())
    elif escolha == 'P':
        jogador_ativo = False
    else:
        print("Opção inválida. Tente novamente.")

# Turno do dealer e Resultado:
print("\n--- Fim de jogo ---")
pontos_jogador = calcular_pontos(mao_jogador)
print(f"Sua mão final: {mao_jogador} (Pontos: {pontos_jogador})")

# Se o jogador não estourou, é a vez do dealer jogar:
if pontos_jogador <= 21:
    # Dealer compra cartas até ter 17 ou mais pontos
    while calcular_pontos(mao_dealer) < 17:
        mao_dealer.append(baralho.pop())

    pontos_dealer = calcular_pontos(mao_dealer)
    print(f"Mão final do dealer: {mao_dealer} (Pontos: {pontos_dealer})")

    # Compara as pontuações e define o vencedor:
    if pontos_dealer > 21:
        print("Dealer estourou! vc venceu!")
    elif pontos_dealer >= pontos_jogador:
        print("O dealer venceu.")
    else:
        print("Parabéns, vc venceu!")
else:
    # Se o jogador já tinha estourado, ele perde automaticamente
    print("O dealer venceu, pq vc estourou.")