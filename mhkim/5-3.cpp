/**
 * @file 5-3.cpp
 * @brief 음료수 얼려먹기
 * @author Sam Kim (samkim2626@gmail.com)
 * 
 * 1. 왜 DFS로 풀어야겠다고 생각?
 * 2. 
 */
#include <iostream>
#include <vector>

using namespace std;

int n, m;
int graph[1001][1001];

bool dfs(int x, int y)
{
    if (x < 1 || x > n || y < 1 || y > m)
    {
        return false;
    }

    if (graph[x][y] == 0)
    {
        graph[x][y] = 1;
        dfs(x + 1, y);
        dfs(x - 1, y);
        dfs(x, y + 1);
        dfs(x, y - 1);
        return true;
    }
    return false;
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

    int rst = 0;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            if (dfs(i, j))
            {
                rst++;
            }
        }
    }

    cout << rst << '\n';

    return 0;
}