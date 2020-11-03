import random

def run_game():
    code = []
    while len(code) != 4:
        r = random.randint(1,8)
        if r not in code:
            code.append(r)
    print('{}-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.'.format(len(code)))
    
    guesses = 11
    while guesses >= 0:
        try:
            user_guess = input('Input {} digit code: '.format(len(code)))
        
        except EOFError:
            pass
        
        if len(user_guess) != 4 or user_guess.isnumeric() == False:
            print('Please enter exactly {} digits.'.format(len(code)))
            continue
        
        user_code = [int(number) for number in user_guess]
        
        correct = 0
        for x,y in zip(user_code,code):
            if x == y:
                correct += 1

        print('Number of correct digits in correct place:     {}'.format(correct))
        
        not_correct = 0
        for x,y in zip(user_code,code):
            if x in code and x != y:
                not_correct += 1
        print('Number of correct digits not in correct place: {}'.format(not_correct))
        
        if user_code == code or len(user_code) != 4 or user_guess.isnumeric == False:
            pass
        else:
            print('Turns left: {}'.format(guesses))
            
        if user_code == code:
            print('Congratulations! You are a codebreaker!')
            print('The code was:',''.join(map(str,code)))
            break
            
        #print(user_code)
        #print(code)
        
        guesses -= 1
    pass

if __name__ == "__main__":
    run_game()
