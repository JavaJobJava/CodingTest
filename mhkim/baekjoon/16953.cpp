/**
 * @file 16953.cpp
 * @brief A -> B
 * @author Sam Kim (samkim2626@gmail.com)
 */
#include <iostream>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b;
    cin >> a >> b;

    int cnt = 0;
    while (1)
    {
        if (a > b)
        {
            cout << -1 << '\n';
            break;
        }
        if (a == b)
        {
            cout << cnt + 1 << '\n';
            break;
        }

        if (b % 10 == 1)
        {
            b /= 10;
        }
        else if (b % 2 == 0)
        {
            b /= 2;
        }
        else
        {
            cout << -1 << '\n';
            break;
        }
        cnt++;
    }

    return 0;
}