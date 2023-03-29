from error_handling import exception_handler
from random import randint


@exception_handler
def guess_number():
    """Gues the number The GAME

    :return:
    """
    computer_number = randint(1, 100)
    # print(f"Wylosowana liczba: {computer_number}")

    while True:
        player_number = int(input("Guess the number: "))

        if computer_number is player_number:
            print("You win!")
            break
        elif computer_number < player_number:
            print("Too big!")
        elif computer_number > player_number:
            print("Too small!")


guess_number()
