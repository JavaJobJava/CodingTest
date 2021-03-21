/**
 * @file 1946.cpp
 * @brief 신입 사원 - 그리디
 * @author Sam Kim (samkim2626@gmail.com)
 */
#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;

        vector<pair<int, int>> v;
        for (int i = 0; i < n; i++)
        {
            int f, s;
            cin >> f >> s;
            v.push_back(make_pair(f, s));
        }

        sort(v.begin(), v.end());

        int min = v[0].second;
        int cnt = 1;
        for (int i = 1; i < n; i++)
        {
            if (min > v[i].second)
            {
                min = v[i].second;
                cnt++;
            }
        }

        cout << cnt << '\n';
    }

    return 0;
}