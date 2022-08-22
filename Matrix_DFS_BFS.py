


#implentng adjacency matrix usig class 
#so I can access to one function from anoter
#inside the same class.
#Directed graph is one directional and and undirected one of bi directional.

from collections import deque

#Implenting adjacency matrix
class Graph:
    #Defining a matrix
    def __init__(self, nodes, directed=True):
        self.total_nodes= nodes
        self.directed= directed

        self.matrix=[]

        for row in range(nodes):
            self.matrix.append([0 for column in range(nodes)])

    #Adding edges
    def add_edge(self, node1, node2, weight=1):
        if (node1 or node2)>=0 and (node1 or node2)<self.total_nodes:
            self.matrix[node1][node2]= weight

            #when graph is bi directional or undirected.
            if self.directed!=True:
                self.matrix[node2][node1]= weight    
        else:
            print("Either node 1 or node 2 is out of range ")
            self.matrix[0][0]= 0    
   
    #deleting the edges.
    def del_edge(self, node1, node2):
        if (node1 or node2) >= 0 and (node1 or node2) <=self.total_nodes-1:
            self.matrix[node1][node2]=0
        
        if self.directed!=True:
            self.matrix[node2][node1]=0
               
    def print_matrix(self):
        row_index=0
        column_index=0
        total_node= self.total_nodes

        while row_index<=total_node:
            
            while column_index<=total_node:
               
                print(self.matrix[row_index][column_index], end=" ")   
                column_index=column_index+1
            
            print('\n')

            row_index = row_index+1
            column_index=0
    
    #Implementing BFS:
    #Strategy:
    #pick a node and put it in the sorted list and then put its vertices in the queue
    #pop one element from the quque and put that element in the sorted list 
    #and put all of its vertices in the queue.
    #keep repeating till the queue is empty.
    
    def BFS(self, node):
        node_index=0
        
        #contains all the visited nodes.
        visited_list= []
        
        #contains nodes without duplicates.
        Queue= deque([])
        
        #Adding a node to the Queue

        
        #Adding node to the list
        visited_list.append(node)

        #Finding all the children of the node. For node 1, lookig for values in [1,0], [1,1], [1,2], [1,N].
        #if they contain any value>1 then 1 has childen with those nodes.
        while node_index<self.total_nodes:      
            if self.matrix[node][node_index]>0:
                for items in visited_list:
                    #Only node_index that are not in the visted_list will into the Queue
                    if node_index not in visited_list:
                        Queue.appendleft(node_index)             
            node_index=node_index+1
        
        # While the Queue contains elements
        while len(Queue)>0:
            node_index=0
    
            #getting the first element from the Queue
            node= Queue[-1]
            
            #Preventing duplate getting inserted into the visited_list.
            for items in  visited_list:
                if node not in visited_list:
                    visited_list.append(node)
            
            #Finding all the children of the node. 
            #For example node 1, lookig for values in [1,0], [1,1], [1,2], [1,N].
            
            while node_index<self.total_nodes:
                if self.matrix[node][node_index]>0:
                    for items in visited_list:
                        #Only node_index that are not in the sorted_list will into the visited_list list
                        if node_index not in visited_list:
                            Queue.appendleft(node_index)      
                node_index=node_index+1
            
            #Deleting the top element from the Queue         
            Queue.pop()

      
        return visited_list

    
    #Implementing DFS
    #Strategies:
    #1. Pick a node and put it in the Stack and in the sorted_list.
    #2. pop one element from the stack and put it in the sorted_list 
    #3. and then find all of that element's children and put them in the stack.
    #4. Keep reapting step 2 and 3 till the stack gets empty.
    def DFS(self, node):
        node_index=0
        #stacks
        list1=[]
        #sorted_list
        sorted_list=[]
        sorted_list.append(node)
        
        #Finding all the children of the node. For node 1, lookig for values in [1,0], [1,1], [1,2], [1,N].
        while node_index<self.total_nodes:
            #if they contain any value>1 then 1 has childen with those nodes.
            if self.matrix[node][node_index]>0 and node!=node_index:
                
                #Preventing inserting dupliacte values into the stack
                    list1.append(node_index)
            node_index=node_index+1
        
        while len(list1)>0:
            node_index=0
            node= list1[-1]
            node_index1= list1.index(node)
            #Preventing inserting dupliacte values into the sorted_list
            for items in sorted_list:
                if node not in sorted_list:
                    sorted_list.append(node)
            
            while node_index<self.total_nodes:  
                if self.matrix[node][node_index]>0:
                    #Comparing the node_index with the sorted_list,
                    #Only node_index that are not in the sorted_list will into the list1 stack
                    for items in sorted_list:
                        if node_index not in sorted_list:
                            list1.append(node_index)            
                node_index=node_index+1

            del list1[node_index1]   
            
        
        return sorted_list


graph= Graph(11)

graph.add_edge(0,2,1)
graph.add_edge(0,4,1)
graph.add_edge(2,3,1)
graph.add_edge(2,5,1)
graph.add_edge(2,7,1)
graph.add_edge(2,8,1)

graph.add_edge(3,9,1)
graph.add_edge(3,10,1)
graph.add_edge(4,3,1)

graph.add_edge(5,6,1)
graph.add_edge(5,7,1)
graph.add_edge(5,8,1)

graph.add_edge(6,7,1)
graph.add_edge(7,8,1)
graph.add_edge(9,2,1)




DFS_list= graph.DFS(0)

BFS_list= graph.BFS(0)

print("DFS:", DFS_list)
print("BFS:", BFS_list)













   






    