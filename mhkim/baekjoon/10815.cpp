/**
 * @file 10815.cpp
 * @brief 숫자 카드
 * @author Sam Kim (samkim2626@gmail.com)
 */

#include <iostream>
#include <algorithm>

using namespace std;

int card[500001];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> card[i];
    }
    sort(card, card + n);

    int m;
    cin >> m;
    while (m--)
    {
        int num;
        cin >> num;
        bool result = binary_search(card, card + n, num);
        result ? cout << 1 << ' ' : cout << 0 << ' ';
    }
    cout << '\n';

    return 0;
}