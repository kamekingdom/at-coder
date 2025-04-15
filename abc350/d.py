def max_new_friendships(N, M, friendships):
    from collections import defaultdict, deque
    
    # Graph initialization
    graph = defaultdict(set)
    
    # Building the graph with given friendships
    for a, b in friendships:
        graph[a].add(b)
        graph[b].add(a)
    
    # To count new possible friendships
    new_friendships = 0
    
    # Process each friendship once
    for a in range(1, N + 1):
        # We will check each friend of a's friends and see if we can connect them back to a
        to_add = set()
        visited = set()
        for b in graph[a]:
            if b > a:  # Only process each edge once, considering a < b to avoid duplicates
                for c in graph[b]:
                    if c != a and c not in graph[a] and (a, c) not in visited and (c, a) not in visited:
                        to_add.add(c)
                        visited.add((a, c))
        
        # Now add the new friendships to the graph and count them
        for c in to_add:
            graph[a].add(c)
            graph[c].add(a)
            new_friendships += 1
    
    return new_friendships

N, M = map(int, input().split())
friendships = [list(map(int, input().split())) for _ in range(M)]
print(max_new_friendships(N, M, friendships))