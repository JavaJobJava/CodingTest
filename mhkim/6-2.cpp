/**
 * @file 6-2.cpp
 * @brief 위에서 아래로
 * @author Sam Kim (samkim2626@gmail.com)
 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<int> v;
    for (int i = 0; i < n; i++)
    {
        int num;
        cin >> num;
        v.push_back(num);
    }

    sort(v.begin(), v.end(), greater<>());

    for (auto &i : v)
    {
        cout << i << ' ';
    }

    return 0;
}