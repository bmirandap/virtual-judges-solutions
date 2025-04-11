# Problem ID: 1500
# Title: Array Palindrome?

n = int(input())
array = list(map(int, input().split()))
array_inv = array[::-1]
if array == array_inv:
    print("SI")
else:
    print("NO")