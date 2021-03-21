/**
 * @file 6-3.cpp
 * @brief 성적이 낮은 순서로 학생 출력하기
 * @author Sam Kim (samkim2626@gmail.com)
 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <string>

using namespace std;

bool compare(pair<string, int> a, pair<string, int> b)
{
    return a.second < b.second;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<pair<string, int>> v;
    for (int i = 0; i < n; i++)
    {
        string name;
        int score;
        cin >> name >> score;
        v.push_back(make_pair(name, score));
    }

    sort(v.begin(), v.end(), compare);

    for (auto &i : v)
    {
        cout << i.first << ' ';
    }

    return 0;
}