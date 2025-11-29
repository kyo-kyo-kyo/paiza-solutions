N = int(input())
words = []
for _ in range(N):
    words.append(sorted(input()))
    print(words)    

for i in range(len(words)):
    