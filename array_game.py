def one_move(array):
    q = array.index(max(array))
    return array[:q]

def game_arr(array):
    games_count = 0
    while array:
        array = one_move(array)
        games_count += 1
    if games_count%2==0:
        return "ANDY"
    return "BOB"

if __name__ == '__main__':
    array = [1, 2,3,4,5,6,127,8,9,0,1,24,5,7,3,2,5,6,7]
    print(game_arr(array))
