/**
 * @file greedy-1.cpp
 * @brief 모험가 길드
 * @author Sam Kim (samkim2626@gmail.com)
 * 
 * sort
 * 
 */
#include <iostream>
#include <algorithm>

using namespace std;

int mo[100001];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> mo[i];
    }

    sort(mo, mo + n);

    int nGroup = 0;
    int nMo = 0; // 현재 그룹에 포함된 모험가의 수
    for (int i = 0; i < n; i++)
    {
        nMo++;
        if (nMo >= mo[i])
        {
            nGroup++;
            nMo = 0;
        }
    }

    cout << nGroup << '\n';

    return 0;
}