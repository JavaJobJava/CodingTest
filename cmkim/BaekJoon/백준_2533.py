import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())
tree = [[] for _ in range(n+1)]
dp = [[0, 0] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for i in range(n-1):
    a, b = map(int, input().split())

    tree[a].append(b)
    tree[b].append(a)

#print(tree)

def bfs(root):
  visited[root] = True
  dp[root][0] = 0
  dp[root][1] = 1

  for i in tree[root]:
    if not visited[i]:
      bfs(i)
      dp[root][0] += dp[i][1]
      dp[root][1] += min(dp[i][0], dp[i][1])

bfs(1)

print(min(dp[1][0], dp[1][1]))