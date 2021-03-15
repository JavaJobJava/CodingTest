/**
 * @file 14501v2.cpp
 * @brief 퇴사
 * @author Sam Kim (samkim2626@gmail.com)
 * 
 * 시간복잡도 O(N^2)
 */
#include <iostream>

using namespace std;

int t[16];
int p[16];
int d[17];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    for (int i = 1; i <= n; i++)
    {
        cin >> t[i] >> p[i];
    }

    for (int i = 1; i <= n + 1; i++)
    {
        for (int j = 1; j < i; j++)
        {
            if (j + t[j] <= i)
            {
                d[i] = max(d[i], d[j] + p[j]);
            }
        }
    }

    cout << d[n + 1] << '\n';

    return 0;
}