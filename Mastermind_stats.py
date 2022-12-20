import json

def get_game_lengths():
    lgths = [0]*11
    for game in DATA['games']:
            l = game['completed_in']
            lgths[l] += 1

    return lgths

def print_8_game():
        for game in DATA['games']:
            if game['completed_in'] == 8:
                for move in game['moves']:
                    print(move)

def get_possibility_space_lists():
    pslists = []
    for game in DATA['games']:
        pslist = []
        for move in game['moves']:
            pslist.append(move['possibility'])
        pslists.append(pslist)
    
    return pslists

# Adds corresponding entries of list
def list_add(a, b):
    diff = len(b) - len(a)
    if diff > 0:
        a = a + [0]*diff
    elif diff < 0:
        b = b + [0]*-diff
    
    return [a[i] + b[i] for i in range(len(a))]

def gen_avg_possibilities():
    ps_all = get_possibility_space_lists()
    total = [0]*9
    weights = [0]*8+[1]
    avg_poss = [0]*9
    for l in ps_all:
        total = list_add(total, l)
        weights = list_add(weights, [1.0]*len(l))
    for idx in range(len(total)):
        avg_poss[idx] = total[idx]/weights[idx]

    return avg_poss
        
def main():
    '''
    res = get_game_lengths()
    for i in res:
        print(i)
    '''
    #print(list_add([6, 2, 7, 3], [4, 6, 2]))
    #input(f'1\t2\n3\t4')
    
    '''
    big_list = get_possibility_space_lists()
    for l in big_list:
        for e in l:
            print(e, end=' ')
        print()
    input()
    '''

    for i in gen_avg_possibilities():
        print(i)

if __name__ == '__main__':
    with open('BiglyBrain2.0/send/data10k.json') as f:
        DATA = json.load(f)
    main()