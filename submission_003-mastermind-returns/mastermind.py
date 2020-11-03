import random


def create_code():
    """Function that creates the 4 digit code, using random digits from 1 to 8"""
    code = [0, 0, 0, 0]
    for i in range(4):
        value = random.randint(1, 8)
        while value in code:
            value = random.randint(1, 8)
        code[i] = value
    return code

def show_instructions():
    """Shows instructions to the user"""
    
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')

def get_user_code():
    answer = input("Input 4 digit code: ")
    while len(answer) < 4 or len(answer) > 4:
        print("Please enter exactly 4 digits.")
        answer = input("Input 4 digit code: ")
    return answer

def show_results(correct_digits_and_position,correct_digits_only):
    """Show the results from one turn"""
    
    print('Number of correct digits in correct place:     ' + str(correct_digits_and_position))
    print('Number of correct digits not in correct place: ' + str(correct_digits_only))

def take_turn(game_code):

    """Handle the logic of taking a turn, which includes:
        * get answer from user
        * check if answer is valid
        * check correctness of answer
    """
    
    
    answer = get_user_code()
    correct_digits_and_position = 0
    correct_digits_only = 0
    for i in range(len(answer)):
        if game_code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in game_code:
            correct_digits_only += 1

    show_results(correct_digits_and_position,correct_digits_only)
    return(correct_digits_and_position)

def show_code(game_code):

    """Show Code that was created to user"""

    print('The code was: '+str(game_code))


def check_correctness(correct_digits_and_position,turns):

    """Checks correctness of answer and show output to user"""

    if correct_digits_and_position == 4:
        print('Congratulations! You are a codebreaker!')
        return True
    else:
        print('Turns left: ' + str(12 - turns))
        return False

def run_game():

    """Main function for running the game"""
    
    correct = False
    show_instructions()
    game_code = create_code()
    turns = 0
    correct_digits_and_position = 0

    while not correct and turns < 12:
        correct_digits_and_position = take_turn(game_code)
        turns += 1
        correct = check_correctness(correct_digits_and_position,turns)
    show_code(game_code)


if __name__ == "__main__":

    run_game()

