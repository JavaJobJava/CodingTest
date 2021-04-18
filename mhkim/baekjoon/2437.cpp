/**
 * @file 2437.cpp
 * @brief 저울
 * @author Sam Kim (samkim2626@gmail.com)
 * 
 * Greedy 
 * 아이디어
 * 
 * 만들 수 없는 최소의 양수 구하기 - 작은 추를 먼저, 잴 수 없는 무게 찾기
 * n번째 원소까지의 누적합 / n번째 원소
 * 올리려는 추가 누적합+1 보다 더 크다면, 누적합+1이 측정할 수 없는 최솟값 (추를 쌓아서 누적합 이하의 수를 모두 만들 수 있다는 것이 보장됨)
 */
#include <iostream>
#include <algorithm>

using namespace std;

int choo[1000];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> choo[i];
    }
    sort(choo, choo + n);

    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        if (sum + 1 < choo[i])
        {
            break;
        }
        sum += choo[i];
    }

    cout << sum + 1 << '\n';

    return 0;
}