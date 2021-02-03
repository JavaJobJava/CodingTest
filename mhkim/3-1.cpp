/**
 * @file 3-1.cpp
 * @brief 거스름돈
 * @author Sam Kim (samkim2626@gmail.com)
 */

#include <iostream>

using namespace std;

int n = 1260;
int cnt = 0;
int coinTypes[4] = {500, 100, 50, 10};

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    for (int i = 0; i < 4; i++)
    {
        int coin = coinTypes[i];
        cnt += n / coin;
        n %= coin;
    }

    cout << cnt << '\n';

    return 0;
}