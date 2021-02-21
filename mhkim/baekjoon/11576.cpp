/**
 * @file 11576.cpp
 * @brief Base Conversion 예전에 풀었지만...
 * @author Sam Kim (samkim2626@gmail.com)
 */
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b;
    cin >> a >> b;
    int m;
    cin >> m;

    // A -> 10
    int res = 0;
    for (int i = 0; i < m; i++)
    {
        int n;
        cin >> n;

        res = res * a + n;
    }

    // 10 -> B
    vector<int> v;
    while (res > 0)
    {
        v.push_back(res % b);
        res /= b;
    }
    reverse(v.begin(), v.end());

    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i] << ' ';
    }

    return 0;
}