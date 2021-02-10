/**
 * @file 15904.cpp
 * @brief UCPC는 무엇의 약자일까?
 * @author Sam Kim (samkim2626@gmail.com)
 */
#include <iostream>
#include <string>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    getline(cin, s);

    int cnt = 0;
    for (int i = 0; i < s.size(); i++)
    {
        if (s[i] == 'U' && cnt == 0)
        {
            cnt++;
        }
        else if (s[i] == 'C' && (cnt == 1 || cnt == 3))
        {
            cnt++;
        }
        else if (s[i] == 'P' && cnt == 2)
        {
            cnt++;
        }
    }

    if (cnt == 4)
    {
        cout << "I love UCPC" << '\n';
    }
    else
    {
        cout << "I hate UCPC" << '\n';
    }

    return 0;
}