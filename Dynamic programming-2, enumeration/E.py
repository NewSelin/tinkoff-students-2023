n, a, b, c, m = map(int, input().split())
def f(i):
    return (a*i%m*i + b*i + c) % m
def ab_pruning(state, alpha, beta, player, steps):
    if steps == n:
        return f(state)
    if player == 1:
        for i in range(2):
            beta = min(beta, ab_pruning(state*2+i, alpha, beta, 0, steps+1))
            if beta <= alpha:
                break
        return beta
    else:
        for i in range(2):
            alpha = max(alpha, ab_pruning(state*2+i, alpha, beta, 1, steps+1))
            if beta <= alpha:
                break
        return alpha
print(ab_pruning(0, 0, m-1, 0, 0))