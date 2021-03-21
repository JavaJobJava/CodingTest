/**
 * @file 9-2.cpp
 * @brief 미래 도시
 * @author Sam Kim (samkim2626@gmail.com)
 * 
 * 플로이드 워셜
 */
#include <iostream>

using namespace std;

#define INF 1e9

int n, m;
int graph[101][101];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            graph[i][j] = INF;
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i == j)
                graph[i][j] = 0;
        }
    }

    // 두 회사 연결 입력
    for (int i = 0; i < m; i++)
    {
        int a, b;
        cin >> a >> b;
        graph[a][b] = 1;
        graph[b][a] = 1;
    }

    int x, k;
    cin >> x >> k;

    for (int k = 1; k <= n; k++)
    {
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]);
            }
        }
    }

    int time = graph[1][k] + graph[k][x];

    if (time >= INF)
    {
        cout << -1 << '\n';
    }
    else
    {
        cout << time << '\n';
    }

    return 0;
}