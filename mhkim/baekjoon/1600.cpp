/**
 * @file 1600.cpp
 * @brief 말이 되고픈 원숭이
 * @author Sam Kim (samkim2626@gmail.com)
 * 
 * BFS
 * DFS로 풀면 최소한의 동작을 구할 수 없음
 * DP로도 풀 수 있을 것 같다는 생각? -> 시작점에서 도착점이 왼쪽위에서 오른쪽아래로 정해져있기 때문에?
 * 
 * 말의 움직임 k번만. 어떻게 k번을 움직이는게 좋을까?
 * 1. 처음 풀이에는 먼저 말처럼 움직이는 것 진행 -> 이 경우 말로 이동하여 도착할 수 있는 경우 안됨
 * 2. 그러면 매 스텝에서 말의 움직임의 횟수를 고려하는 경로를 설정해보자 -> visited에 (말 이동한 횟수) 차원 추가
 * 
 * 추가) x, y - w, h 그래프 입력받을 때 주의할 것
 */
#include <iostream>
#include <tuple>
#include <queue>

using namespace std;

int k, w, h;
int g[200][200];
bool visited[200][200][31];
pair<int, int> horse[8] = {{1, -2}, {2, -1}, {2, 1}, {1, 2}, {-1, 2}, {-2, 1}, {-2, -1}, {-1, -2}};
pair<int, int> monkey[4] = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};

int bfs(int startX, int startY)
{
    int step = 0;
    int nHorse = 0; // 말처럼 이동한 횟수
    queue<tuple<int, int, int, int>> q;
    q.push(make_tuple(startX, startY, step, nHorse));
    visited[startX][startY][nHorse] = true;

    while (!q.empty())
    {
        tuple<int, int, int, int> t = q.front();
        int x = get<0>(t);
        int y = get<1>(t);
        step = get<2>(t);
        nHorse = get<3>(t);
        q.pop();

        if (x == w - 1 && y == h - 1)
        {
            return step;
        }

        int newX, newY;
        // 말처럼 이동
        if (nHorse < k)
        {
            for (int i = 0; i < 8; i++)
            {
                newX = x + horse[i].first;
                newY = y + horse[i].second;
                if (!visited[newX][newY][nHorse + 1] && newX >= 0 && newX < w && newY >= 0 && newY < h && g[newX][newY] != 1)
                {
                    visited[newX][newY][nHorse + 1] = true;
                    q.push(make_tuple(newX, newY, step + 1, nHorse + 1));
                }
            }
        }

        // 원숭이 이동
        for (int i = 0; i < 4; i++)
        {
            newX = x + monkey[i].first;
            newY = y + monkey[i].second;
            if (!visited[newX][newY][nHorse] && newX >= 0 && newX < w && newY >= 0 && newY < h && g[newX][newY] != 1)
            {
                visited[newX][newY][nHorse] = true;
                q.push(make_tuple(newX, newY, step + 1, nHorse));
            }
        }
    }

    return -1;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> k >> w >> h;
    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < w; j++)
        {
            cin >> g[j][i];
        }
    }

    cout << bfs(0, 0) << '\n';

    return 0;
}