#CH10 그래프이론
#예제 10-2
#경로 압축 기법

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]