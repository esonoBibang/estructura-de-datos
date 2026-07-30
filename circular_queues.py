import heapq

tasks = [] #the list of tasks

#insert task in to the tasks list
heapq.heappush(tasks, (3, "write report")) 
heapq.heappush(tasks,(1,"Call the user"))
heapq.heappush(tasks, (2, "fix critical bug")) 
heapq.heappush(tasks, (5, "reply to email"))
heapq.heappush(tasks,(4,"write name"))


print(tasks)
print("-----------------------")

while tasks:
    num,task = heapq.heappop(tasks)
    print(num,task)

print("-----------------------")
print(tasks)