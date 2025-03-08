circularAdjList = {}
n = 10
servers = [4,6,2,9]

for i in range(1, n+1):
    circularAdjList[i] = [(i-1)%n, (i+1)%n, False]

circularAdjList[1][0] = n
circularAdjList[n-1][1] = n

for s in servers:
    circularAdjList[s][2] = True

print(circularAdjList)

minTime = float('inf')

def getMinTime(i, timeTaken, counted, previ):
    global minTime
    # print(i, timeTaken, counted, previ)
    if timeTaken > n:
        return
    if circularAdjList[i][2]:
        counted += 1
        if counted == len(servers):
            minTime = min(minTime, timeTaken)
            return
    if previ == -1 or previ == circularAdjList[i][1]:
        getMinTime(circularAdjList[i][0], timeTaken+1, counted, i)
    if previ == -1 or previ == circularAdjList[i][0]:
        getMinTime(circularAdjList[i][1], timeTaken+1, counted, i)
    

for s in servers:
    getMinTime(s, 0, 0, -1)

print(minTime)