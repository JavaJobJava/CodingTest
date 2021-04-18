/**
 * @file 2667.cpp
 * @brief 단지번호붙이기
 * @author Sam Kim (samkim2626@gmail.com)
 * 
 * DFS
 * 음료수 얼려먹기 문제랑 비슷
 * 
 * 백준 테스트 케이스 맞왜틀? -> 입출력 주석제거해서 통과
 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

int n, cnt;
int map[26][26];
bool visited[26][26] = {
    false,
};
vector<int> cnts;
pair<int, int> dir[4] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

void dfs(int x, int y)
{
    cnt++;
    visited[x][y] = true;

    for (int i = 0; i < 4; i++)
    {
        int newX = x + dir[i].first;
        int newY = y + dir[i].second;

        if (newX >= 1 && newX <= n && newY >= 1 && newY <= n)
        {
            if (!visited[newX][newY] && map[newX][newY] == 1)
            {
                dfs(newX, newY);
            }
        }
    }
}

int main()
{
    // ios_base::sync_with_stdio(false);
    // cin.tie(nullptr);

    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            scanf("%1d", &map[i][j]);
        }
    }

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            if (!visited[i][j] && map[i][j] == 1)
            {
                cnt = 0;
                dfs(i, j);
                cnts.push_back(cnt);
            }
        }
    }

    sort(cnts.begin(), cnts.end());

    cout << cnts.size() << '\n';
    for (int i = 0; i < cnts.size(); i++)
    {
        cout << cnts[i] << '\n';
    }

    return 0;
}