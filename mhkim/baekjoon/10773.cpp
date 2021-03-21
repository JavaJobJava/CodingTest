/**
 * @file 10773.cpp
 * @brief 제로 - 구현
 * @author Sam Kim (samkim2626@gmail.com)
 */
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    cin >> k;

    vector<int> v;
    for (int i = 0; i < k; i++)
    {
        int n;
        cin >> n;
        if (n > 0)
        {
            v.push_back(n);
        }
        else if (n == 0)
        {
            v.pop_back();
        }
    }

    int sum = accumulate(v.begin(), v.end(), 0);
    cout << sum << '\n';

    return 0;
}