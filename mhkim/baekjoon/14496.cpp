/**
 * @file 14496.cpp
 * @brief 그대, 그머가 되어
 * @author Sam Kim (samkim2626@gmail.com)
 */
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

#define INF 1e9

vector<pair<int, int>> graph[1001];
int d[1001];

void dijkstra(int start)
{
    priority_queue<pair<int, int>> pq;

    pq.push({0, start});
    d[start] = 0;
    while (!pq.empty())
    {
        int dist = -pq.top().first;
        int now = pq.top().second;
        pq.pop();

        if (d[now] < dist)
        {
            continue;
        }
        for (int i = 0; i < graph[now].size(); i++)
        {
            int cost = dist + graph[now][i].second;
            if (cost < d[graph[now][i].first])
            {
                d[graph[now][i].first] = cost;
                pq.push(make_pair(-cost, graph[now][i].first));
            }
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b;
    cin >> a >> b;
    int n, m;
    cin >> n >> m;

    for (int i = 0; i < m; i++)
    {
        int x, y;
        cin >> x >> y;
        graph[x].push_back({y, 1});
        graph[y].push_back({x, 1});
    }

    fill(d, d + 1001, INF);

    dijkstra(a);

    if (d[b] == INF)
    {
        cout << -1 << '\n';
    }
    else
    {
        cout << d[b] << '\n';
    }

    return 0;
}