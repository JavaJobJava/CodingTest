/**
 * @file 1783.cpp
 * @brief 병든 나이트 - 그리디
 * @author Sam Kim (samkim2626@gmail.com)
 */
#include <iostream>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    if (n == 1) // 처음 위치 밖에 안됨
    {
        cout << 1 << '\n';
    }
    else if (n == 2) // m이 커도 최대 4
    {
        cout << min((m + 1) / 2, 4);
    }
    else // 1번, 4번 번갈아서
    {
        if (m <= 6) // 최대 4칸
        {
            cout << min(m, 4) << '\n';
        }
        else // m > 6 부터는 한 칸 씩 움직일 수 있음
        {
            cout << m - 2 << '\n';
        }
    }

    return 0;
}