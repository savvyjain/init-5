import sys
lines = sys.stdin.read().strip().split('\n')
pairs = (map(int, l.split()) for l in lines)
ranges = (range(s, e) for s, e in pairs)
print(len(set().union(*ranges)))