/**
 * @file greedy-4.cpp
 * @brief 만들 수 없는 금액
 * @author Sam Kim (samkim2626@gmail.com)
 * 
 * 아이디어 생각하기 어려움
 */
#include <iostream>

using namespace std;

int coins[1001];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> coins[i];
    }

    sort(coins, coins + n);

    int target = 1;
    // 아이디어!
    for (int i = 0; i < n; i++)
    {

        if (target < coins[i])
        {
            break;
        }
        target += coins[i];
    }

    cout << target << '\n';

    return 0;
}