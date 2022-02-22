import json
from graph import Graph


def q1a(g: Graph):
    result = ""
    max = -1
    count = 0
    for v in g.vertices:
        count = g.count_edges(v)
        if count >= max:
            result = v
            max = count
    return result

def q1b(g: Graph):
    result = ""
    min = len(g.vertices) - 1
    count = 0
    for v in g.vertices:
        count = g.count_edges(v)
        if count <= min:
            result = v
            min = count
    return result

def q2a(g: Graph):
    v = q1a(g)
    e = g.get_edges(v)
    result = []
    for i in e:
        if i[0] == v:
            result.append(i[1])
        else:
            result.append(i[0])
    return result

def q2b(g: Graph):
    v = q1b(g)
    e = g.get_edges(v)
    result = []
    for i in e:
        if i[0] == v:
            result.append(i[1])
        else:
            result.append(i[0])
    return result

def q3(g: Graph):
    return len(g.vertices)/len(g.edges)

def q4(g: Graph):
    hist_size = len(g.vertices)
    hist = [0] * hist_size
    total = []
    for i in g.vertices:
        total.append(g.count_edges(i))
    for i in total:
        hist[i] += 1
    return hist


g = Graph()

import json

data = json.load(open('data.json'))

for i in data['vertices']:
    g.vertices.add(i)

for i in data['edges']:
    edge = i.split("-")
    g.add_edge(edge[0], edge[1])

print("Q1 (maior): " + q1a(g))
print("Q1 (menor): " + q1b(g))
print("Q2 (maior): " + str(q2a(g)))
print("Q2 (menor): " + str(q2b(g)))
print("Q3: " + str(q3(g)))
print("Q4: " + str(q4(g)))
