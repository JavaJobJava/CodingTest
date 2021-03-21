/**
 * @file 1920.cpp
 * @brief 수 찾기
 * @author Sam Kim (samkim2626@gmail.com)
 */
#include <iostream>
#include <algorithm>

using namespace std;

int n, a[100000];

int binarySearch(int target)
{
    int start = 0, end = n - 1;
    int mid;

    while (start <= end)
    {
        mid = (start + end) / 2;
        if (a[mid] == target)
        {
            return mid;
        }
        else if (a[mid] > target)
        {
            end = mid - 1;
        }
        else
        {
            start = mid + 1;
        }
    }
    return -1;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    sort(a, a + n);

    int m;
    cin >> m;
    for (int i = 0; i < m; i++)
    {
        int num;
        cin >> num;

        int result = binarySearch(num);
        result == -1 ? cout << 0 << '\n' : cout << 1 << '\n';
    }

    return 0;
}