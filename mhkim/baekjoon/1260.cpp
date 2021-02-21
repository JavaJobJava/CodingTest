/**
 * @file 1260.cpp
 * @brief DFS와 BFS
 * @author Sam Kim (samkim2626@gmail.com)
 */
#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

int num = 1001;
vector<int> g[1001];
bool visited[1001];

void dfs(int start)
{
    if (visited[start] == true)
    {
        return;
    }

    visited[start] = true;
    cout << start << ' ';

    for (int i = 0; i < g[start].size(); i++)
    {
        dfs(g[start][i]);
    }
}

void bfs(int start)
{
    deque<int> dq;
    dq.push_back(start);
    visited[start] = true;

    while (!dq.empty())
    {
        int x = dq.front();
        cout << x << ' ';
        dq.pop_front();

        for (int i = 0; i < g[x].size(); i++)
        {
            int y = g[x][i];
            if (!visited[y])
            {
                dq.push_back(y);
                visited[y] = true;
            }
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, v;
    cin >> n >> m >> v;

    for (int i = 0; i < m; i++)
    {
        int a, b;
        cin >> a >> b;
        g[a].push_back(b);
        g[b].push_back(a);
    }

    // 오름차순
    for (int i = 0; i < num; i++)
    {
        sort(g[i].begin(), g[i].end());
    }

    dfs(v);
    cout << '\n';

    for (int i = 0; i < num; i++)
    {
        visited[i] = false;
    }

    bfs(v);

    return 0;
}