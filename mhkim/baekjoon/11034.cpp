/**
 * @file 11034.cpp
 * @brief 캥거루 세마리2 - 그리디
 * @author Sam Kim (samkim2626@gmail.com)
 * 
 * 이미 정렬되어 있어서 뽑기만 하면 된다.
 */
#include <iostream>

using namespace std;

int main()
{
    int a, b, c;
    while (cin >> a >> b >> c)
    {
        cout << max(b - a - 1, c - b - 1) << '\n';
    }

    return 0;
}
