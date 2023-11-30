# 백준 1715번 골드4

import heapq
import sys
read = sys.stdin.readline

N = int(read())
cards = []
for i in range(N):
    heapq.heappush(cards, int(read())) # 어디에 어떤걸 힙의 방식으로 넣으시겠어요

total = 0 # 우리의 답이 될 친구
while len(cards) > 1: # 카드 안의 원소들이 모두 합해져 하나로 수렴할 때 까지 돌아
    a = heapq.heappop(cards) # 힙큐의 첫번째 원소 뽑아서 담아
    b = heapq.heappop(cards) # 힙큐의 두번째 원소를 뽑아서 담아

    SUM = a+b # 위 두 원소를 더해요
    total += SUM # 더한 것은 토탈값을 내야하는 우리의 답에 더해놔주세요
    heapq.heappush(cards,SUM) # 카드에 위 두 원소를 더한 값을 힙의 방식으로 넣을 게요

print(total)
