/**
 * @file 4-1.cpp
 * @brief 상하좌우
 * @author Sam Kim (samkim2626@gmail.com)
 */
#include <iostream>
#include <string>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int x = 1, y = 1;
    int n;
    cin >> n;
    cin.ignore();

    string s;
    getline(cin, s);
    for (char c : s)
    {
        switch (c)
        {
        case 'L':
            if (y <= 1)
            {
                continue;
            }
            y--;
            break;
        case 'R':
            if (y >= n)
            {
                continue;
            }
            y++;
            break;
        case 'U':
            if (x <= 1)
            {
                continue;
            }
            x--;
            break;
        case 'D':   
            if (x >= n)
            {
                continue;
            }
            x++;
            break;
        default:
            break;
        }
    }

    cout << x << ' ' << y << '\n';

    return 0;
}