/**
 * @file 8-4.cpp
 * @brief 바닥 공사
 * @author Sam Kim (samkim2626@gmail.com)
 * 
 * d[i] : 가로 길이가 i, 세로 길이가 2인 바닥을 채우는 모든 경우의 수
 */
#include <iostream>

using namespace std;

int d[1001];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    d[1] = 1;
    d[2] = 3;
    for (int i = 3; i <= n; i++)
    {
        d[i] = (d[i - 1] + d[i - 2] * 2) % 796796;
    }

    cout << d[n] << '\n';

    return 0;
}