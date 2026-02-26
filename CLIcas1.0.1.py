import random


def play_round() -> bool:
    first = random.randint(0, 200)
    print(f"Первое число: {first}")
    print("Выбери:")
    print("  1 - следующее число будет больше")
    print("  2 - следующее число будет меньше")

    while True:
        choice = input("Твой выбор (1/2): ").strip()
        if choice in ("1", "2"):
            break
        print("Нужно ввести 1 или 2.")

    second = random.randint(0, 200)
    print(f"Второе число: {second}")

    if choice == "1":
        win = second > first
    else:
        win = second < first

    if win:
        print("Ты выиграл!")
    else:
        print("Ты проиграл.")

    return win


def main() -> None:
    print("Игра 'Больше / Меньше' (числа от 0 до 200)")
    print("Тебе показывается первое число,")
    print("ты выбираешь, будет ли следующее число больше или меньше.")
    print("Если угадал то побеждаешь, иначе — проигрываешь.")
    print()

    balance = 250
    print(f"Начальный баланс: {balance}")

    while True:
        print(f"\nТекущий баланс: {balance}")

       
        while True:
            bet_str = input("Сколько ставишь? ").strip()
            try:
                bet = int(bet_str)
            except ValueError:
                print("Нужно ввести целое число.")
                continue

            if bet <= 0:
                print("Ставка должна быть больше нуля.")
            elif bet > balance:
                print("Нельзя ставить больше, чем есть на балансе.")
            else:
                break

        win = play_round()

        if win:
            balance += bet
        else:
            balance -= bet

        print(f"Баланс после раунда: {balance}")

        if balance <= 0:
            print("У тебя закончились деньги. Игра окончена.")
            break

        
        while True:
            again = input("Хочешь сыграть ещё? (y/n): ").strip().lower()
            if again in ("y", "n", "yes", "no"):
                break
            print("Напишите пожалуйста или y или n")

        if again not in ("y", "yes"):
            print("Пока!")
            break


if __name__ == "__main__":
    main()

