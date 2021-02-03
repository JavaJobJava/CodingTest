/**
 * @file 3-3.cpp
 * @brief 숫자 카드 게임
 * @author Sam Kim (samkim2626@gmail.com)
 */
#include <iostream>

using namespace std;

int nm[100][100] = {};

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> nm[i][j];
        }
    }

    int res;
    for (int i = 0; i < n; i++)
    {
        int num = 101;
        for (int j = 0; j < m; j++)
        {
            num = min(num, nm[i][j]);
        }
        res = max(res, num);
    }
    cout << res << '\n';

    return 0;
}