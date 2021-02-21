/**
 * @file 5430.cpp
 * @brief AC
 * @author Sam Kim (samkim2626@gmail.com)
 */
#include <iostream>
#include <string>
#include <deque>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--)
    {
        string p, strX;
        int n;
        cin >> p >> n >> strX;

        // x입력 배열 처리
        deque<int> dq;
        int x = 0;
        for (int i = 0; i < strX.size(); i++)
        {
            if (strX[i] >= '0' && strX[i] <= '9')
            {
                x *= 10;
                x += int(strX[i] - '0');
            }
            else
            {
                if (x == 0)
                {
                    continue;
                }

                dq.push_back(x);
                x = 0;
            }
        }

        // 함수 수행
        bool dir = true, error = false;
        for (int i = 0; i < p.size(); i++)
        {
            if (p[i] == 'R')
            {
                dir = !dir;
            }
            else if (p[i] == 'D')
            {
                if (dq.empty())
                {
                    cout << "error" << '\n';
                    error = true;
                    break;
                }
                else
                {
                    if (dir)
                    {
                        dq.pop_front();
                    }
                    else
                    {
                        dq.pop_back();
                    }
                }
            }
        }

        if (!error)
        {
            cout << "[";
        }
        while (!dq.empty())
        {
            if (dir)
            {
                cout << dq.front();
                dq.pop_front();
            }
            else
            {
                cout << dq.back();
                dq.pop_back();
            }

            if (!dq.empty())
            {
                cout << ",";
            }
        }
        if (!error)
        {
            cout << "]" << '\n';
        }
    }

    return 0;
}