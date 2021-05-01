/**
 * @file 11724.cpp
 * @brief 연결 요소의 개수
 * @author Sam Kim (samkim2626@gmail.com)
 * 
 * BFS, 인접리스트
 * DFS로 풀 수 있지 않을까?
 */
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

#define N 1001

vector<int> g[N];
bool visited[N];

void bfs(int start)
{
    visited[start] = true;
    queue<int> q;
    q.push(start);

    while (!q.empty())
    {
        int p = q.front();
        q.pop();

        for (int i = 0; i < g[p].size(); i++)
        {
            if (!visited[g[p][i]])
            {
                visited[g[p][i]] = true;
                q.push(g[p][i]);
            }
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    for (int i = 1; i <= m; i++)
    {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    int ans = 0;
    for (int i = 1; i <= n; i++)
    {
        if (!visited[i])
        {
            bfs(i);
            ans++;
        }
    }

    cout << ans << '\n';

    return 0;
}