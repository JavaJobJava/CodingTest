/**
 * @file 9-3.cpp
 * @brief 전보
 * @author Sam Kim (samkim2626@gmail.com)
 * 
 * 다익스트라 알고리즘
 */
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

#define INF 1e9

int n, m, c;
vector<pair<int, int>> graph[30001];
int d[30001];

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

    cin >> n >> m >> c;

    for (int i = 0; i < m; i++)
    {
        int x, y, z;
        cin >> x >> y >> z;
        graph[x].push_back({y, z});
    }

    fill(d, d + 30001, INF);

    dijkstra(c);

    int cnt = 0;   // 도시 수
    int total = 0; // 총 걸리는 시간
    for (int i = 1; i <= n; i++)
    {
        if (d[i] != INF) // 도달할 수 있는 도시면
        {
            cnt++;
            total = max(total, d[i]);
        }
    }

    cout << cnt - 1 << ' ' << total << '\n';

    return 0;
}