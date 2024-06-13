def fazer_perguntas():
    """
    Faz as perguntas ao usuário sobre o número de vitórias e derrotas
    e retorna o saldo e o elo baseado no saldo.
    """
    # Perguntas ao usuário
    vitoria = int(input("Qual número de vitórias? "))
    derrota = int(input("Qual número de derrotas? "))
    
    # Calcular o saldo
    saldo = vitoria - derrota
    
    # Determinar o elo
    if saldo <= 10:
        elo = 'Ferro'
    elif 10 < saldo <= 20:
        elo = 'Bronze'
    elif 20 < saldo <= 50:
        elo = 'Prata'
    elif 50 < saldo <= 80:
        elo = 'Ouro'
    elif 80 < saldo <= 90:
        elo = 'Diamante'
    elif 90 < saldo <= 100:
        elo = 'Lendário'
    elif saldo >= 101:
        elo = 'Imortal'
    else: 
        elo = 'Insira um valor válido'
    
    return saldo, elo

def main():
    # Determinar o saldo e o elo do jogador
    saldo, elo = fazer_perguntas()
    
    # Exibir resultado
    print(f'O Herói tem um saldo de {saldo} e está no nível {elo}')

# Executa o programa principal
if __name__ == "__main__":
    main()
