/**
 * @file greedy-6.cpp
 * @brief 무지의 먹방 라이브
 * @author Sam Kim (samkim2626@gmail.com)
 * 
 * 1. 처음에 tni 음식 시간, 음식 인덱스 pair로 만들어서 정렬함 -> 우선순위큐로
 * 2. 우선순위큐 top이 시간이 가장 적게 걸리는 음식 -> 계산해서 k에서 빼기, 우선순위큐에서 빼기
 * 3. 다음 반복에서 계산했을 때 k보다 크면 빼지 않고 다음에 먹어야 할 음식 인덱스 출력
 */
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>
#include <utility>
#include <queue>

using namespace std;

int solution(vector<int> food_times, long long k)
{
    int answer = 0;

    long long sum = accumulate(food_times.begin(), food_times.end(), 0LL);
    if (sum <= k)
    {
        return -1;
    }

    // 우선순위 큐로 time과 index를 저장: 시간이 가장 적게 걸리는 음식 순
    priority_queue<pair<int, int>> tni;
    for (int i = 0; i < food_times.size(); i++)
    {
        tni.push(make_pair(-food_times[i], i + 1)); // 파이썬은 +
    }

    int nFoods = food_times.size(); // 남은 음식의 개수
    int prev = 0;                   // 이전 음식 개수
    while (1)
    {
        pair<int, int> top = tni.top();
        if ((-top.first - prev) * nFoods > k) // 더 이상 돌지 못하는 경우
        {
            break;
        }
        k -= (-top.first - prev) * nFoods;
        prev = -top.first;
        tni.pop();
        nFoods--;
    }

    // 존재하는 음식 인덱스 정렬
    vector<int> remains;
    while (!tni.empty())
    {
        int idx = tni.top().second;
        remains.push_back(idx);
        tni.pop();
    }
    sort(remains.begin(), remains.end());

    answer = remains[int(k % remains.size())];

    return answer;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> food_times;
    for (int i = 0; i < n; i++)
    {
        int time;
        cin >> time;
        food_times.push_back(time);
    }

    long long k;
    cin >> k;

    cout << solution(food_times, k) << '\n';

    return 0;
}