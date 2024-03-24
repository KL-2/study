import sys
class Solution:
    def __init__(self):
        self.graph={}
    def addedge(self,node,neighbour):
        #无向图
        if node not in self.graph:
            self.graph[node]=[]
        self.graph[node].append(neighbour)
        if neighbour not in self.graph:
            self.graph[neighbour]=[]
        self.graph[neighbour].append(node)
  
    def addedgewithcost(self,start,end,cost):
        if start not in self.graph:
            self.graph[start]=[]
        self.graph[start].append((end,cost))
               
    def bfs(self,start):
        print(f"current algorithm:{sys._getframe().f_code.co_name}")
        # visited=[]
        # queue=[]
        # visited.append(start)
        # queue.append(start)
        visited=set()
        queue=set()
        visited.add(start)
        queue.add(start)
        while queue:
            s=queue.pop(0)#从队列中取出第一个元素
            for neighbour in self.graph[s]:
                if neighbour not in visited:
                    # visited.append(neighbour)
                    # queue.append(neighbour)
                    visited.add(neighbour)
                    queue.add(neighbour)
        return visited

    def dfs(self,start,visited=None):
        if visited is None:
            # visited=[]
            visited=set()
            # print(type(visited))#<class 'set'>相较于list不允许重复元素，但时间复杂度低
        if start not in visited:
            # visited.append(start)
            visited.add(start)
            for neighbour in self.graph.get(start,[]):
                self.dfs(neighbour,visited)
        return visited

    def ucs(self,start,goal):#uniform-cost-search
        visited=set()
        priorityqueue=[(0,start,[])]
        while priorityqueue:
            priorityqueue.sort(key=lambda x: x[0])
            cost,node,path=priorityqueue.pop(0)
            if node not in visited:
                visited.add(node)
                path+=[node]
                if node==goal:
                    return cost,path
                for neighbour,edgecost in self.graph.get(node,[]):
                    if neighbour not in visited:
                        priorityqueue.append((cost+int(edgecost),neighbour,path))
        return float("inf"),[]

    def dls(self,start,goal,limit):#depth-limited-search
        def dls_util(node,depth,path):#util工具
            if depth>limit:
                return False,[]
            if node==goal:
                return True,path+[node]
            for neighbour in self.graph.get(node,[]):
                found,result=dls_util(neighbour,depth+1,path+[node])
                if found:
                    return True,result
            return False,[]
        return dls_util(start,0,[])

    def ids(self,start,goal,maxdepth):#iterative-deepening-search
        for limit in range(1,maxdepth+1):
            found,path=self.dls(start,goal,limit)
            if found:
                return True,path
        return False,[]

    def bs(self,start,goal):#bidirectional-search
        if start == goal:
            return [start]

        # Initialize frontiers for both searches
        frontierstart = {start}
        frontiergoal = {goal}

        # Initialize paths
        pathstart = {start: [start]}
        pathgoal = {goal: [goal]}

        while frontierstart and frontiergoal:
            # Expand in forward direction
            nextfrontierstart = set()
            for u in frontierstart:
                for v in graph.graph[u]:
                    if v in frontiergoal:  # Check for me
                        return pathstart[u] + pathgoal[v][::-1][1:]
                        #pathgoal[v][::-1][1:]是pathgoal[v]对应的键值再去掉第一个
                        #即倒序然后再去除重复的那个节点
                    if v not in pathstart:
                        pathstart[v] = pathstart[u] + [v]
                        nextfrontierstart.add(v)
            frontierstart = nextfrontierstart

            # Expand in backward direction
            nextfrontiergoal = set()
            for u in frontiergoal:
                for v in graph.graph[u]:
                    if v in frontierstart:  # Check for meeting point
                        return pathstart[v] + pathgoal[u][::-1][1:]
                    if v not in pathgoal:
                        pathgoal[v] = pathgoal[u] + [v]
                        nextfrontiergoal.add(v)
            frontiergoal = nextfrontiergoal

        return []

    def heuristic(self,start,goal):
        for neighbour,edgecost in self.graph.get(start,[]):
            if neighbour==goal:
                return edgecost
        return 10000
    
    def gbfs(self,start,goal):#greedy bfs
        queue=[(start,[start])]
        visited=set([start])
        while queue:
            current,path=min(queue,key=lambda x:self.heuristic(x[0],goal))
            queue.remove((current,path))
            if current==goal:
                return path                
            visited.add(current)
            for neighbour,_ in self.graph[current]:
                if neighbour not in visited:
                    newpath=path+[neighbour]
                    queue.append((neighbour,newpath))
        return None
    
if __name__=="__main__":
    print("SAY MY NAME!")
    graph=Solution()
    graphwithcost=Solution()
    edges={('A','B',1),('C','B',2),('B','O',3),('O','C',8),('R','O',2),('C','R',2)}
    for edge in edges:
        graphwithcost.addedgewithcost(*edge)#解包操作
        graph.addedge(edge[0],edge[1])
    # searchresult=graph.dfs('A')
    # print(searchresult)
    # cost,path=graphwithcost.ucs('A','R')
    # print(path,cost)
    # found,path=graph.dls('A','R',limit=3)
    # if found:
    #     print(path)
    # else:
    #     print(f"No path founded")
    # found,path=graph.ids('A','R',maxdepth=3)
    # if found:
    #     print(path)
    # else:
    #     print(f"No path founded")
    # path = graph.bs('A','R')
    # print(path)
    path=graphwithcost.gbfs('A','R')
    print(path)


