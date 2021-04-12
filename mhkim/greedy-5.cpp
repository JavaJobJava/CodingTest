/**
 * @file greedy-5.cpp
 * @brief 볼링공 고르기
 * @author Sam Kim (samkim2626@gmail.com)
 */
#include <iostream>

using namespace std;

int balls[1000];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        cin >> balls[i];
    }

    sort(balls, balls + n);

    int count = 0;
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (balls[i] != balls[j])
            {
                count++;
            }
        }
    }

    cout << count << '\n';

    return 0;
}