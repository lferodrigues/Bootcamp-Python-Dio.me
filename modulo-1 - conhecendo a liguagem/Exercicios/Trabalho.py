import random

# criar 100 vértices
vertices = list(range(1, 101))

# gerar um número aleatório de arestas
num_arestas = random.randint(100, 1000)

# criar o grafo vazio
grafo = {}

# adicionar as arestas
for i in range(num_arestas):
    # escolher dois vértices aleatoriamente
    u, v = random.sample(vertices, 2)
    
    # verificar se já existe uma aresta entre esses dois vértices
    if u not in grafo:
        grafo[u] = set()
    if v not in grafo:
        grafo[v] = set()
    if v not in grafo[u]:
        # adicionar a aresta
        grafo[u].add(v)
        grafo[v].add(u)
    else:
        # tentar novamente até 10 vezes
        for j in range(10):
            u, v = random.sample(vertices, 2)
            if u not in grafo:
                grafo[u] = set()
            if v not in grafo:
                grafo[v] = set()
            if v not in grafo[u]:
                grafo[u].add(v)
                grafo[v].add(u)
                break

# imprimir o grafo
print(grafo)
