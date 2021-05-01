/**
 * @file 5557.cpp
 * @brief 1학년
 * @author Sam Kim (samkim2626@gmail.com)
 * 
 * 못 풀어서 솔루션 참고. 문제 풀이, 접근 방법 다시 확인
 * 
 * 2차원배열
 * dp[i][j] : i번째 수까지 계산했을 때 j값을 만드는 올바른 등식의 수
 * 1. j-num[i] >= 0 / 2. j+num[i] <= 20
 * 
 * dp테이블 int -> long long (2^63-1)
 */
#include <iostream>

using namespace std;

int num[101];
long long dp[101][21];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        cin >> num[i];
    }

    dp[1][num[1]] = 1; // 첫 번째 수까지 경우의 수 초기화
    for (int i = 2; i <= n; i++)
    {
        for (int j = 0; j <= 20; j++)
        {
            if (dp[i - 1][j] >= 0)
            {
                if (j - num[i] >= 0)
                {
                    dp[i][j - num[i]] += dp[i - 1][j];
                }
                if (j + num[i] <= 20)
                {
                    dp[i][j + num[i]] += dp[i - 1][j];
                }
            }
        }
    }

    cout << dp[n - 1][num[n]] << '\n';

    return 0;
}