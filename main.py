from random import randint


def start_game():
    code = create_code()
    enter_guess(code)


def enter_guess(code):
    round_counter = 1
    fin = False
    while not fin:
        print("---------------------")
        print("Round " + str(round_counter) + "/8")
        guess = input("Enter Guess:")
        guess_length = len(guess)
        code = code
        if guess_length != 4:
            print("Guess must be 4 digits")
        else:
            round_counter = round_counter + 1
            if calc_hits_blows(guess, code):
                print("You Win!")
                print("Code is: " + code)
                fin = True
            elif round_counter > 8:
                print("You Lose!")
                print("Code is: " + code)
                fin = True


def calc_hits_blows(guess, code):
    hits = 0
    blows = 0
    guess_positions = get_guess_positions(guess)
    code_positions = get_code_positions(code)
    for x in range(len(guess_positions)):
        guess_val = guess_positions[x]
        codes_val = code_positions[x]
        if guess_val == codes_val:
            hits += 1;
        else:
            if guess_val in code and guess_val != guess_positions[x-1] and guess_positions[x-1] != 0:
                blows += 1;
        # elif guess_val != codes_val:
         #   for i in range(len(code_positions)):
          #      if guess_val == code_positions[i] and guess_val in guess_positions:
              #      blows = blows + 1
                #    if check_code(code, guess_val):
                    #    break
    print("Hits: " + str(hits))
    print("Blows: " + str(blows))
    if hits == 4:
        return True
33

def create_code():
    fin = False
    count = 0
    code = "5163"
    # while not fin:
    #     rand_val = str(randint(1, 6))
    #     if not check_code(code, rand_val):
    #         code = code + rand_val
    #         count = count + 1
    #         if count == 4:
    #             fin = True
    return code


def check_code(code, char):
    if char in code:
        return True


def get_guess_positions(guess):
    guess_positions = list(guess)
    return guess_positions


def get_code_positions(code):
    code_positions = list(code)
    return code_positions


start_game()
