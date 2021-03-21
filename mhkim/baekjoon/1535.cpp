/**
 * @file 1535.cpp
 * @brief 안녕
 * @author Sam Kim (samkim2626@gmail.com)
 * 
 * d[i][j] : i명의 사람에게 인사할 때 체력j 내에서 얻을 수 있는 최대 기쁨
 */
#include <iostream>

using namespace std;

int d[21][101];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    int L[21], J[21];
    for (int i = 1; i <= n; i++)
    {
        cin >> L[i];
    }
    for (int i = 1; i <= n; i++)
    {
        cin >> J[i];
    }

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j < 100; j++)
        {
            d[i][j] = d[i - 1][j];
            if (L[i] <= j && d[i][j] < d[i - 1][j - L[i]] + J[i])
            {
                d[i][j] = d[i - 1][j - L[i]] + J[i];
            }
        }
    }

    cout << d[n][99] << '\n';

    return 0;
}