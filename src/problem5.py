n = int(input())
grid = [input() for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]

for j in range(3):
    if grid[-1][j] == "C":
        dp[-1][j] = 1
    
for i in range(n - 2, -1, -1):
    for j in range(3):
        if grid[i][j] == "W":
            continue
        
        for k in range(j - 1, j + 2):
            if 0 <= k < 3 and grid[i + 1][k] != 'W':
                has_mushroom = 0
                if grid[i][j] == "C":
                    has_mushroom = 1
                
                dp[i][j] = max(dp[i][j], dp[i + 1][k] + has_mushroom)

print(max(dp[0]))