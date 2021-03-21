/**
 * @file 6-4.cpp
 * @brief 두 배열의 원소 교체
 * @author Sam Kim (samkim2626@gmail.com)
 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;

    vector<int> vA, vB;
    for (int i = 0; i < n; i++)
    {
        int a;
        cin >> a;
        vA.push_back(a);
    }
    for (int i = 0; i < n; i++)
    {
        int b;
        cin >> b;
        vB.push_back(b);
    }

    sort(vA.begin(), vA.end());
    reverse(vB.begin(), vB.end());

    for (int i = 0; i < k; i++)
    {
        if (vA[i] < vB[i])
        {
            vA[i] = vB[i];
        }
        else
        {
            break;
        }
    }

    int sum = accumulate(vA.begin(), vA.end(), 0);
    cout << sum << '\n';

    return 0;
}