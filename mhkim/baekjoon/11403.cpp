/**
 * @file 11403.cpp
 * @brief 경로 찾기
 * @author Sam Kim (samkim2626@gmail.com)
 */
#include <iostream>

using namespace std;

int graph[101][101];
int path[101][101];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            cin >> graph[i][j];
        }
    }

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            for (int k = 1; k <= n; k++)
            {
                if (graph[j][k] == 1 || graph[j][i] + graph[i][k] == 2)
                {
                    path[j][k] = 1;
                }

                if (path[j][k] == 1 || path[j][i] + path[i][k] == 2)
                {
                    graph[j][k] = 1;
                }
            }
        }
    }

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            cout << path[i][j] << ' ';
        }
        cout << '\n';
    }

    return 0;
}