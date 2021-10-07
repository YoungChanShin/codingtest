import heapq


# 출발지, 목적지
def start(de, arr):
    queue = []
    # 출발지, 비용
    heapq.heappush(queue, (de, 0))

    visit = [0] * (city + 1)
    while queue:
        depart, cost = heapq.heappop(queue)
        # 목적지와 출발지가 같을 경우
        if depart == arr:
            return cost

        if visit[depart]:
            continue

        visit[depart] = 1
        for next_depart, next_cost in routes[depart]:
            if not visit[next_depart]:
                heapq.heappush(queue, (next_depart, cost + next_cost))


# 도시 개수
city = int(input())
# 버스 개수
bus = int(input())

# 노선표
routes = {x + 1: [] for x in range(city)}

# 노선표를 배열에 담음
for _ in range(bus):
    # x -> 출발지, y -> 도착지, z -> 비용
    x, y, z = map(int, input().split())
    # 딕셔너리 타입으로 정렬
    routes[x].append((y, z))

# 출발지, 도착지
departure, arrival = map(int, input().split())
print(start(departure, arrival))
