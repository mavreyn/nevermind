'''
Trying to make a mastermind game last as long as possible
Dynamically changes the codemaker's code
Selects bin that minimally reduces possibility space

Maverick Reynolds
Start   07-31-2022
v1      08-04-2022
v1.1    08-08-2022

'''

COLOR_BIN = 'oygpfw'

# Gets pins that correspond with two codes
# Reds listed first then whites
def get_pins(code1: list, code2: list):
    # Make duplicate unaliased lists
    a = code1.copy()
    b = code2.copy()
    pinresult = []

    # Get the reds
    for i in range(4):
        if a[i] == b[i]:
            a[i] = None
            b[i] = None
            pinresult.append('r')

    # Get the whites
    for i in range(4):
        if a[i] is not None and a[i] in b:
            b[b.index(a[i])] = None
            a[i] = None
            pinresult.append('w')

    return pinresult

# Multiple list comprehension
def gen_all_codes():
    return [[i, j, k, l] for i in COLOR_BIN
                         for j in COLOR_BIN
                         for k in COLOR_BIN
                         for l in COLOR_BIN]

# Start with r then w
def gen_all_pin_combos():
    return [['r']*i + ['w']*j for i in range(5) for j in range(5-i)]

# Gets codes that match with a pin combination
def get_matching_codes(code, pins, pos_space):
    return [cd for cd in pos_space if get_pins(cd, code) == pins]

ALL_CODES = gen_all_codes()
ALL_PIN_COMBOS = gen_all_pin_combos()

def main():
    # Lets play the game!
    print('Welcome to Nevermind')
    curr_poss_space = ALL_CODES
    code_match = False

    # Reduce possibility space until only one solution is available
    while not code_match:
        # Prompt and check guess
        guess = list(input('\nEnter player guess: '))
        code_match = [guess] == curr_poss_space

        # Get amount of codes that match with each pin combo
        code_amnts = [len(get_matching_codes(guess, pc, curr_poss_space)) for pc in ALL_PIN_COMBOS]

        # Reduce possibility space by the least amount
        idx_max = code_amnts.index(max(code_amnts))
        curr_poss_space = get_matching_codes(guess, ALL_PIN_COMBOS[idx_max], curr_poss_space)
        
        # Print computer information
        print(curr_poss_space)
        print(len(curr_poss_space))
        print(code_amnts)
        print(ALL_PIN_COMBOS[idx_max])

    input("\nMost impressive!")


if __name__ == '__main__':
    main()