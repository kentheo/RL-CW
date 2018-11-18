

def generateCIDTrace(cid=[1,2,7,2,2,1,0,4]):
    n = len(cid) + 1
    s = [0]*(n)
    r = [0]*(n)
    for i in range(n-1):
        s[i] = (cid[i]+1)%3
        r[i+1] = cid[i]%2
    zipped = list(zip(s[:-1], r[1:]))
    print(zipped)

generateCIDTrace()
