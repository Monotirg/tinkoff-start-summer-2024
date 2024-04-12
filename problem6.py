def bfs():
    queue = [(start, "K")]
    dist = 0
    while queue:
        dist += 1
        for _ in range(len(queue)):
            pos, state = queue.pop(0)
            cur_i, cur_j = pos
            for di, dj in direction[state]:
                i, j  = cur_i + di, cur_j + dj
                if i < 0 or i >= n or j < 0 or j >= n or (i, j) in visited[state]:
                    continue
                if (i, j) == end:
                    return dist
                elif board[i][j] not in (".", "S"):
                    queue.append(((i, j), board[i][j]))
                    visited[board[i][j]].add((i, j))
                else:
                    queue.append(((i, j), state)) 
                    visited[state].add((i, j))
    
    return -1

n = int(input())
board = []
start = (-1, -1)
end = (-1, -1)

for i in range(n):
    row = input()
    if "S" in row:
        start = (i, row.index("S"))
    elif "F" in row:
        end = (i, row.index("F"))
    board.append(row)


queue = [(start, "K")]
direction = {
    "K":{
        (-2, -1), (-1, -2), (1, -2), (2, -1),
        (2, 1), (1, 2), (-1, 2), (-2, 1)
    },
    "G": {
        (-1, -1), (0, -1), (1, -1), (1, 0),
        (1, 1), (0, 1), (-1, 1), (-1, 0)
    }

}
visited = {
    "K": set([start]),
    "G": set()
}

result = bfs()
print(result)
