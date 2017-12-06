def solution(): return True

n = 0
mx = 1
visited = [[0]*10 for i in range(10)]
x_dir = [-1, 1, 0, 0]
y_dir = [0, 0, -1, 1]


def dfs(x, y, cnt, v):
    global mx
    for i in range(0, 4):
        x_next = x + x_dir[i]
        y_next = y + y_dir[i]
        if x_next < 0 or x_next >= n or y_next < 0 or y_next >= n or visited[x_next][y_next] or v[x_next][y_next] != v[x][y]:
            if mx < cnt:
                mx = cnt
        else:
            visited[x_next][y_next] = 1
            dfs(x_next, y_next, cnt + 1, v)
            visited[x_next][y_next] = 0


def ddd(board):
    global n
    n = len(board)

    for i in range(0, n):
        for j in range(0, n):
            visited[i][j] = 1
            dfs(i, j, 1, board)
            visited[i][j] = 0

    if (mx < 2):
        return -1

    return mx
