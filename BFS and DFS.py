n=int(input("\nEnter number of nodes: "))
d={k:[] for k in range(1,n+1)}
i=input("\nEnter the edges: \n")
while(i!="DONE"):
    l=list(map(int,i.split("->")))
    d[l[0]].append(l[1])
    i=input()
goal=int(input("\nEnter the goal: "))
#BFS:
bfs=[1];r=1
while(goal not in bfs):
    if d[r]!=[]:
        bfs.extend(d[r])
        r+=1
while(bfs[len(bfs)-1]!=goal):
    bfs.pop()
print("\nBreadth First Search : ",end="")
print(*bfs,sep=" -> ")
print("Cost is : ",len(bfs)-1)
#DFS:
dfs=[goal];
for i in range(len(d),0,-1):
    if goal in d[i]:
        goal=i
        dfs.append(goal)
dfs.reverse()
print("\nDepth First Search : ",end="")
print(*dfs,sep=" -> ")
print("Cost is : ",len(dfs)-1)
