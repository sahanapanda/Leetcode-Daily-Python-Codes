class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :type rtype: int
        """
        # Step 1: Build the adjacency list and track degrees
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = [False] * n
        complete_components_count = 0
        
        # Step 2: Iterate through all nodes to find components
        for i in range(n):
            if not visited[i]:
                component_nodes = []
                
                # Step 3: Run DFS to collect all nodes in the current component
                stack = [i]
                visited[i] = True
                
                while stack:
                    curr = stack.pop()
                    component_nodes.append(curr)
                    for neighbor in adj[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            stack.append(neighbor)
                
                # Step 4: Check if the component is complete
                # Each node in a complete component of size V must have a degree of V - 1
                V = len(component_nodes)
                is_complete = True
                for node in component_nodes:
                    if len(adj[node]) != V - 1:
                        is_complete = False
                        break
                        
                if is_complete:
                    complete_components_count += 1
                    
        return complete_components_count
