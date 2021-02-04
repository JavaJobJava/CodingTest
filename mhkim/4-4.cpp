/**
 * @file 4-4.cpp
 * @brief 게임 개발
 * @author Sam Kim (samkim2626@gmail.com)
 */
#include <iostream>

using namespace std;

int map[50][50];
int gone[50][50] = {0}; // 맵에서 간 곳 플래그
pair<int, int> moves[4] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}}; // 북, 동, 남, 서 순
int a, b, d;

// 캐릭터 왼쪽으로 회전
void turn()
{
    d--;
    if (d < 0)
    {
        d = 3;
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    cin >> a >> b >> d;
    gone[a][b] = 1; // 처음 위치 간 곳 처리

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> map[i][j];
        }
    }

    int cnt = 1;
    int nTurn = 0;
    while (1)
    {
        turn();
        int nextA = a + moves[d].first;
        int nextB = b + moves[d].second;

        if (gone[nextA][nextB] == 0 && map[nextA][nextB] == 0)
        {
            a = nextA;
            b = nextB;
            gone[a][b] = 1;
            cnt++;
            nTurn = 0;
        }
        else
        {
            nTurn++;
        }

        if (nTurn == 4)
        {
            nextA = a - moves[d].first;
            nextB = b - moves[d].second;
            if (map[nextA][nextB] == 0)
            {
                a = nextA;
                b = nextB;
            }
            else
            {
                break;
            }
            nTurn = 0;
        }
    }

    cout << cnt << '\n';

    return 0;
}