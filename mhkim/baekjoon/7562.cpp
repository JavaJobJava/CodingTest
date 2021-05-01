/**
 * @file 7562.cpp
 * @brief 나이트의 이동
 * @author Sam Kim (samkim2626@gmail.com)
 * 
 * bfs
 * 
 * !! memset - #include <cstring>
 */
#include <iostream>
#include <deque>
#include <utility>
#include <cstring>

using namespace std;

bool chess[300][300];
int l;
pair<int, int> moves[8] = {{-2, -1}, {-1, -2}, {1, -2}, {2, -1}, {-2, 1}, {-1, 2}, {1, 2}, {2, 1}};

int bfs(pair<int, int> &start, pair<int, int> &end)
{
    deque<pair<pair<int, int>, int>> q;
    int step = 0;
    q.push_back(make_pair(start, step));
    chess[start.first][start.second] = true;

    int count = 0;
    while (!q.empty())
    {
        pair<pair<int, int>, int> qNow = q.front();
        pair<int, int> now = qNow.first;
        count = qNow.second;
        q.pop_front();

        if (now.first == end.first && now.second == end.second)
        {
            break;
        }

        count += 1;
        for (int i = 0; i < 8; i++)
        {
            if (chess[now.first + moves[i].first][now.second + moves[i].second] != true)
            {
                if (now.first + moves[i].first > l - 1 || now.first + moves[i].first < 0 || now.second + moves[i].second > l - 1 || now.second + moves[i].second < 0)
                {
                    continue;
                }
                q.push_back(make_pair(make_pair(now.first + moves[i].first, now.second + moves[i].second), count));
                chess[now.first + moves[i].first][now.second + moves[i].second] = true;
            }
        }
    }

    return count;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--)
    {
        cin >> l;
        int fromX, fromY;
        cin >> fromX >> fromY;
        pair<int, int> from = {fromX, fromY};
        int toX, toY;
        cin >> toX >> toY;
        pair<int, int> to = {toX, toY};

        cout << bfs(from, to) << '\n';
        memset(chess, false, sizeof(chess));
    }

    return 0;
}