/**
 * @file 5-4.cpp
 * @brief 미로 탈출
 * @author Sam Kim (samkim2626@gmail.com)
 */
#include <iostream>
#include <queue>
#include <utility>

using namespace std;

int n, m;
int graph[201][201];
pair<int, int> d[4] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

int bfs(int x, int y)
{
    pair<int, int> xy = {x, y};
    queue<pair<int, int>> q;
    q.push(xy);

    while (!q.empty())
    {
        x = q.front().first;
        y = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++)
        {
            int nx = x + d[i].first;
            int ny = y + d[i].second;

            if (nx < 1 || nx > n || ny < 1 || ny > m)
            {
                continue;
            }

            if (graph[nx][ny] == 0)
            {
                continue;
            }

            if (graph[nx][ny] == 1)
            {
                graph[nx][ny] = graph[x][y] + 1;
                q.push(make_pair(nx, ny));
            }
        }
    }

    return graph[n][m];
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            scanf("%1d", &graph[i][j]);
        }
    }

    cout << bfs(1, 1) << ' ';

    return 0;
}