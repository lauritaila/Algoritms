#Breadth-irst search tells you if there’s a path from A to B.
#If there’s a path, breadth-irst search will ind the shortest path.
#Breadth-irst search is use in graph
#Breadth-irst search is used to calculate the shortest path for an unweighted graph.

from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

#Creates a new queue
search_queue = deque() 
#Adds all of your neighbors to the search queue
search_queue += graph["you"]  

#function to tell you when someone is a mango seller.
def person_is_seller(name):
  return name[-1] == "m"

#breadth-irst search
def search(name):
  search_queue = deque()
  search_queue += graph[name]
  # This array is how you keep track of which people you’ve searched before.
  searched = [] 
  # While the queue isn’t empty …
  while search_queue:
    #… grabs the first person off the queue
    person = search_queue.popleft()  
    #Only search this person if you haven’t already searched them.
    if not person in searched: 
      #Checks whether the person is a mango seller
      if person_is_seller(person): 
        print (person + " is a mango seller!")
        return True
      else:
        search_queue += graph[person]
        # Marks this person as searched
        searched.append(person) 
  return False

search("you")

