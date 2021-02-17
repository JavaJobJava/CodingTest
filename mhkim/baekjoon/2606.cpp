/**
 * @file 2606.cpp
 * @brief 바이러스
 * @author Sam Kim (samkim2626@gmail.com)
 */
#include <iostream>
#include <deque>

using namespace std;

int n, m;
int comp[101][101] = {0};
bool visited[101];
int cnt = 0;

void bfs(int start)
{
    deque<int> dq;
    dq.push_back(start);
    visited[start] = true;

    while (!dq.empty())
    {
        int v = dq.front();
        dq.pop_front();
        cnt++;

        for (int i = 1; i <= n; i++)
        {
            if (comp[v][i] == 1 && visited[i] != true)
            {
                dq.push_back(i);
                visited[i] = true;
            }
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;

    for (int i = 0; i < m; i++)
    {
        int a, b;
        cin >> a >> b;
        comp[a][b] = comp[b][a] = 1;
    }

    bfs(1);

    cout << cnt - 1 << '\n';

    return 0;
}