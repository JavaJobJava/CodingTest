/**
 * @file 14938.cpp
 * @brief 서강그라운드
 * @author Sam Kim (samkim2626@gmail.com)
 */
#include <iostream>

using namespace std;

#define INF 1e9

int n, m, r;
int t[101];
int g[101][101];

void floydWarshall()
{
    for (int k = 1; k <= n; k++)
    {
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
            }
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    // input
    cin >> n >> m >> r;
    for (int i = 1; i <= n; i++)
    {
        cin >> t[i];
    }
    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = 0; j < n; j++)
    //     {
    //         if (i != j)
    //         {
    //             g[i][j] = INF;
    //         }
    //     }
    // }
    fill(g[0], g[0] + 10000, INF);

    for (int i = 1; i <= n; i++)
    {
        g[i][i] = 0;
    }

    for (int i = 0; i < r; i++)
    {
        int a, b, l;
        cin >> a >> b >> l;
        g[a][b] = l;
        g[b][a] = l;
    }

    floydWarshall();

    // output
    // 각 시작점으로부터 수색범위 내 아이템 합들을 비교
    int ans = 0;
    for (int i = 1; i <= n; i++) // 시작점
    {
        int sum = 0;
        for (int j = 1; j <= n; j++) // 끝점
        {
            if (g[i][j] <= m)
            {
                sum += t[j];
            }
        }

        ans = max(ans, sum);
    }

    cout << ans << '\n';

    return 0;
}