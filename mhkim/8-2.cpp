/**
 * @file 8-2.cpp
 * @brief 1로 만들기
 * @author Sam Kim (samkim2626@gmail.com)
 * 
 * d[i] : 정수 i가 1로 만들어지는 연산 횟수의 최솟값
 */
#include <iostream>

using namespace std;

int d[30001];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int x;
    cin >> x;

    d[1] = 0;
    for (int i = 2; i <= x; i++)
    {
        d[i] = d[i - 1] + 1;

        if (i % 2 == 0)
        {
            d[i] = min(d[i], d[i / 2] + 1);
        }
        if (i % 3 == 0)
        {
            d[i] = min(d[i], d[i / 3] + 1);
        }
        if (i % 5 == 0)
        {
            d[i] = min(d[i], d[i / 5] + 1);
        }
    }

    cout << d[x] << '\n';

    return 0;
}