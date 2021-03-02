/**
 * @file 8-5.cpp
 * @brief 효율적인 화폐 구성
 * @author Sam Kim (samkim2626@gmail.com)
 * 
 * d[i] : i원을 만들 수 있는 최소한의 화폐 개수
 */
#include <iostream>

using namespace std;

int coin[100], d[10001];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        cin >> coin[i];
    }

    fill_n(d, 10001, 10001);
    d[0] = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = coin[i]; j <= m; j++)
        {
            if (d[j - coin[i]] != 10001)
            {
                d[j] = min(d[j], d[j - coin[i]] + 1);
            }
        }
    }

    if (d[m] == 10001)
    {
        cout << -1 << '\n';
    }
    else
    {
        cout << d[m] << '\n';
    }

    return 0;
}