# Problem ID: 1330
# Title: Rotando cadenas

s, r = input().split()
n = int(r)
print(s[-n:] + s[:-n])