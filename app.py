import random

def get_user_choice():
    user_choice = input("Escolha pedra, papel ou tesoura: ")
    return user_choice.lower()

def get_computer_choice():
    choices = ["pedra", "papel", "tesoura"]
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Empate!"
    elif user_choice == "pedra":
        if computer_choice == "tesoura":
            return "Você venceu!"
        else:
            return "Você perdeu!"
    elif user_choice == "papel":
        if computer_choice == "pedra":
            return "Você venceu!"
        else:
            return "Você perdeu!"
    elif user_choice == "tesoura":
        if computer_choice == "papel":
            return "Você venceu!"
        else:
            return "Você perdeu!"
    else:
        return "Escolha inválida!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("Você escolheu:", user_choice)
    print("O computador escolheu:", computer_choice)
    print(determine_winner(user_choice, computer_choice))

play_game()
