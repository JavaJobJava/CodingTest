/**
 * @file 6603.cpp
 * @brief 로또
 * @author Sam Kim (samkim2626@gmail.com)
 * 
 * 조합(combination)
 * kC6 k개 중에서 6개 뽑기
 * DFS?
 */
#include <iostream>
#include <vector>

using namespace std;

#define r 6

int k;
int s[13];
int arr[13];

void comb(int start, int depth)
{
    if (depth == r)
    {
        for (int i = 0; i < r; i++)
        {
            cout << arr[i] << ' ';
        }
        cout << '\n';
        return;
    }

    for (int i = start; i < k; i++)
    {
        arr[depth] = s[i];
        comb(i + 1, depth + 1);
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    while (1)
    {
        cin >> k;
        if (k == 0)
        {
            break;
        }

        for (int i = 0; i < k; i++)
        {
            cin >> s[i];
        }

        comb(0, 0);

        cout << '\n';
    }

    return 0;
}