# 백준 1260 DFS와 BFS 실버2

import sys
from collections import deque

def dfs(start):

    visited1[start] = 1
    print(start, end=' ')


    for i in arr[start]:
        if visited1[i] == 0:
            dfs(i)


def bfs(graph,start,visited):
    queue = deque([start])

    visited[start] = 1
    while queue:
        end = queue.popleft()
        print(end, end=' ')
        for i in graph[end]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1


N,M,V = map(int,sys.stdin.readline().split())
visited1 = [0] * (N+1)
visited = [0] * (N+1)
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)
for i in range(len(arr)):
    arr[i].sort()
dfs(V)
print()
bfs(arr,V,visited)








