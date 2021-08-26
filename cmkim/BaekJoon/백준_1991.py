def rab(node):
    if node == '.':
        return
    print(node, end='')
    rab(tree[node][0])
    rab(tree[node][1])


def arb(node):
    if node == '.':
        return
    arb(tree[node][0])
    print(node, end='')
    arb(tree[node][1])


def abr(node):
    if node == '.':
        return
    abr(tree[node][0])
    abr(tree[node][1])
    print(node, end='')


n = int(input())
tree = {}

for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]

print(tree)
rab('A')
print('')
arb('A')
print('')
abr('A')
