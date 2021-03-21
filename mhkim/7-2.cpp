/**
 * @file 7-2.cpp
 * @brief 부품 찾기
 * @author Sam Kim (samkim2626@gmail.com)
 */
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> vN, vM;
int res;

int binarySearch(int target, int start, int end)
{
    while (start <= end)
    {
        int mid = (start + end) / 2;
        if (vN[mid] == target)
        {
            return mid;
        }
        else if (vN[mid] > target)
        {
            end = mid - 1;
        }
        else
        {
            start = mid + 1;
        }
    }
    if (start > end)
    {
        return -1;
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int num;
        cin >> num;
        vN.push_back(num);
    }
    sort(vN.begin(), vN.end());

    int m;
    cin >> m;
    for (int i = 0; i < m; i++)
    {
        int num;
        cin >> num;
        vM.push_back(num);
    }

    for (int &i : vM)
    {
        res = binarySearch(i, 0, n - 1);
        if (res == -1)
        {
            cout << "no" << ' ';
        }
        else
        {
            cout << "yes" << ' ';
        }
    }

    return 0;
}