/**
 * @file 11399.cpp
 * @brief ATM
 * @author Sam Kim (samkim2626@gmail.com)
 */
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    int p[1000];
    for (int i = 0; i < n; i++)
    {
        cin >> p[i];
    }
    sort(p, p + n);

    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        sum += p[i] * (n - i);
    }

    cout << sum << '\n';

    return 0;
}