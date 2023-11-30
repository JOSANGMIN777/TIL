# 백준 10825 국영수 실버4

import sys

N = int(input())
table = list(input().split() for _ in range(N))


new_table=sorted(table, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(len(new_table)):
    print(new_table[i][0])

