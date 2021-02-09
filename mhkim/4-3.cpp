/**
 * @file 4-3.cpp
 * @brief 왕실의 나이트
 * @author Sam Kim (samkim2626@gmail.com)
 */
#include <iostream>
#include <utility>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    getline(cin, s);
    int row = s[1] - '0';
    int column = s[0] - 'a' + 1;

    pair<int, int> moves[8] = {{1, -2},
                               {-1, -2},
                               {-2, -1},
                               {-2, 1},
                               {1, 2},
                               {-1, 2},
                               {2, 1},
                               {2, -1}};

    int cnt = 0;
    for (int i = 0; i < 8; i++)
    {
        int nextR = row + moves[i].first;
        int nextC = column + moves[i].second;
        if (nextR >= 1 && nextR <= 8 && nextC >= 1 && nextC <= 8)
        {
            cnt++;
        }
    }

    cout << cnt << '\n';

    return 0;
}