#TIP: use random.randint to get a random word from the list
import random


def read_file(file_name):
    """
    TODO: Step 1 - open file and read lines as words
    """
    words_file = open(file_name, 'r')
    list = words_file.readlines()
    return list


def select_random_word(words):
    """
    TODO: Step 2 - select random word from list of file
    """
    random_word = random.randint(0,len(words)-1)
    words = words[random_word]
    random_char = random.randint(0,len(words[0])-1)
    print('Guess the word: ' + words[:random_char] + '_' + words[random_char + 1:])
    return words



def get_user_input():
    """
    TODO: Step 3 - get user input for answer
    """
    answer = input('Guess the missing letter: ')
    return answer


def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')

