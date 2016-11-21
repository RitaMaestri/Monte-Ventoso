import random as rnd
from itertools import chain
def find_path(graph, start, end, path):
    path += [start]
    if start == end:
        return path
    if graph[start] == []:
        return None
    for node in graph[start]:
        if node not in path and (len(graph[node]) > 1 or node == end):
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

def generate_graph(end,graph,path,max_children,start=0):

    def maieutica():
        last_node = 0 if start==0 else max(chain.from_iterable(graph.values()))
        endpoint = max_children if (end - last_node) > max_children else end - last_node
        return range(last_node+1,rnd.randint(last_node+1,last_node+endpoint+1))

    def taigeto():
        """due nodi possono solo connettersi allo stesso figlio se sono 
        adiacenti e non vi sono altri figli 'di mezzo' (i nodi vengono ordinati 
        in ordine di grandezza)"""
        if start == 0 or start in graph[start-1] or graph[start-1] == [] or rnd.random() > 0.2: return []
        return [max(graph[start-1])]

    if start in path: 
        for child in graph[start]:
            generate_graph(end,graph, path,max_children,child)
        graph[start] += taigeto()
        path.pop(0)
        if path == []: return graph
    else:
        graph[start] = [child for child in maieutica()]
        path.append(start)
        if path[0] != start: return None
    return generate_graph(end,graph,path,max_children,path[0])



            
  

def graph_traversable(graph): return find_path(graph,0,max(graph.keys()),[]) is not None

def generate_traversable_graph(num_nodes):
    while True:
        graph = generate_graph(num_nodes,{},0) 
        if graph_traversable(graph): return graph


print(generate_graph(20,{},[],6))
