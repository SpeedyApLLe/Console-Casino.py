import random
import tkinter as tk
from tkinter import ttk


START_BALANCE = 250


class HigherLowerGame(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Higher / Lower")
        self.resizable(False, False)

        
        self.balance: int = START_BALANCE
        self.current_bet: int = 0
        self.first_number: int | None = None

       
        self.balance_var = tk.StringVar()
        self.bet_var = tk.StringVar()
        self.first_var = tk.StringVar(value="-")
        self.second_var = tk.StringVar(value="-")
        self.message_var = tk.StringVar(
            value="Enter your bet and start the round."
        )

        self._build_ui()
        self._update_balance_label()

    def _build_ui(self) -> None:
       
        self.configure(bg="#f7f7f7")
        container = ttk.Frame(self, padding=16)
        container.grid(row=0, column=0, sticky="nsew")

        title_label = ttk.Label(
            container,
            text="Higher / Lower",
            font=("Segoe UI", 16, "bold"),
        )
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 12))

        
        balance_label = ttk.Label(
            container,
            textvariable=self.balance_var,
            font=("Segoe UI", 11),
        )
        balance_label.grid(row=1, column=0, columnspan=3, sticky="w")

      
        numbers_frame = ttk.Frame(container, padding=(0, 12, 0, 12))
        numbers_frame.grid(row=2, column=0, columnspan=3, sticky="ew")

        ttk.Label(
            numbers_frame,
            text="First:",
            font=("Segoe UI", 11),
        ).grid(row=0, column=0, padx=(0, 8), sticky="e")

        ttk.Label(
            numbers_frame,
            textvariable=self.first_var,
            font=("Segoe UI", 14, "bold"),
        ).grid(row=0, column=1, padx=(0, 24), sticky="w")

        ttk.Label(
            numbers_frame,
            text="Second:",
            font=("Segoe UI", 11),
        ).grid(row=0, column=2, padx=(0, 8), sticky="e")

        ttk.Label(
            numbers_frame,
            textvariable=self.second_var,
            font=("Segoe UI", 14, "bold"),
        ).grid(row=0, column=3, sticky="w")

       
        ttk.Label(
            container,
            text="Bet:",
            font=("Segoe UI", 11),
        ).grid(row=3, column=0, sticky="e", pady=(0, 8))

        bet_entry = ttk.Entry(container, textvariable=self.bet_var, width=10)
        bet_entry.grid(row=3, column=1, sticky="w", pady=(0, 8))

        self.start_button = ttk.Button(
            container,
            text="Start round",
            command=self._start_round,
        )
        self.start_button.grid(row=3, column=2, sticky="e", pady=(0, 8))

       
        self.higher_button = ttk.Button(
            container,
            text="Higher",
            command=lambda: self._make_guess("higher"),
            state="disabled",
        )
        self.higher_button.grid(row=4, column=0, pady=(0, 8), sticky="ew")

        self.lower_button = ttk.Button(
            container,
            text="Lower",
            command=lambda: self._make_guess("lower"),
            state="disabled",
        )
        self.lower_button.grid(row=4, column=1, pady=(0, 8), sticky="ew")

        quit_button = ttk.Button(
            container,
            text="Quit",
            command=self.destroy,
        )
        quit_button.grid(row=4, column=2, pady=(0, 8), sticky="ew")

        
        message_label = ttk.Label(
            container,
            textvariable=self.message_var,
            font=("Segoe UI", 10),
            foreground="#555555",
            wraplength=280,
        )
        message_label.grid(row=5, column=0, columnspan=3, sticky="w")

        
        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=1)
        container.columnconfigure(2, weight=1)

       
        bet_entry.focus_set()

    def _update_balance_label(self) -> None:
        self.balance_var.set(f"Balance: {self.balance}")

    def _start_round(self) -> None:
      
        bet_text = self.bet_var.get().strip()
        try:
            bet = int(bet_text)
        except ValueError:
            self.message_var.set("Bet must be an integer.")
            return

        if bet <= 0:
            self.message_var.set("Bet must be greater than zero.")
            return
        if bet > self.balance:
            self.message_var.set("Bet cannot exceed your balance.")
            return

        self.current_bet = bet
        self.first_number = random.randint(1, 100)
        self.first_var.set(str(self.first_number))
        self.second_var.set("-")

        self.message_var.set("Will the next number be higher or lower?")

       
        self.higher_button.config(state="normal")
        self.lower_button.config(state="normal")
        self.start_button.config(state="disabled")

    def _make_guess(self, guess: str) -> None:
        if self.first_number is None:
            return

        second = random.randint(1, 100)
        self.second_var.set(str(second))

        if guess == "higher":
            win = second > self.first_number
        else:
            win = second < self.first_number

        if win:
            self.balance += self.current_bet
            self.message_var.set("You won this round.")
        else:
            self.balance -= self.current_bet
            self.message_var.set("You lost this round.")

        self._update_balance_label()
        self.first_number = None

       
        if self.balance <= 0:
            self.balance = 0
            self._update_balance_label()
            self.message_var.set("Balance is zero. Game over.")
            self.higher_button.config(state="disabled")
            self.lower_button.config(state="disabled")
            self.start_button.config(state="disabled")
            return

     
        self.start_button.config(state="normal")
        self.higher_button.config(state="disabled")
        self.lower_button.config(state="disabled")

    def run(self) -> None:
        self.mainloop()


def main() -> None:
    app = HigherLowerGame()
    app.run()


if __name__ == "__main__":
    main()

import os
import random


RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
CYAN = "\033[36m"
GREEN = "\033[32m"
RED = "\033[31m"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_header(balance, bet=None):
    title = "БОЛЬШЕ / МЕНЬШЕ"
    line = "-" * 36
    print(CYAN + line + RESET)
    print(CYAN + f"| {BOLD}{title:<30}{RESET}{CYAN} |" + RESET)
    print(CYAN + line + RESET)
    print(f"{DIM}Баланс:{RESET} {BOLD}{balance}{RESET}")
    if bet is not None:
        print(f"{DIM}Ставка:{RESET} {bet}")
    print()


def play_round() -> bool:
    first = random.randint(1, 100)
    print(DIM + "-" * 36 + RESET)
    print(f"Первое число: {BOLD}{first}{RESET}")
    print()
    print("Выбери:")
    print("  1 - следующее число будет больше")
    print("  2 - следующее число будет меньше")

    while True:
        choice = input("Твой выбор (1/2): ").strip()
        if choice in ("1", "2"):
            break
        print("Нужно ввести 1 или 2.")

    second = random.randint(1, 100)
    print()
    print(f"Второе число: {BOLD}{second}{RESET}")

    if choice == "1":
        win = second > first
    else:
        win = second < first

    if win:
        print(GREEN + "Ты выиграл!" + RESET)
    else:
        print(RED + "Ты проиграл." + RESET)

    return win


def main() -> None:
    clear_screen()
    print_header(balance=250)
    print("Тебе показывается первое число,")
    print("ты выбираешь, будет ли следующее число больше или меньше.")
    print("Если угадал то побеждаешь, иначе — проигрываешь.")
    print()

    balance = 250

    while True:
        clear_screen()
        print_header(balance)

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

        clear_screen()
        print_header(balance, bet)
        win = play_round()

        if win:
            balance += bet
        else:
            balance -= bet

        print()
        print(DIM + "-" * 36 + RESET)
        print(f"Баланс после раунда: {BOLD}{balance}{RESET}")

        if balance <= 0:
            print(RED + "У тебя закончились деньги. Игра окончена." + RESET)
            break

        print()
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

