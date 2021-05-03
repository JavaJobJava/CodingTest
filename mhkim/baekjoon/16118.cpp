/**
 * @file 16118.cpp
 * @brief 달빛 여우
 * @author Sam Kim (samkim2626@gmail.com)
 * 
 * 여우는 그대로, 늑대는 2배 빠르게/2배 느리게(퐁당퐁당) 이동
 * -> 늑대의 최단경로 로직을 어떻게 짜느냐가 문제
 * 
 * 오솔길 길이 * 간선 수의 최대값이 1e9 -> INF 1e9+1
 * 오솔길 길이/2 할 경우 소수점 -> float 하게 되면 코드의 복잡도 증가, 정확도에 의심 -> 어차피 비교니까 길이*2
 * 
 * 1. 일반적인 다잌스트라에서 늑대 경로를 /2, *2 로만 변경
 * -> 다른 최단 경로(다른 경우의 수)로 갈 수 있음에도 업데이트 안됨
 * 2. 추가로 늑대 최단경로 테이블을 두 개(빠르게, 느리게)로 나눠서 각각 업데이트
 * - 지점까지 느리게 온 경우/빠르게 온 경우
 * 
 * !시작에서 빠르게 출발
 */
#include <iostream>
#include <vector>
#include <queue>

#define INF 1e9 + 1

using namespace std;

int n, m, start = 1;
vector<pair<int, int>> graph[4001];
int dFox[4001];
int dWolf[4001][2]; // 0:빠르게, 1:느리게

void dijkstra4Fox(int start)
{
    priority_queue<pair<int, int>> pq;
    pq.push({0, start});
    dFox[start] = 0;
    while (!pq.empty())
    {
        int dist = -pq.top().first;
        int now = pq.top().second;
        pq.pop();

        if (dFox[now] < dist)
        {
            continue;
        }

        for (int i = 0; i < graph[now].size(); i++)
        {
            int cost = dist + graph[now][i].second;
            if (cost < dFox[graph[now][i].first])
            {
                dFox[graph[now][i].first] = cost;
                pq.push(make_pair(-cost, graph[now][i].first));
            }
        }
    }
}

void dijkstra4Wolf(int start)
{
    // {노드까지의 거리, {노드, 속도}}
    priority_queue<pair<int, pair<int, int>>> pq;
    pq.push({0, {start, 0}}); // 다음 속도0 2배빠르게, 속도1 2배느리게
    dWolf[start][1] = 0;      // 시작에서는 빠르게만 출발(느리게 도착했다고 가정)

    while (!pq.empty())
    {
        int dist = -pq.top().first;
        int now = pq.top().second.first;
        int speed = pq.top().second.second;
        pq.pop();

        if (dWolf[now][1 - speed] < dist)
        {
            continue;
        }

        for (int i = 0; i < graph[now].size(); i++)
        {
            int cost;
            if (speed == 0)
            {
                cost = dist + graph[now][i].second / 2;
            }
            else
            {
                cost = dist + graph[now][i].second * 2;
            }

            if (cost < dWolf[graph[now][i].first][speed])
            {
                dWolf[graph[now][i].first][speed] = cost;
                pq.push(make_pair(-cost, make_pair(graph[now][i].first, 1 - speed)));
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
        int a, b, c;
        cin >> a >> b >> c;
        graph[a].push_back({b, c * 2});
        graph[b].push_back({a, c * 2});
    }

    fill(dFox, dFox + 4001, INF);
    fill(&dWolf[0][0], &dWolf[4001][2], INF);

    dijkstra4Fox(start);
    dijkstra4Wolf(start);

    int ans = 0;
    for (int i = 1; i <= n; i++)
    {
        if (dFox[i] < min(dWolf[i][0], dWolf[i][1]))
        {
            ans++;
        }
    }
    cout << ans << '\n';

    return 0;
}