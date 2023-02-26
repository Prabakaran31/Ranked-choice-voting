# This program finds the winner of ranked choice voting / preferential voting


ballot = [[5, 4, 2, 1, 3], [5, 2, 1, 3, 4], [4, 2, 3, 5, 1], [1, 2, 4, 5, 3], [5, 3, 1, 4, 2], [2, 4, 5, 1, 3], [1, 2, 4, 5, 3], [1, 4, 2, 3, 5], [2, 4, 5, 3, 1], [1, 2, 4, 3, 5], [1, 4, 2, 3, 5], [1, 4, 2, 3, 5], [1, 2, 4, 3, 5], [5, 4, 3, 1, 2], [1, 2, 3, 4, 5], [3, 4, 2, 1, 5], [1, 5, 4, 3, 2], [5, 3, 4, 2, 1], [5, 3, 4, 2, 1], [4, 3, 2, 5, 1], [3, 5, 2, 1, 4], [2, 4, 3, 1, 5], [4, 5, 1, 3, 2], [2, 1, 5, 3, 4], [1, 4, 2, 3, 5], [3, 4, 1, 2, 5], [5, 3, 2, 1, 4], [3, 4, 2, 1, 5], [5, 4, 1, 2, 3], [3, 2, 1, 5, 4], [5, 1, 2, 3, 4], [5, 4, 3, 1, 2], [5, 4, 3, 1, 2], [4, 3, 5, 1, 2], [2, 1, 5, 3, 4], [3, 1, 4, 5, 2], [1, 5, 2, 3, 4], [3, 5, 4, 2, 1], [1, 3, 4, 5, 2], [2, 3, 4, 5, 1], [3, 5, 2, 1, 4], [1, 5, 3, 4, 2], [1, 2, 3, 4, 5], [5, 1, 2, 3, 4], [1, 3, 4, 2, 5], [2, 1, 5, 3, 4], [4, 3, 2, 5, 1], [5, 3, 4, 1, 2], [5, 2, 1, 4, 3], [5, 3, 4, 2, 1], [1, 4, 3, 2, 5], [3, 2, 4, 5, 1], [1, 3, 4, 5, 2], [2, 5, 4, 1, 3], [2, 3, 5, 4, 1], [3, 4, 1, 2, 5], [3, 2, 1, 5, 4], [5, 1, 4, 2, 3], [1, 3, 2, 5, 4], [1, 3, 2, 5, 4], [5, 1, 2, 3, 4], [4, 5, 2, 3, 1], [4, 3, 1, 5, 2], [5, 3, 1, 4, 2], [1, 5, 2, 4, 3], [2, 3, 1, 5, 4], [1, 4, 3, 5, 2], [1, 5, 4, 3, 2], [2, 5, 4, 3, 1], [5, 1, 3, 4, 2], [4, 2, 5, 1, 3], [5, 2, 3, 1, 4], [2, 3, 5, 1, 4], [5, 3, 2, 1, 4], [2, 4, 1, 5, 3], [2, 3, 4, 1, 5], [4, 5, 3, 1, 2], [1, 4, 5, 2, 3], [1, 5, 2, 4, 3], [5, 2, 3, 4, 1], [2, 3, 4, 1, 5], [4, 2, 5, 1, 3], [3, 5, 1, 2, 4], [4, 2, 5, 3, 1], [3, 2, 5, 1, 4], [2, 1, 4, 5, 3], [5, 1, 3, 4, 2], [1, 5, 3, 2, 4], [5, 1, 3, 2, 4], [4, 2, 5, 3, 1], [1, 5, 3, 4, 2], [2, 1, 3, 5, 4], [5, 3, 1, 4, 2], [2, 3, 4, 5, 1], [2, 5, 1, 3, 4], [3, 4, 2, 5, 1], [2, 1, 5, 3, 4], [2, 5, 1, 4, 3], [1, 2, 5, 3, 4], [4, 1, 5, 2, 3], [4, 2, 5, 3, 1], [2, 1, 3, 5, 4], [2, 4, 3, 1, 5], [3, 1, 5, 2, 4], [1, 2, 4, 5, 3], [5, 3, 2, 1, 4], [2, 4, 5, 3, 1], [1, 3, 5, 4, 2], [3, 4, 2, 5, 1], [2, 3, 5, 4, 1], [2, 1, 5, 3, 4]]
a = ballot
ref = ['A', 'B', 'C', 'D', 'E']

def counter(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    d = [0 for x in range(columns)]
    print(rows, columns)
    for i in range(0, columns):
        sum = 0
        for j in range(0, rows):
            if matrix[j][i] == 1:
                sum = sum + 1
        d[i] = sum
        print(sum)
    return d


def kicker(mat, w):

    length = len(mat)
    col = len(mat[0])
    for i in range(0, length):

        u = mat[i][w]
       
    
        for j in range(0,col):
            if mat[i][j] > u:
                mat[i][j] = mat[i][j] - 1
            else:
                pass

    length = len(mat)
    # print(len(mat))
    for i in range(0, length):
        del mat[i][w]
    del ref[w]
    return mat


def winner():
    winne = g.index(max(g))
    print(f'The winner is {ref[winne]}')


# change the range(0, 3) and threshold(55) based on the number of voter choices and candidates
for i in range(0,3):

    g = counter(a)
    if max(g) < 55:
        # print(g.index(min(g)))
        clip = g.index(min(g))
        print(f'{ref[clip]} is out of the race')
        a = kicker(a, clip)
        print(ref)
        print(a)

g = counter(a)
if max(g) > 55:
    winner()
else:
    print("It's time for re-election!")
