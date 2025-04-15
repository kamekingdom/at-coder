def solve(N, M, friendships):
    from collections import defaultdict
    
    # Use a dictionary of sets to keep track of friendships (adjacency list)
    friends = defaultdict(set)
    for A, B in friendships:
        friends[A].add(B)
        friends[B].add(A)
    
    # Set to track new possible friendships without duplication
    new_relationships = set()
    
    # Process each user X
    for X in range(1, N + 1):
        # Look at all friends Y of X
        for Y in friends[X]:
            # Look for friends Z of Y that are not already friends with X
            # And ensure Z is not Y (avoid self-loops)
            for Z in friends[Y]:
                if Z != X and Z not in friends[X]:
                    # Sort the pair (X, Z) to avoid duplication
                    # Always make the pair (min, max)
                    new_relationships.add((min(X, Z), max(X, Z)))
    
    # The number of possible new friendships is the size of this set
    print(len(new_relationships))

# Main part to take inputs
N, M = map(int, input().split())
friendships = [list(map(int, input().split())) for _ in range(M)]
solve(N, M, friendships)
