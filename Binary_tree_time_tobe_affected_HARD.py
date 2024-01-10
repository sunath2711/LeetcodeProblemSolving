# You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.

# Each minute, a node becomes infected if:

# The node is currently uninfected.
# The node is adjacent to an infected node.
# Return the number of minutes needed for the entire tree to be infected.
class Solution(object):
    def amountOfTime(self, root, start):
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """
        G = self.tree_to_graph(root,graph=None)
        visited = set()
        que = deque([(start,0)])
        visited.add(start)
        min_time = 0

        while que:
            current_node,current_time = que.popleft()
            min_time = current_time

            for neighbour in G[current_node]:
                if neighbour not in visited:
                    que.append((neighbour,current_time+1))
                    visited.add(neighbour)
        return min_time                  

    def tree_to_graph(self,root,graph=None):
        if graph is None:
            graph = {}
        if root is not None:
            if root.val not in graph:
                graph[root.val] = []

            if root.left is not None:
                graph[root.val].append(root.left.val)
                if root.left.val not in graph:
                    graph[root.left.val] = []   
                graph[root.left.val].append(root.val)

            if root.right is not None:
                graph[root.val].append(root.right.val)
                if root.right.val not in graph:
                    graph[root.right.val] = []   
                graph[root.right.val].append(root.val) 

            self.tree_to_graph(root.left,graph)
            self.tree_to_graph(root.right,graph)

        return graph  

#Very good question 
#to learn Graphs and Trees and BFS
# since we have a tree and can only go in 2 dirctions left and right but we want to go back and find the largest distance 
# so we convert the tree to undirected graph to go all neighbours and then fursther and then going to farthest node
#we created a function tree_to_graph - good logic easy that reutrns a undirected graph
#then BFS - breadth first using queue is implemented by double ended queue in python to 
#visited set is created if node already visite dont add to set and its neightbours to queue, if not visited then add neighbours to queue then 
