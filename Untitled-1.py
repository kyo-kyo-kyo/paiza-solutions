N = int(input())
for _ in range(N):
    S = input().split()
    t = []
    t.append(S[0].split(":"))
    h = t[0][0]
    m = t[0][1]
    h = int(h) + int(S[1])
    m = int(m) + int(S[2])
    print(t)
    if int(m) >= 60:
        h = int(h) + 1
        m = int(m) - 60
    if int(h) >= 24:
        h = int(h) - 24
    if len(str(h)) == 1:
        h = "0"+str(h)
    if len(str(m)) == 1:
        m = "0"+str(m)
    print(f"{h}"":",f"{m}",sep="")