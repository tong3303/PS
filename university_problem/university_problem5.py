import sys
from functools import lru_cache
input = sys.stdin.read
MOD = 1000007
P1, P2 = 29, 34483

fact1 = [1] * P1
fact2 = [1] * P2
for i in range(1, P1): fact1[i] = fact1[i-1] * i % P1
for i in range(1, P2): fact2[i] = fact2[i-1] * i % P2

inv1 = [1] * P1
inv2 = [1] * P2
inv1[P1-1] = pow(fact1[P1-1], P1-2, P1)
inv2[P2-1] = pow(fact2[P2-1], P2-2, P2)
for i in range(P1-2, -1, -1): inv1[i] = inv1[i+1] * (i+1) % P1
for i in range(P2-2, -1, -1): inv2[i] = inv2[i+1] * (i+1) % P2

INV29 = pow(P1, -1, P2)

def lucas(n, r, p, fact, inv):
    res = 1
    while n > 0 or r > 0:
        ni, ri = n % p, r % p
        if ri > ni:
            return 0
        res = res * fact[ni] % p * inv[ri] % p * inv[ni-ri] % p
        n //= p
        r //= p
    return res

@lru_cache(maxsize=None)
def nCr(n, r):
    if r < 0 or r > n or n < 0:
        return 0
    r1 = lucas(n, r, P1, fact1, inv1)
    r2 = lucas(n, r, P2, fact2, inv2)
    t = (r2 - r1) * INV29 % P2
    return (r1 + P1 * t) % MOD

def get_paths(x1, y1, x2, y2):
    return nCr(abs(x2-x1) + abs(y2-y1), abs(x2-x1))

def on_path(x1, y1, x2, y2, px, py):
    return (min(x1,x2) <= px <= max(x1,x2) and
            min(y1,y2) <= py <= max(y1,y2))

def get_paths_via(x1, y1, x2, y2, px, py):
    if not on_path(x1, y1, x2, y2, px, py):
        return 0
    return get_paths(x1, y1, px, py) * get_paths(px, py, x2, y2) % MOD

def solve():
    lines = input().split()
    T = int(lines[0])
    idx = 1
    out = []
    for _ in range(T):
        sx=int(lines[idx]);   sy=int(lines[idx+1])
        tx=int(lines[idx+2]); ty=int(lines[idx+3])
        ax=int(lines[idx+4]); ay=int(lines[idx+5])
        bx=int(lines[idx+6]); by=int(lines[idx+7])
        idx += 8

        path_A = get_paths_via(sx,sy,tx,ty,ax,ay)
        path_B = get_paths_via(sx,sy,tx,ty,bx,by)

        path_AB = 0
        if (on_path(sx,sy,tx,ty,ax,ay) and
            on_path(sx,sy,tx,ty,bx,by) and
            on_path(ax,ay,tx,ty,bx,by)):
            path_AB = get_paths(sx,sy,ax,ay) * get_paths(ax,ay,bx,by) % MOD * get_paths(bx,by,tx,ty) % MOD

        path_BA = 0
        if (on_path(sx,sy,tx,ty,ax,ay) and
            on_path(sx,sy,tx,ty,bx,by) and
            on_path(bx,by,tx,ty,ax,ay)):
            path_BA = get_paths(sx,sy,bx,by) * get_paths(bx,by,ax,ay) % MOD * get_paths(ax,ay,tx,ty) % MOD

        ans = (path_A + path_B - path_AB - path_BA + 2*MOD) % MOD
        out.append(str(ans))

    print('\n'.join(out))

import time
curr_time = time.time()
solve()
print(time.time() - curr_time)