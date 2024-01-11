from collections import deque

def solution(rows, columns, queries):
    x, graph = 1, []
    for _ in range(rows):
        temp = []
        for i in range(columns):
            temp.append(x)
            x = x + 1
        graph.append(temp)    
    answer = []

    length = len(queries)
    for i in range(length):
        x1, y1, x2, y2 = queries[i]
        temp = deque([])
        minimum = 10001
        temp.append(graph[x1-1][y1-1])
        if minimum > temp[0] :
            minimum = temp[0]
        for j in range(y2-y1):
            temp.append(graph[x1-1][y1+j])
            if minimum > temp[-1] :
                minimum = temp[-1]
            graph[x1-1][y1+j] = temp.popleft()
        for k in range(x2-x1):
            temp.append(graph[x1+k][y2-1])
            if minimum > temp[-1] :
                minimum = temp[-1]
            graph[x1+k][y2-1] = temp.popleft()
        for l in range(y2-y1):
            temp.append(graph[x2-1][y2 -l -2])
            if minimum > temp[-1] :
                minimum = temp[-1]
            graph[x2-1][y2-l-2] = temp.popleft()
        for m in range(x2-x1):
            temp.append(graph[x2-2-m][y1-1])
            if minimum > temp[-1] :
                minimum = temp[-1]
            graph[x2-2-m][y1-1] = temp.popleft()
        answer.append(minimum)

    # for i in range(rows):
    #     print(graph[i])

    return answer



test1 = [6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]]
test2 = [3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]]
test3 = [100, 97, [[1,1,100,97]]]


print(solution(test2[0],test2[1],test2[2]))
