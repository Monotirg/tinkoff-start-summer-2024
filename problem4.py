n, rotate = input().split()
n = int(n)
mat = [list(map(int, input().split())) for _ in range(n)]

result = []

if rotate == "L":
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            result.extend([
                [[i, j], [j, n - i - 1]],
                [(j, n - i - 1), (n - i - 1, n - j - 1)],
                [(n - i - 1, n - j - 1), (n - j - 1, i)]
            ])
else:
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            result.extend([
                [[i, j], [n - j - 1, i]],
                [(j, n - i - 1), (n - i - 1, n - j - 1)],
                [(n - i - 1, n - j - 1), (n - j - 1, i)]
            ])

print(len(result))
for item in result:
    ind1, ind2 = item
    print(*ind1, *ind2)
