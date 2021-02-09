graph = [[]for _ in range(3)] # 3개의 행 [] 을 가진 AdjacencyList

graph[0].append((1,2))
graph[0].append((3,4))
graph[0].append(5)
graph[0].append((5))

graph[1].append((1,3))  #append 는 stack 마냥 뒤로 넣는다?
graph[1].insert(0,1)    #insert 는 insert(index, value)

graph[2].append((1,5))




print(graph)