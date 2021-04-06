/**
 * @file greedy-3.cpp
 * @brief 문자열 뒤집기
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

    int one2zero, zero2one = 0;
    for (int i = 1; i < s.length(); i++)
    {
        if (s[i - 1] == '0' && s[i - 1] != s[i])
        {
            zero2one++;
        }
        else if (s[i - 1] == '1' && s[i - 1] != s[i])
        {
            one2zero++;
        }
    }

    cout << min(zero2one, one2zero) << '\n';

    return 0;
}