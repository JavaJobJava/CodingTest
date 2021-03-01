/**
 * @file 8-3.cpp
 * @brief 개미 전사
 * @author Sam Kim (samkim2626@gmail.com)
 * 
 * d[i] : i개의 식량창고에서 얻을 수 있는 식량의 최댓값
 */
#include <iostream>

using namespace std;

int n, container[101], d[101];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        cin >> container[i];
    }

    d[0] = 0;
    d[1] = container[1];
    for (int i = 2; i <= n; i++)
    {
        d[i] = max(d[i - 1], d[i - 2] + container[i]);
    }

    cout << d[n] << '\n';

    return 0;
}