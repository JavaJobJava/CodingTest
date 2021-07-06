vowels = ['a', 'e', 'i', 'o', 'u']

l, c = map(int, input().split())
arr = list(map(str, input().split()))
arr.sort()
answer = [''] * l


def recur(a, b):
    if a == l:
        if check():
            print("".join(answer))

        return

    for i in range(b, c):
        answer[a] = arr[i]
        recur(a + 1, i + 1)


def check():
    m_count, j_count = 0, 0  # 모음, 자음 카운트
    for i in range(l):
        if answer[i] in vowels:  # 모음이라면
            m_count += 1
        else:
            j_count += 1
    if m_count >= 1 and j_count >= 2:
        return True
    else:
        return False


recur(0, 0)
