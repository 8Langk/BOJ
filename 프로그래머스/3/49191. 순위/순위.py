from collections import defaultdict, deque
def bfs(start, graph):
    queue = deque([start])
    visited = set()
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited

def solution(n, results):
    answer = 0
    
    # 각 선수의 승리와 패배를 저장
    win = defaultdict(set)
    lose= defaultdict(set)
    
    for wins, loses in results:
        win[wins].add(loses)
        lose[loses].add(wins)
    print(win)
    print(lose)
    # 모든 선수의 순위를 계산

    for player in range(1, n + 1):
        wins = bfs(player, win)
        loses = bfs(player, lose)
        
        # 자신을 제외한 모든 선수와의 승패 관계가 확실하면 순위 확정
        if len(wins) + len(loses) == n - 1:
            print(player)
            answer += 1
    
    return answer
