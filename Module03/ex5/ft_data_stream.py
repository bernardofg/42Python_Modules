def next_seed(seed):
    return (seed * 1103515245 + 12345) % 2147483648


def events(n, seed):
    rng = next_seed(seed)

    for i in range(1, n + 1):
        r1 = next(rng)
        r2 = next(rng)
        r3 = next(rng)

def main():
