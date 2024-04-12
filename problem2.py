n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

mat = [[mat[j][i] for j in range(n)] for i in range(m)]
for i in range(m):
    for j in range(n // 2):
        mat[i][j], mat[i][n - j - 1] = mat[i][n - j - 1], mat[i][j]

for row in mat:
    print(*row)
