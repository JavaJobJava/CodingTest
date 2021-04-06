/**
 * @file greedy-2.cpp
 * @brief 곱하기 혹은 더하기
 * @author Sam Kim (samkim2626@gmail.com)
 */
#include <iostream>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;

    int sum = 0;
    for (int i = 0; i < s.length(); i++)
    {
        int n = s[i] - '0';
        int hap = sum + n;
        int gop = sum * n;
        if (hap < gop)
        {
            sum = gop;
        }
        else
        {
            sum = hap;
        }
    }

    cout << sum << '\n';

    return 0;
}