/**
 * @file 3-4.cpp
 * @brief 1이 될 때까지
 * @author Sam Kim (samkim2626@gmail.com)
 */
#include <iostream>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;

    int cnt = 0;
    while (n >= k)
    {
        if (n == 1)
        {
            break;
        }

        if (n % k != 0)
        {
            n--;
        }
        else
        {
            n /= k;
        }
        cnt++;
    }

    cout << cnt << '\n';

    return 0;
}