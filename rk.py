import random

N = 3
M = 3

def rnd_matritsa():
    matritsa = [[0] * M for _ in range(N)]
    
    x = random.randint(0, N - 1)
    y = random.randint(0, M - 1)
    matritsa[x][y] = 2
    
    for i in range(N):
        for j in range(M):
            if matritsa[i][j] == 0:
                matritsa[i][j] = random.randint(0, 1)
    
    return matritsa

matritsa = rnd_matritsa()

for row in matritsa:
    print(row)

def check(matritsa):
    minutes = 0
    while True:
        copy_matritsa = [row[:] for row in matritsa]
        c = False
        for i in range(N):
            for j in range(M):
                if matritsa[i][j] == 2:
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        x, y = i + dx, j + dy
                        if 0 <= x < N and 0 <= y < M:
                            if matritsa[x][y] == 1:
                                copy_matritsa[x][y] = 2
                                c = True
                                print(minutes+1,matritsa)
                                print(minutes+1,copy_matritsa)
        if not c:
            break
        matritsa = copy_matritsa
        minutes += 1
    print("last matritsa:")
    for row in copy_matritsa:
        print(row) 
    for i in range(N):
        for j in range(M):
            if matritsa[i][j] == 1:
                return -1
    return minutes

print("min:", check(matritsa))
