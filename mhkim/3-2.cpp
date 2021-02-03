/**
 * @file 3-2.cpp
 * @brief 큰 수의 법칙
 * @author Sam Kim (samkim2626@gmail.com)
 */

#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int numbs[1000] = {0};
    int n, m, k;
    cin >> n >> m >> k;

    for (int i = 0; i < n; i++)
    {
        cin >> numbs[i];
    }

    sort(numbs, numbs + n);
    int f = numbs[n - 1];
    int s = numbs[n - 2];

    int result = 0;
    while (1)
    {
        if (m == 0)
            break;
        for (int i = 0; i < k; i++)
        {
            result += f;
            m--;
            if (m == 0)
                break;
        }
        result += s;
        m--;
    }

    cout << result << '\n';

    return 0;
}