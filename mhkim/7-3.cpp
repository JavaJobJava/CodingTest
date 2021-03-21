/**
 * @file 7-3.cpp
 * @brief 떡볶이 떡 만들기
 * @author Sam Kim (samkim2626@gmail.com)
 */
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> v;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        int num;
        cin >> num;
        v.push_back(num);
    }

    int start = 0;
    int end = *max_element(v.begin(), v.end());
    int rst = 0;
    while (start <= end)
    {
        int total = 0;
        int mid = (start + end) / 2;
        for (auto &&i : v)
        {
            if (i > mid)
            {
                total += i - mid;
            }
        }

        if (total < m)
        {
            end = mid - 1;
        }
        else
        {
            rst = mid;
            start = mid + 1;
        }
    }

    cout << rst << '\n';

    return 0;
}