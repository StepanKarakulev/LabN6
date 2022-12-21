import sys
sys.setrecursionlimit(10**9)

flag = 0
def is_bin_tree(potok, minx, maxx):
    global flag
    if potok[0] <= minx or potok[0] >= maxx:
        flag = 1
        return 'NO'
    if potok[1] != 0 and potok[2] != 0 and flag == 0:
        is_bin_tree(a[potok[1]-1], minx, potok[0])
        is_bin_tree(a[potok[2]-1], potok[0], maxx)
    if potok[1] != 0 and potok[2] == 0 and flag == 0:
        is_bin_tree(a[potok[1]-1], minx, potok[0])
    if potok[1] == 0 and potok[2] != 0 and flag == 0:
        is_bin_tree(a[potok[2]-1], potok[0], maxx)
    if flag == 0:
        return "YES"
    if flag == 1:
        return 'NO'

n = int(input())
minx = -(10**20)
maxx = 10**20
if n == 0:
    print('YES')
else:
    a = list()
    for i in range(n):
        t = list(map(int, input().split()))
        a.append(t)
    print(is_bin_tree(a[0], minx, maxx))