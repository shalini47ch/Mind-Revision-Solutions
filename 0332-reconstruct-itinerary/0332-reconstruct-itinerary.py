class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #here lets first build the graph and then apply the hierholzer algo
        graph=defaultdict(list)
        #sort the tickets in descending order
        tickets.sort(reverse=True)
        for u,v in tickets:
            graph[u].append(v)
        #now the next step is to perform dfs 
        itinerary=[]
        def dfs(airport):
            while graph[airport]:
                nextpair=graph[airport].pop()
                dfs(nextpair)
            itinerary.append(airport)
        dfs("JFK")
        return itinerary[::-1]


      



        


       
        
        

        