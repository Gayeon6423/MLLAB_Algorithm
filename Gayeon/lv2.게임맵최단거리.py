from collections import deque
def bfs(row,col,len_row,len_col,maps,visit):
    drow = (1,0,-1,0) # 상하 변화
    dcol = (0,1,0,-1) # 좌우 변화
    queue = deque()
    queue.append((row,col))
    while queue :
        row,col = queue.popleft()
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]

            if nrow < 0 or ncol < 0 or nrow > len_row-1 or ncol > len_col-1:
                continue

            if maps[nrow][ncol] and not visit[nrow][ncol]:
                visit[nrow][ncol] = 1
                maps[nrow][ncol] = maps[row][col]+1
                queue.append((nrow,ncol))

    if maps[len_row-1][len_col-1] == 1:
        return -1

    return maps[len_row-1][len_col-1]

def solution(maps):
    len_row = len(maps)
    len_col = len(maps[0])
    visited = [[0]*len_col for i in range(len_row)]
    visited[0][0]=1
    return bfs(0,0,len_row,len_col,maps,visited)