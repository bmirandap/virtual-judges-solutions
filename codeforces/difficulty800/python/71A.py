# Problem ID: 71A
# Name: Way Too Long Words

n = int(input())
for i in range(0, n):
    word = input()
    if len(word) > 10:
        print(word[0] + str(len(word)-2) + word[-1])
    else:
        print(word)