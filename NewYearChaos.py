""" https://www.hackerrank.com/challenges/new-year-chaos/problem """
def minimumBribes(Q):
    moves = 0
    q = [P-1 for P in Q]
    for index, person in enumerate(q):
        if person - index > 2:
            print("Too chaotic")
            return
        for j in range(max(person-1,0),index):
            if q[j] > person:
                moves += 1
    print(moves)
