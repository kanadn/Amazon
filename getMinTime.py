circularAdjList = {}
n = 10
servers = [4,6,2,9]

# for i in range(1, n+1):
#     circularAdjList[i] = [(i-1)%n, (i+1)%n, False]

# circularAdjList[1][0] = n
# circularAdjList[n-1][1] = n

# for s in servers:
#     circularAdjList[s][2] = True

# print(circularAdjList)

# minTime = float('inf')

# def getMinTime(i, timeTaken, counted, previ):
#     global minTime
#     # print(i, timeTaken, counted, previ)
#     if timeTaken > n:
#         return
#     if circularAdjList[i][2]:
#         counted += 1
#         if counted == len(servers):
#             minTime = min(minTime, timeTaken)
#             return
#     if previ == -1 or previ == circularAdjList[i][1]:
#         getMinTime(circularAdjList[i][0], timeTaken+1, counted, i)
#     if previ == -1 or previ == circularAdjList[i][0]:
#         getMinTime(circularAdjList[i][1], timeTaken+1, counted, i)
    

# for s in servers:
#     getMinTime(s, 0, 0, -1)

def get_min_connect_time(servers , n):
    servers.sort()
    diff = 0
    max_diff = float('-inf')
    for i in range(0,len(servers)-1):
        diff += abs(servers[i+1]-servers[i])
        max_diff = max(max_diff, abs(servers[i+1]-servers[i]))
        
    diff += (n-(servers[-1]-servers[0]))
    max_diff = max(max_diff, (n-(servers[-1]-servers[0])))

    return diff-max_diff

def getMinTime(total_servers, servers):
    servers.sort()
    
    max_gap = 0
    n = len(servers)
    
    # find the maximum gap between consecutive servers in the sorted list
    for i in range(1, n):
        gap = servers[i] - servers[i-1]
        max_gap = max(max_gap, gap)
    
    # compute the wrap-around gap: from the last server to the first server via the circle's end
    wrap_gap = servers[0] + total_servers - servers[-1]
    max_gap = max(max_gap, wrap_gap)
    
    # the minimum time is the total circle length minus the largest gap
    return total_servers - max_gap

# print(get_min_connect_time([4,6,2,9], 10) == getMinTime(10, [4,6,2,9]))
# print(get_min_connect_time([1,2,3,4,5], 5) == getMinTime(5, [1,2,3,4,5]))
# print(get_min_connect_time([1,2,3,4,5,10], 10) == getMinTime(10, [1,2,3,4,5,10]))
# print(get_min_connect_time([2,6,8], 8) == getMinTime(8, [2,6,8]))
# print(get_min_connect_time([1,2,4,6,10], 10) == getMinTime(10, [1,2,4,6,10]))
# print(get_min_connect_time([1,5], 5) == getMinTime(5, [1,5]))
print(get_min_connect_time([1,2,3,4,5], 5))
print(get_min_connect_time([1,2,3,4,5,10], 10))
print(get_min_connect_time([2,6,8], 8))
print(get_min_connect_time([1,2,4,6,10], 10))